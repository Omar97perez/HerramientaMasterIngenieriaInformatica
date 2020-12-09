#-*- coding: utf-8-*-

import matplotlib.pyplot as plt
import pandas as pd
import StrategyFile as sf
import StrategyAlgorithm as st
import sys
import string
import os
import geopandas as gpd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression, RANSACRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_predict, train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn import model_selection
from pandas.plotting import scatter_matrix
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from time import time


pedirParametros = int(sys.argv[2])

#Cargamos los datos de un fichero
file = sys.argv[1]
fichero = os.path.splitext(file)
fichero = fichero[0] + ".csv"
nombreFichero = ""

if file.endswith('.csv'):
    fileSelected = sf.Csv(file, fichero)
    df = fileSelected.collect()
elif file.endswith('.json'):
    fileSelected= sf.Json(file, fichero)
    df = fileSelected.collect()
elif file.endswith('.xlsx'):
    fileSelected= sf.Xlsx(file, fichero)
    df = fileSelected.collect()
else:
    print("Formato no soportado")
    sys.exit()

if(pedirParametros == 1):
    algoritmoSeleccionado = int(input('¿Qué algoritmo quiere ejecutar?: \n\t 1. Clasificación Bayesiana. \n\t 2. Decision Tree Regression. \n\t 3. Mean Shift. \n\t 4. Linear Regresion. \n\t 5. Random Forest. \n\t 6. MLPRegressor. \n\t 7. Comparativa Regresión. \n\t 8. Comparativa Clasificación. \n\t 9. Agglomerative Clustering. \n\t 10. Comparativa Clustering. \n\t 11. DBSCAN. \n\t 12. Clasificador Gausiano.\n  > '))
    columnaSeleccionadaInicial = int(input('¿Qué columna inicial quiere analizar?\n > '))
    columnaSeleccionada = int(input('¿Qué columna final quiere analizar?\n > '))

else:
    algoritmoSeleccionado = int(sys.argv[3])
    columnaSeleccionadaInicial = int(sys.argv[4])
    columnaSeleccionada = int(sys.argv[5])
    nombreFichero = sys.argv[6]

array = df.values
X = (array[:,columnaSeleccionadaInicial:columnaSeleccionada])
Y = (array[:,columnaSeleccionada])

if algoritmoSeleccionado == 1:
  graficaFinal = st.BR(X, Y, pedirParametros, nombreFichero)
  graficaFinal.grafica()
elif algoritmoSeleccionado == 2:
  graficaFinal= st.DecisionTreeRegression(X, Y, pedirParametros, nombreFichero)
  graficaFinal.grafica()
elif algoritmoSeleccionado == 3:
  graficaFinal = st.MeanShift1(X, Y, pedirParametros, nombreFichero)
  graficaFinal.grafica()
elif algoritmoSeleccionado == 4:
  graficaFinal= st.LinearRegresion(X, Y, pedirParametros, nombreFichero)
  graficaFinal.grafica()
elif algoritmoSeleccionado == 5:
  graficaFinal= st.RandomForestRegressorSA(X, Y, pedirParametros, nombreFichero)
  graficaFinal.grafica()
elif algoritmoSeleccionado == 6:
  graficaFinal= st.MLPRegressorSA(X, Y, pedirParametros, nombreFichero)
  graficaFinal.grafica()
elif algoritmoSeleccionado == 7:
  graficaFinal= st.ComparativeRegression(X, Y, pedirParametros, nombreFichero)
  graficaFinal.grafica()
elif algoritmoSeleccionado == 8:
  iris = datasets.load_iris()
  X = iris.data[:, 0:2]  # we only take the first two features for visualization
  Y = iris.target
  # X = (array[:,columnaSeleccionada-2:columnaSeleccionada])
  graficaFinal= st.ComparativeClasification(X, Y, pedirParametros, nombreFichero)
  graficaFinal.grafica()
elif algoritmoSeleccionado == 9:
  graficaFinal= st.AgglomerativeClusteringSA(X, Y, pedirParametros, nombreFichero)
  graficaFinal.grafica()
elif algoritmoSeleccionado == 10:
  graficaFinal= st.ComparativeClustering(X, Y, pedirParametros, nombreFichero)
  graficaFinal.grafica()
elif algoritmoSeleccionado == 11:
  graficaFinal= st.DBSCANSA(X, Y, pedirParametros, nombreFichero)
  graficaFinal.grafica()
elif algoritmoSeleccionado == 12:
  # iris = datasets.load_iris()
  # X = iris.data[:, 0:2]  # we only take the first two features for visualization
  # Y = iris.target
  X = (array[:,columnaSeleccionada-2:columnaSeleccionada])
  graficaFinal= st.GaussianProcessClassifierSA(X, Y, pedirParametros, nombreFichero)
  graficaFinal.grafica()
else:
  print("El algoritmo introducido no existe")