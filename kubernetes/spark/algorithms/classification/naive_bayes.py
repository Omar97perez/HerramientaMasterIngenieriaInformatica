from __future__ import print_function

import os
from time import time
from matplotlib import pyplot as plt

from pyspark.ml.classification import NaiveBayes
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import StringIndexer, VectorIndexer, VectorAssembler
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("NaiveBayes")\
        .getOrCreate()

    # $example on$
    # Load training data
    data = spark.read.load("/mnt/work/" + os.environ.get('FILE_NAME_IN'), format="csv", sep=",", inferSchema="true", header="true")

    columnaInicial = int(os.environ.get('COLUMNA_INICIAL'))
    columnaFinal = int(os.environ.get('COLUMNA_FINAL'))
    array = data.columns

    start_time = time() # Comienzo de contar tiempo

    data = VectorAssembler(inputCols=array[columnaInicial:columnaFinal], outputCol="features").transform(data)

    # Automatically identify categorical features, and index them.
    # We specify maxCategories so features with > 4 distinct values are treated as continuous.
    featureIndexer =\
        VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=12).fit(data)

    # Split the data into train and test
    splits = data.randomSplit([0.7, 0.3])
    train = splits[0]
    test = splits[1]

    # create the trainer and set its parameters
    nb = NaiveBayes(smoothing=1.0, labelCol=array[columnaInicial], modelType="multinomial", featuresCol="indexedFeatures")

    # Pipeline
    pipeline = Pipeline(stages=[featureIndexer, nb])

    # train the model
    model = pipeline.fit(train)

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'

    # select example rows to display.
    predictions = model.transform(test)
    predictions.show()

    # compute accuracy on the test set
    evaluator = MulticlassClassificationEvaluator(labelCol=array[columnaInicial], predictionCol="prediction",
                                                  metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Test set accuracy = " + str(accuracy))
    # $example off$

    validation = predictions.toPandas()

    fig, ax = plt.subplots()
    fig.suptitle("Decision Tree Classification (" + str(accuracy) + ")\n" + salida)
    ax.scatter(validation[array[columnaInicial]], validation['prediction'], edgecolors=(0, 0, 0))
    ax.plot([validation[array[columnaInicial]].min(), validation[array[columnaInicial]].max()], [validation[array[columnaInicial]].min(), validation[array[columnaInicial]].max()], 'k--', lw=2)
    ax.set_xlabel('Medido')
    ax.set_ylabel('Predecido')
    plt.savefig("/mnt/work/" + str(os.environ.get("FILE_NAME_EXIT")))

    spark.stop()