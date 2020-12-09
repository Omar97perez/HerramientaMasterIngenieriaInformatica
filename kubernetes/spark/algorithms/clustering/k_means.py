from __future__ import print_function

import os
from time import time
from matplotlib import pyplot as plt

from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.feature import StringIndexer, VectorIndexer, VectorAssembler

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("KMeansExample")\
        .getOrCreate()

    # Loads data.
    data = spark.read.load("/mnt/work/" + os.environ.get('FILE_NAME_IN'), format="csv", sep=",", inferSchema="true", header="true")

    columnaInicial = int(os.environ.get('COLUMNA_INICIAL'))
    columnaFinal = int(os.environ.get('COLUMNA_FINAL'))
    array = data.columns

    start_time = time() # Comienzo de contar tiempo

    data = VectorAssembler(inputCols=array[columnaInicial:columnaFinal], outputCol="features").transform(data)

    # Trains a k-means model.
    kmeans = KMeans().setK(4)
    model = kmeans.fit(data)

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'

    # Make predictions
    predictions = model.transform(data)

    # Evaluate clustering by computing Silhouette score
    evaluator = ClusteringEvaluator()

    silhouette = evaluator.evaluate(predictions)
    print("Silhouette with squared euclidean distance = " + str(silhouette))

    # Shows the result.
    centers = model.clusterCenters()
    print("Cluster Centers: ")
    for center in centers:
        print(center)

    validation = predictions.toPandas()

    fig, ax = plt.subplots()
    fig.suptitle("K-Means Clustering (Silhouette score" + str(silhouette) + ")\n" + salida)
    ax.scatter(validation[array[columnaFinal]], validation[array[columnaInicial]], c=validation['prediction'], cmap="viridis")
    plt.savefig("/mnt/work/" + str(os.environ.get("FILE_NAME_EXIT")))

    spark.stop()