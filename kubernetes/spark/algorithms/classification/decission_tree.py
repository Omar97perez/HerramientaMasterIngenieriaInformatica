from __future__ import print_function

import os
from time import time
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.linalg import Vectors
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer, VectorAssembler
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from matplotlib import pyplot as plt


if __name__ == "__main__":

    spark = SparkSession.builder.appName("DecisionTreeClassifier").getOrCreate()

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

    # Split the data into training and test sets (30% held out for testing)
    (trainingData, testData) = data.randomSplit([0.7, 0.3])

    # Train a DecisionTree model.
    dt = DecisionTreeClassifier(labelCol=array[columnaInicial], featuresCol="indexedFeatures")

    # Chain indexers and tree in a Pipeline
    pipeline = Pipeline(stages=[featureIndexer, dt])

    # Train model.  This also runs the indexers.
    model = pipeline.fit(trainingData)

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'

    # Make predictions.
    predictions = model.transform(testData)

    # Select (prediction, true label) and compute test error
    evaluator = MulticlassClassificationEvaluator(
        labelCol=array[columnaInicial], predictionCol="prediction", metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Accuracy = %g" % accuracy)
    print("Test Error = %g " % (1.0 - accuracy))

    treeModel = model.stages[1]
    # summary only
    print(treeModel)

    validation = predictions.toPandas()

    fig, ax = plt.subplots()
    fig.suptitle("Decision Tree Classification (" + str(accuracy) + ")\n" + salida)
    ax.scatter(validation[array[columnaInicial]], validation['prediction'], edgecolors=(0, 0, 0))
    ax.plot([validation[array[columnaInicial]].min(), validation[array[columnaInicial]].max()], [validation[array[columnaInicial]].min(), validation[array[columnaInicial]].max()], 'k--', lw=2)
    ax.set_xlabel('Medido')
    ax.set_ylabel('Predecido')
    plt.savefig("/mnt/work/" + str(os.environ.get("FILE_NAME_EXIT")))
    