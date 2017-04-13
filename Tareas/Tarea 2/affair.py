# -*- coding: utf-8 -*-
"""
Created on Tue May 12 18:44:44 2015

@author: Javier
"""

import numpy as np
import pylab as pl
from scipy import interp
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn import svm
from sklearn.utils import shuffle
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import StratifiedKFold

archivo=open('usuarios.txt','r')
data =  np.loadtxt(fname = "usuarios.txt", delimiter = '/')

print("PARA C1")
X = data[:, 5:12]
y = data[:, 23]

model = LogisticRegression()
model = model.fit(X, y)

print("Evaluamos el modelo creado dividiendolo en 70% para entrenamiento y 30% para testeo.")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model2 = LogisticRegression()
model2.fit(X_train, y_train)

print("Algunas predicciones hechas para los usuarios son (0=comprador 1=vendedor):")
predicted = model2.predict(X_test)
print predicted

print("Para cada usuario las probabilidades predichas de ser comprador o vendedor se ven respectivamente en la lista:")
probs = model2.predict_proba(X_test)
print probs

auc = (metrics.roc_auc_score(y_test, probs[:, 1]))
print("La metrica AUC obtenida para el modelo es: " + str(auc))

print("Las metricas Precision, Recall y F1 se pueden ver a continuacion para cada prediccion (0=comprador 1=vendedor):")
print metrics.classification_report(y_test, predicted)

print("Evaluando el modelo usando k-fold cross validation con k = 5 se obtienen:")
scores = cross_val_score(LogisticRegression(), X, y, scoring='precision', cv=5)
print ("Average Precision: " + str(scores.mean()))
scores2 = cross_val_score(LogisticRegression(), X, y, scoring='recall', cv=5)
print ("Average Recall: " + str(scores2.mean()))
scores3 = cross_val_score(LogisticRegression(), X, y, scoring='f1', cv=5)
print ("Average F1: " + str(scores3.mean()))
scores4 = cross_val_score(LogisticRegression(), X, y, scoring='roc_auc', cv=5)
print ("Average AUC: " + str(scores4.mean()))

classifier = svm.SVC(kernel='linear', probability=True)
probas_ = classifier.fit(X_train, y_train).predict_proba(X_test)

fpr, tpr, thresholds = metrics.roc_curve(y_test, probas_[:, 1])

pl.clf()
pl.plot(fpr, tpr, label='Curva ROC')
pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Curva ROC')
pl.legend(loc="lower right")
pl.show()

print("---------------------------------------------")

print("PARA C2")
X = data[:, 13:20]
y = data[:, 23]

model = LogisticRegression()
model = model.fit(X, y)

print("Evaluamos el modelo creado dividiendolo en 70% para entrenamiento y 30% para testeo.")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model2 = LogisticRegression()
model2.fit(X_train, y_train)

print("Algunas predicciones hechas para los usuarios son (0=comprador 1=vendedor):")
predicted = model2.predict(X_test)
print predicted

print("Para cada usuario las probabilidades predichas de ser comprador o vendedor se ven respectivamente en la lista:")
probs = model2.predict_proba(X_test)
print probs

auc = (metrics.roc_auc_score(y_test, probs[:, 1]))
print("La metrica AUC obtenida para el modelo es: " + str(auc))

print("Las metricas Precision, Recall y F1 se pueden ver a continuacion para cada prediccion (0=comprador 1=vendedor):")
print metrics.classification_report(y_test, predicted)

print("Evaluando el modelo usando k-fold cross validation con k = 5 se obtienen:")
scores = cross_val_score(LogisticRegression(), X, y, scoring='precision', cv=5)
print ("Average Precision: " + str(scores.mean()))
scores2 = cross_val_score(LogisticRegression(), X, y, scoring='recall', cv=5)
print ("Average Recall: " + str(scores2.mean()))
scores3 = cross_val_score(LogisticRegression(), X, y, scoring='f1', cv=5)
print ("Average F1: " + str(scores3.mean()))
scores4 = cross_val_score(LogisticRegression(), X, y, scoring='roc_auc', cv=5)
print ("Average AUC: " + str(scores4.mean()))

classifier = svm.SVC(kernel='linear', probability=True)
probas_ = classifier.fit(X_train, y_train).predict_proba(X_test)

fpr, tpr, thresholds = metrics.roc_curve(y_test, probas_[:, 1])

pl.clf()
pl.plot(fpr, tpr, label='Curva ROC')
pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Curva ROC')
pl.legend(loc="lower right")
pl.show()

print("---------------------------------------------")

print("PARA C3")
X = data[:, 21:22]
y = data[:, 23]

model = LogisticRegression()
model = model.fit(X, y)

print("Evaluamos el modelo creado dividiendolo en 70% para entrenamiento y 30% para testeo.")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model2 = LogisticRegression()
model2.fit(X_train, y_train)

print("Algunas predicciones hechas para los usuarios son (0=comprador 1=vendedor):")
predicted = model2.predict(X_test)
print predicted

print("Para cada usuario las probabilidades predichas de ser comprador o vendedor se ven respectivamente en la lista:")
probs = model2.predict_proba(X_test)
print probs

auc = (metrics.roc_auc_score(y_test, probs[:, 1]))
print("La metrica AUC obtenida para el modelo es: " + str(auc))

print("Las metricas Precision, Recall y F1 se pueden ver a continuacion para cada prediccion (0=comprador 1=vendedor):")
print metrics.classification_report(y_test, predicted)

print("Evaluando el modelo usando k-fold cross validation con k = 5 se obtienen:")
scores = cross_val_score(LogisticRegression(), X, y, scoring='precision', cv=5)
print ("Average Precision: " + str(scores.mean()))
scores2 = cross_val_score(LogisticRegression(), X, y, scoring='recall', cv=5)
print ("Average Recall: " + str(scores2.mean()))
scores3 = cross_val_score(LogisticRegression(), X, y, scoring='f1', cv=5)
print ("Average F1: " + str(scores3.mean()))
scores4 = cross_val_score(LogisticRegression(), X, y, scoring='roc_auc', cv=5)
print ("Average AUC: " + str(scores4.mean()))

classifier = svm.SVC(kernel='linear', probability=True)
probas_ = classifier.fit(X_train, y_train).predict_proba(X_test)

fpr, tpr, thresholds = metrics.roc_curve(y_test, probas_[:, 1])

pl.clf()
pl.plot(fpr, tpr, label='Curva ROC')
pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Curva ROC')
pl.legend(loc="lower right")
pl.show()

print("---------------------------------------------")

print("PARA C4")
X = data[:, 5:22]
y = data[:, 23]

model = LogisticRegression()
model = model.fit(X, y)

print("Evaluamos el modelo creado dividiendolo en 70% para entrenamiento y 30% para testeo.")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model2 = LogisticRegression()
model2.fit(X_train, y_train)

print("Algunas predicciones hechas para los usuarios son (0=comprador 1=vendedor):")
predicted = model2.predict(X_test)
print predicted

print("Para cada usuario las probabilidades predichas de ser comprador o vendedor se ven respectivamente en la lista:")
probs = model2.predict_proba(X_test)
print probs

auc = (metrics.roc_auc_score(y_test, probs[:, 1]))
print("La metrica AUC obtenida para el modelo es: " + str(auc))

print("Las metricas Precision, Recall y F1 se pueden ver a continuacion para cada prediccion (0=comprador 1=vendedor):")
print metrics.classification_report(y_test, predicted)

print("Evaluando el modelo usando k-fold cross validation con k = 5 se obtienen:")
scores = cross_val_score(LogisticRegression(), X, y, scoring='precision', cv=5)
print ("Average Precision: " + str(scores.mean()))
scores2 = cross_val_score(LogisticRegression(), X, y, scoring='recall', cv=5)
print ("Average Recall: " + str(scores2.mean()))
scores3 = cross_val_score(LogisticRegression(), X, y, scoring='f1', cv=5)
print ("Average F1: " + str(scores3.mean()))
scores4 = cross_val_score(LogisticRegression(), X, y, scoring='roc_auc', cv=5)
print ("Average AUC: " + str(scores4.mean()))

classifier = svm.SVC(kernel='linear', probability=True)
probas_ = classifier.fit(X_train, y_train).predict_proba(X_test)

fpr, tpr, thresholds = metrics.roc_curve(y_test, probas_[:, 1])

pl.clf()
pl.plot(fpr, tpr, label='Curva ROC')
pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Curva ROC')
pl.legend(loc="lower right")
pl.show()

print("---------------------------------------------")