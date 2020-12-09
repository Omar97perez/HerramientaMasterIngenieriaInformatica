from __future__ import print_function

import os
from time import time
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.feature import StringIndexer, VectorIndexer, VectorAssembler
from pyspark.ml.evaluation import RegressionEvaluator
from matplotlib import pyplot as plt

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("DecisionTreeRegression")\
        .getOrCreate()

    # Load training data
    data = spark.read.load("/mnt/work/" + os.environ.get('FILE_NAME_IN'), format="csv",
                           sep=",", inferSchema="true", header="true")

    columnaInicial = int(os.environ.get('COLUMNA_INICIAL'))
    columnaFinal = int(os.environ.get('COLUMNA_FINAL'))
    array = data.columns

    start_time = time() # Comienzo de contar tiempo

    data = VectorAssembler(inputCols=array[columnaInicial:columnaFinal], outputCol="features").transform(data)

    # Automatically identify categorical features, and index them.
    # We specify maxCategories so features with > 4 distinct values are treated as continuous.
    featureIndexer =\
        VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=12).fit(data)

    (trainingData, testData) = data.randomSplit([0.7, 0.3])

    dtr = DecisionTreeRegressor(labelCol=array[columnaFinal], featuresCol="indexedFeatures")

    # Chain indexer and tree in a Pipeline
    pipeline = Pipeline(stages=[featureIndexer, dtr])

    # Train model.  This also runs the indexer.
    model = pipeline.fit(trainingData)

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'

    dtr_predictions = model.transform(testData)
    
    dtr_evaluator = RegressionEvaluator(predictionCol="prediction",
                                    labelCol=array[columnaFinal], metricName="rmse")

    rmse = dtr_evaluator.evaluate(dtr_predictions)

    print("Root Mean Squared Error (RMSE) on test data = %g" % rmse)

    treeModel = model.stages[1]
    # summary only
    print(treeModel)

    validation = dtr_predictions.toPandas()

    fig, ax = plt.subplots()
    fig.suptitle("Decision Tree Regression ( RMSE:" + str(rmse) + ")\n" + salida)
    ax.scatter(validation[array[columnaFinal]], validation['prediction'], edgecolors=(0, 0, 0))
    ax.plot([validation[array[columnaFinal]].min(), validation[array[columnaFinal]].max()], [validation[array[columnaFinal]].min(), validation[array[columnaFinal]].max()], 'k--', lw=2)
    ax.set_xlabel('Medido')
    ax.set_ylabel('Predecido')
    plt.savefig("/mnt/work/" + str(os.environ.get("FILE_NAME_EXIT")))

    spark.stop()
