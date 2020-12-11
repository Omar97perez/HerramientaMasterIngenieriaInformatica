import matplotlib.pyplot as plt
import pandas as pd
import StrategyFile as sf
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
nombreFichero = fichero[0]
fichero = fichero[0] + ".csv"

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
    algoritmoSeleccionado = int(input('¿Qué algoritmo quiere ejecutar?: \n\t 1. Regresión Lineal. \n\t 2. Árbol de Regresión. \n\t 3. Regresión árbol Aleatorio. \n\t 4. Red Neuronal.\n  > '))
    columnaSeleccionadaInicial = int(input('¿Qué columna inicial quiere analizar?\n > '))
    columnaSeleccionadaFinal = int(input('¿Qué columna final quiere analizar?\n > '))
    valoresPredecir = input('¿Qué valores tiene para predecir?\n > ')
else:
    algoritmoSeleccionado = int(sys.argv[3])
    columnaSeleccionadaInicial = int(sys.argv[4])
    columnaSeleccionadaFinal = int(sys.argv[5])
    columnaSeleccionada = int(sys.argv[6])
    valoresPredecir = sys.argv[7]
    rutaEscribirJson = sys.argv[8]

array = df.values
X = (array[:,columnaSeleccionadaInicial:columnaSeleccionadaFinal])
Y = (array[:,columnaSeleccionada])

if algoritmoSeleccionado == 1:
    model = LinearRegression()
elif algoritmoSeleccionado == 2:
    model = DecisionTreeRegressor()
elif algoritmoSeleccionado == 3:
    model = RandomForestRegressor()
elif algoritmoSeleccionado == 4:
    model = MLPRegressor()
else:
    print("El algoritmo introducido no existe")
    sys.exit()

valorSplit = valoresPredecir.split(",")
valorMap = list(map(float, valorSplit))

valoresPredecir = np.array([valorMap])
reg = model.fit(X, Y)
result = reg.predict(valoresPredecir)

validation_size = 0.22
seed = 123
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold)
msg = "%s (%f) \n %s (%f)" % ('Predicción:', result, 'Porcentaje de acierto:', cv_results.mean())

model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

fig = plt.figure()
fig.suptitle(msg)
ax = fig.add_subplot(111)
plt.boxplot(cv_results)
# ax.set_xticklabels('BR')

if(pedirParametros == 1):
    plt.show()
else:
    print(nombreFichero)
    plt.savefig(nombreFichero)