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
from joblib import parallel_backend

n_jobs_parrallel=3

def plot_dendrogram(model, **kwargs):
  # Create linkage matrix and then plot the dendrogram

  # create the counts of samples under each node
  counts = np.zeros(model.children_.shape[0])
  n_samples = len(model.labels_)
  for i, merge in enumerate(model.children_):
      current_count = 0
      for child_idx in merge:
          if child_idx < n_samples:
              current_count += 1  # leaf node
          else:
              current_count += counts[child_idx - n_samples]
      counts[i] = current_count

  linkage_matrix = np.column_stack([model.children_, model.distances_,
                                    counts]).astype(float)

  # Plot the corresponding dendrogram
  dendrogram(linkage_matrix, **kwargs)

class Algorithm:
    def __init__(self, X,Y,pedirParametros, nombreFichero):
      self.X = X
      self.Y = Y
      self.pedirParametros = pedirParametros
      self.nombreFichero = nombreFichero

class BR(Algorithm):
  def grafica(self):
    validation_size = 0.22
    seed = 123
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(self.X, self.Y, test_size=validation_size, random_state=seed)
    model = linear_model.BayesianRidge()

    start_time = time()
    with parallel_backend('threading', n_jobs=n_jobs_parrallel):
      kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
      model.fit(X_train, Y_train)
      predictions = model.predict(X_validation)

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold)
    msg = 'Clasificador Bayesiano ' + '(' + str(format(cv_results.mean(),'.4f')) + ') \n' +  salida

    fig, ax = plt.subplots()
    fig.suptitle( msg)
    ax.scatter(Y_validation, predictions, edgecolors=(0, 0, 0))
    ax.plot([Y_validation.min(), Y_validation.max()], [Y_validation.min(), Y_validation.max()], 'k--', lw=2)
    ax.set_xlabel('Medido')
    ax.set_ylabel('Predecido')
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

    if(self.pedirParametros == 1):
        fig = plt.figure() 
        fig.suptitle('Diagrama de Cajas y Bigotes para BR')
        ax = fig.add_subplot(111)
        plt.boxplot(cv_results)
        ax.set_xticklabels('BR')
        plt.show()

class DecisionTreeRegression(Algorithm):
  def grafica(self):
    validation_size = 0.22
    seed = 123
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(self.X, self.Y, test_size=validation_size, random_state=seed)
    model = DecisionTreeRegressor()
    start_time = time()
    with parallel_backend('threading', n_jobs=n_jobs_parrallel):
      kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
      model.fit(X_train, Y_train)
      predictions = model.predict(X_validation)

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold)
    msg = 'Árbol de decisión ' + '(' + str(format(cv_results.mean(),'.4f')) + ') \n' +  salida

    fig, ax = plt.subplots()
    fig.suptitle( msg)
    ax.scatter(Y_validation, predictions, edgecolors=(0, 0, 0))
    ax.plot([Y_validation.min(), Y_validation.max()], [Y_validation.min(), Y_validation.max()], 'k--', lw=2)
    ax.set_xlabel('Medido')
    ax.set_ylabel('Predecido')
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

    if(self.pedirParametros == 1):
        fig = plt.figure()
        fig.suptitle('Diagrama de Cajas y Bigotes para Decision Tree Regression')
        ax = fig.add_subplot(111)
        plt.boxplot(cv_results)
        ax.set_xticklabels('BR')
        plt.show()
        
class MeanShift1(Algorithm):
  def grafica(self):
    ms = MeanShift(bin_seeding=True)
    ms.fit(self.X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    print("number of estimated clusters : %d" % n_clusters_)

    import matplotlib.pyplot as plt
    from itertools import cycle

    plt.figure(1)
    plt.clf()

    colors = cycle('bgrcmyk')
    start_time = time()
    with parallel_backend('threading', n_jobs=n_jobs_parrallel):    
      for k, col in zip(range(n_clusters_), colors):
          my_members = labels == k
          cluster_center = cluster_centers[k]
          plt.plot(self.X[my_members, 0], self.X[my_members, 1], col + '.')
          plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                  markeredgecolor='k', markersize=14)
    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.8f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'
    plt.title('Estimated number of clusters:' + str(n_clusters_) + '\n' + salida)    
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

class LinearRegresion(Algorithm):
  def grafica(self):
    validation_size = 0.22
    seed = 123
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(self.X, self.Y, test_size=validation_size, random_state=seed)
    model = LinearRegression()
    start_time = time()
    with parallel_backend('threading', n_jobs=n_jobs_parrallel):
      kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
      model.fit(X_train, Y_train)
      predictions = model.predict(X_validation)

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold)
    msg = 'Regresión Lineal ' + '(' + str(format(cv_results.mean(),'.4f')) + ') \n' +  salida


    fig, ax = plt.subplots()
    fig.suptitle( msg)
    ax.scatter(Y_validation, predictions, edgecolors=(0, 0, 0))
    ax.plot([Y_validation.min(), Y_validation.max()], [Y_validation.min(), Y_validation.max()], 'k--', lw=2)
    ax.set_xlabel('Medido')
    ax.set_ylabel('Predecido')
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

    if(self.pedirParametros == 1):
        fig = plt.figure()
        fig.suptitle('Diagrama de Cajas y Bigotes para Decision Tree Regression')
        ax = fig.add_subplot(111)
        plt.boxplot(cv_results)
        ax.set_xticklabels('BR')
        plt.show()

class RandomForestRegressorSA(Algorithm):
  def grafica(self):
    validation_size = 0.22
    seed = 123
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(self.X, self.Y, test_size=validation_size, random_state=seed)
    model = RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=2,max_features='sqrt', max_leaf_nodes=None)
    start_time = time()
    with parallel_backend('threading', n_jobs=n_jobs_parrallel):
      kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
      model.fit(X_train, Y_train)
      predictions = model.predict(X_validation)

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold)
    msg = 'Random Forest Regressor ' + '(' + str(format(cv_results.mean(),'.4f')) + ') \n' +  salida

    fig, ax = plt.subplots()
    fig.suptitle( msg)
    ax.scatter(Y_validation, predictions, edgecolors=(0, 0, 0))
    ax.plot([Y_validation.min(), Y_validation.max()], [Y_validation.min(), Y_validation.max()], 'k--', lw=2)
    ax.set_xlabel('Medido')
    ax.set_ylabel('Predecido')
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

    if(pedirParametros == 1):
        fig = plt.figure()
        fig.suptitle('Diagrama de Cajas y Bigotes para Decision Tree Regression')
        ax = fig.add_subplot(111)
        plt.boxplot(cv_results)
        ax.set_xticklabels('BR')
        plt.show()

class MLPRegressorSA(Algorithm):
  def grafica(self):
    validation_size = 0.22
    seed = 123
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(self.X, self.Y, test_size=validation_size, random_state=seed)
    model = MLPRegressor()
    start_time = time()
    with parallel_backend('threading', n_jobs=n_jobs_parrallel):
      kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
      model.fit(X_train, Y_train)
      predictions = model.predict(X_validation)

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold)
    msg = 'Red Neuronal ' + '(' + str(format(cv_results.mean(),'.4f')) + ') \n' +  salida

    fig, ax = plt.subplots()
    fig.suptitle( msg)
    ax.scatter(Y_validation, predictions, edgecolors=(0, 0, 0))
    ax.plot([Y_validation.min(), Y_validation.max()], [Y_validation.min(), Y_validation.max()], 'k--', lw=2)
    ax.set_xlabel('Medido')
    ax.set_ylabel('Predecido')
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

    if(pedirParametros == 1):
        fig = plt.figure()
        fig.suptitle('Diagrama de Cajas y Bigotes para Decision Tree Regression')
        ax = fig.add_subplot(111)
        plt.boxplot(cv_results)
        ax.set_xticklabels('BR')
        plt.show()

class ComparativeRegression(Algorithm):
  def grafica(self):
    validation_size = 0.22
    seed = 123
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(self.X, self.Y, test_size=validation_size, random_state=seed)
    models = []

    models.append(('LR', LinearRegression()))

    models.append(('DTR', DecisionTreeRegressor()))

    models.append(('RF',RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=2,
            max_features='auto', max_leaf_nodes=None,
            )))

    models.append(('RF(LOG)',RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=2,
            max_features='log2', max_leaf_nodes=None,
            )))

    models.append(('RF(Sqrt)',RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=2,
            max_features='sqrt', max_leaf_nodes=None,
            )))

    models.append(('RF(4)',RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=2,
            max_features=4, max_leaf_nodes=None,
            )))

    models.append(('NN',MLPRegressor()))

    results = []
    names = []
    start_time = time()
    with parallel_backend('threading', n_jobs=n_jobs_parrallel):
      for name, model in models:
          kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
          cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold)
          results.append(cv_results)
          names.append(name)
          msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
          print(msg)

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')

    fig = plt.figure()
    fig.suptitle('Comparacion de los algoritmos \n Tiempo ejecución:' + str(elapsed_time) + ' segundos')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)

    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

class ComparativeClasification(Algorithm):
  def grafica(self):
    n_features = self.X.shape[1]
    C = 10
    kernel = 1.0 * RBF([1.0, 1.0])  # for GPC

    # Create different classifiers.
    classifiers = {
        'L1 logistic': LogisticRegression(C=C, penalty='l1',
                                          solver='saga',
                                          multi_class='multinomial',
                                          max_iter=10000),
        'L2 logistic (Multinomial)': LogisticRegression(C=C, penalty='l2',
                                                        solver='saga',
                                                        multi_class='multinomial',
                                                        max_iter=10000),
        'L2 logistic (OvR)': LogisticRegression(C=C, penalty='l2',
                                                solver='saga',
                                                multi_class='ovr',
                                                max_iter=10000),
        'Linear SVC': SVC(kernel='linear', C=C, probability=True,
                          random_state=0),
        'GPC': GaussianProcessClassifier(kernel)
    }

    n_classifiers = len(classifiers)

    plt.figure(figsize=(3 * 2, n_classifiers * 2))
    plt.subplots_adjust(bottom=.2, top=.95)

    xx = np.linspace(3, 9, 100)
    yy = np.linspace(1, 5, 100).T
    xx, yy = np.meshgrid(xx, yy)
    Xfull = np.c_[xx.ravel(), yy.ravel()]


    start_time = time()
    with parallel_backend('threading', n_jobs=n_jobs_parrallel):
      for index, (name, classifier) in enumerate(classifiers.items()):
          classifier.fit(self.X, self.Y)

          y_pred = classifier.predict(self.X)
          accuracy = accuracy_score(self.Y, y_pred)
          print("Accuracy (train) for %s: %0.1f%% " % (name, accuracy * 100))

          # View probabilities:
          probas = classifier.predict_proba(Xfull)
          n_classes = np.unique(y_pred).size
          for k in range(n_classes):
              plt.subplot(n_classifiers, n_classes, index * n_classes + k + 1)
              plt.title("Class %d" % k)
              if k == 0:
                  plt.ylabel(name)
              imshow_handle = plt.imshow(probas[:, k].reshape((100, 100)),
                                        extent=(3, 9, 1, 5), origin='lower')
              plt.xticks(())
              plt.yticks(())
              idx = (y_pred == k)
              if idx.any():
                  plt.scatter(self.X[idx, 0], self.X[idx, 1], marker='o', c='w', edgecolor='k')

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')

    ax = plt.axes([0.15, 0.04, 0.7, 0.05])
    plt.title('Probability \n' + 'Tiempo ejecución:' + str(elapsed_time) + ' segundos')
    plt.colorbar(imshow_handle, cax=ax, orientation='horizontal')

    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

class AgglomerativeClusteringSA(Algorithm):
  def grafica(self):
    start_time = time()
    with parallel_backend('threading', n_jobs=n_jobs_parrallel):
      model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
      model = model.fit(self.X)
    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'
    plt.title('Hierarchical Clustering Dendrogram \n' + salida)
    plot_dendrogram(model, truncate_mode='level', p=3)
    plt.xlabel("Number of points in node (or index of point if no parenthesis).")
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

class ComparativeClustering(Algorithm):
  def grafica(self):
    import matplotlib.pyplot as plt
    from itertools import cycle
    import numpy as np
    
    plt.figure(figsize=(9, 3))
    plt.subplot(131)

    ms = MeanShift(bin_seeding=True)
    ms.fit(self.X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_
    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    colors = cycle('bgrcmyk')
    start_time = time()
    with parallel_backend('threading', n_jobs=n_jobs_parrallel):
      for k, col in zip(range(n_clusters_), colors):
          my_members = labels == k
          cluster_center = cluster_centers[k]
          plt.plot(self.X[my_members, 0], self.X[my_members, 1], col + '.')
          plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                  markeredgecolor='k', markersize=14)
    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'
    plt.title('MeanShift Estimated number of clusters:' + str(n_clusters_) + '\n' + salida)

    plt.subplot(132)
    model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

    model = model.fit(self.X)
    plt.title('Hierarchical Clustering Dendrogram')
    # plot the top three levels of the dendrogram
    plot_dendrogram(model, truncate_mode='level', p=3)
    plt.xlabel("Number of points in node (or index of point if no parenthesis).")

    plt.subplot(133)

    import numpy as np
    from sklearn.cluster import DBSCAN
    from sklearn import metrics
    from sklearn.datasets import make_blobs
    from sklearn.preprocessing import StandardScaler

    # #############################################################################
    # Compute DBSCAN
    db = DBSCAN(eps=0.3, min_samples=10).fit(self.X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    print('Estimated number of clusters: %d' % n_clusters_)
    print('Estimated number of noise points: %d' % n_noise_)
    # #############################################################################
    # Plot result
    import matplotlib.pyplot as plt

    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

        class_member_mask = (labels == k)

        xy = self.X[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                markeredgecolor='k', markersize=14)

        xy = self.X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                markeredgecolor='k', markersize=6)
    plt.title('DBSCAN')

    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

class GaussianProcessClassifierSA(Algorithm):
  def grafica(self):
    n_features = self.X.shape[1]
    C = 10
    kernel = 1.0 * RBF([1.0, 1.0])  # for GPC

    # Create different classifiers.
    classifiers = {
        'GPC': GaussianProcessClassifier(kernel)
    }

    n_classifiers = len(classifiers)

    plt.figure(figsize=(3 * 2, n_classifiers * 2))
    plt.subplots_adjust(bottom=.2, top=.95)

    xx = np.linspace(3, 9, 100)
    yy = np.linspace(1, 5, 100).T
    xx, yy = np.meshgrid(xx, yy)
    Xfull = np.c_[xx.ravel(), yy.ravel()]

    start_time = time()
    with parallel_backend('threading', n_jobs=n_jobs_parrallel):
      for index, (name, classifier) in enumerate(classifiers.items()):
          classifier.fit(self.X, self.Y)

          y_pred = classifier.predict(self.X)
          accuracy = accuracy_score(self.Y, y_pred)
          print("Accuracy (train) for %s: %0.1f%% " % (name, accuracy * 100))

          # View probabilities:
          probas = classifier.predict_proba(Xfull)
          n_classes = np.unique(y_pred).size
          for k in range(n_classes):
              plt.subplot(n_classifiers, n_classes, index * n_classes + k + 1)
              plt.title("Class %d" % k)
              if k == 0:
                  plt.ylabel(name)
              imshow_handle = plt.imshow(probas[:, k].reshape((100, 100)),
                                        extent=(3, 9, 1, 5), origin='lower')
              plt.xticks(())
              plt.yticks(())
              idx = (y_pred == k)
              if idx.any():
                  plt.scatter(self.X[idx, 0], self.X[idx, 1], marker='o', c='w', edgecolor='k')

    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'

    ax = plt.axes([0.15, 0.04, 0.7, 0.05])
    plt.title("Clasificador Gausian \n" + salida)
    plt.colorbar(imshow_handle, cax=ax, orientation='horizontal')

    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

class DBSCANSA(Algorithm):
  def grafica(self):
    import numpy as np
    from sklearn.cluster import DBSCAN
    from sklearn import metrics
    from sklearn.datasets import make_blobs
    from sklearn.preprocessing import StandardScaler

    # #############################################################################
    # Compute DBSCAN
    db = DBSCAN(eps=0.3, min_samples=10).fit(self.X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    print('Estimated number of clusters: %d' % n_clusters_)
    print('Estimated number of noise points: %d' % n_noise_)
    # #############################################################################
    # Plot result
    import matplotlib.pyplot as plt

    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]
    start_time = time()
    with parallel_backend('threading', n_jobs=n_jobs_parrallel):
      for k, col in zip(unique_labels, colors):
          if k == -1:
              # Black used for noise.
              col = [0, 0, 0, 1]

          class_member_mask = (labels == k)

          xy = self.X[class_member_mask & core_samples_mask]
          plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                  markeredgecolor='k', markersize=14)

          xy = self.X[class_member_mask & ~core_samples_mask]
          plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                  markeredgecolor='k', markersize=6)
    elapsed_time = time() - start_time
    elapsed_time = format(elapsed_time, '.6f')
    salida = 'Tiempo ejecución:' + str(elapsed_time) + ' segundos'

    plt.title('Estimated number of clusters:' +  str(n_clusters_) + "\n" + salida)
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()