#-*- coding: utf-8-*-

from __future__ import print_function

import os
from time import time
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import StringIndexer, VectorIndexer, VectorAssembler
from pyspark.ml.evaluation import RegressionEvaluator
from matplotlib import pyplot as plt



if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("GeneralizedLinearRegressionExample")\
        .getOrCreate()

    # $example on$
    # Load training data
    data = spark.read.load("/mnt/work/" + os.environ.get('FILE_NAME_IN'), format="csv",
                           sep=",", inferSchema="true", header="true")

    columnaInicial = int(os.environ.get('COLUMNA_INICIAL'))
    columnaFinal = int(os.environ.get('COLUMNA_FINAL'))
    array = data.columns

    start_time = time() # Comienzo de contar tiempo

    data = VectorAssembler(inputCols=array[columnaInicial:columnaFinal], outputCol="features").transform(data)

    (trainingData, testData) = data.randomSplit([0.7, 0.3])

    lr = LinearRegression(labelCol=array[columnaFinal], maxIter=10,
                          regParam=0.3, elasticNetParam=0.8)

    # Fit the model
    model = lr.fit(trainingData)

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'

    # Print the coefficients and intercept for generalized linear regression model
    print("Coefficients: " + str(model.coefficients))
    print("Intercept: " + str(model.intercept))

    # Summarize the model over the training set and print out some metrics
    trainingSummary = model.summary
    print("numIterations: %d" % trainingSummary.totalIterations)
    print("objectiveHistory: %s" % str(trainingSummary.objectiveHistory))
    trainingSummary.residuals.show()
    print("RMSE: %f" % trainingSummary.rootMeanSquaredError)
    print("r2: %f" % trainingSummary.r2)

    lr_predictions = model.transform(testData)
    
    lr_evaluator = RegressionEvaluator(predictionCol="prediction",
                                    labelCol=array[columnaFinal], metricName="r2")
    print("R Squared (R2) on test data = %g" %
        lr_evaluator.evaluate(lr_predictions))

    test_result = model.evaluate(testData)
    print("Root Mean Squared Error (RMSE) on test data = %g" % test_result.rootMeanSquaredError)

    validation = lr_predictions.toPandas()

    fig, ax = plt.subplots()
    fig.suptitle("Decision Tree Classification (R2: " + str(trainingSummary.r2) + ")\n" + salida)
    ax.scatter(validation[array[columnaFinal]], validation['prediction'], edgecolors=(0, 0, 0))
    ax.plot([validation[array[columnaFinal]].min(), validation[array[columnaFinal]].max()], [validation[array[columnaFinal]].min(), validation[array[columnaFinal]].max()], 'k--', lw=2)
    ax.set_xlabel('Medido')
    ax.set_ylabel('Predecido')
    plt.savefig("/mnt/work/" + str(os.environ.get("FILE_NAME_EXIT")))

    spark.stop()
