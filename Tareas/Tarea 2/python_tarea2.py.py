#PARTE 1

import mysql.connector
import datetime
from textblob import TextBlob
from statistics import pstdev
print("El programa se demora aproximadamente 1 minuto 10 segundos en funcionar.")
print("COMIENZO:", datetime.datetime.time(datetime.datetime.now()))

cnx = mysql.connector.connect(user='root', password="1305", database='iic1005')
cursor = cnx.cursor()

query = ("SELECT id, avatar FROM about")
cursor.execute(query)
lista_ids_usuarios = []
lista_general=[]
for avatar in cursor:
  lista_ids_usuarios.append(avatar[0])
  usuario = str(avatar[1])
  datos_usuario = [usuario,0,0,0,0,[],0,0,[],0,0,0,0,0,0,[],[],0,0,0,0,0,0,0,0,0,0,0]
#[usuario(0), c_loves(1), c_comments(2), c_wallposts(3), c_snapshots(4),
#[todos los status en feed](5), prom_subj_status(6), desv_subj_status(7),
#[todos los comments en feed](8), prom_subj_comments(9), desv_subj_comments(10),
#prom_pol_status(11), desv_pol_status(12), prom_pol_comments(13), desv_pol_comments(14),
#[textos de reviews hechos](15), [textos de comments hechos en store](16),
#prom_sub_reviews(17), desv_sub_reviews(18), prom_pol_reviews(19), desv_pol_reviews(20),
#prom_sub_comments(21), desv_sub_comments(22),prom_pol_comments(23), desv_pol_comments(24)
#total_in_degree(25),total_out_degree(26),vendedor_1 comprador_0 (27)]
  lista_general.append(datos_usuario)
total_usuarios = len(lista_general)
print("1. NUMERO DE USUARIOS:",total_usuarios)
      
tiendas=[]
query = ("SELECT store_id FROM stores")
cursor.execute(query)
for tienda in cursor:
    if tienda not in tiendas:
        tiendas.append(tienda)
print("2. NUMERO DE TIENDAS:",len(tiendas))

categorias=[]
query = ("SELECT category FROM categories")
cursor.execute(query)
for categoria in cursor:
    if categoria not in categorias:
        categorias.append(categoria)
print("3. NUMERO DE CATEGORIAS DE PRODUCTOS:",len(categorias))

products_ids = []
query = ("SELECT product_id FROM products")
cursor.execute(query)
for product in cursor:
  products_ids.append(int(product[0]))
total_products = len(products_ids)
query = ("SELECT id, comments FROM reviews")
cursor.execute(query)
total_reviews = 0
total_comments = 0
for x in cursor:
  if int(x[0]) in products_ids:
    total_reviews += 1
    total_comments += int(x[1])
promRP = total_reviews/total_products
promCP = total_comments/total_products
print("4.1 PROMEDIO DE REVIEWS POR PRODUCTO:",promRP)
print("4.2 PROMEDIO DE COMMENTS POR PRODUCTO:",promCP)
print("Paciencia, el siguiente print se demora aproximadamente 50 segundos...")

loves=0
comments2=0
wallposts=0
snapshots=0
query = ("SELECT * FROM feed")
cursor.execute(query)
for feed in cursor:
  #IN_DEGREE OUT_DEGREE
  source = str(feed[1])
  destination = str(feed[2])
  if feed[3]=="LOVE":
    loves+=1
  if feed[3]=="COMMENT":
    comments2+=1
  if feed[3]=="WALLPOST":
    wallposts+=1
  if feed[3]=="SNAPSHOT":
    snapshots+=1
  feeder = str(feed[1])
  feed_text = str(feed[4])
  for datos in lista_general:
    usuario = datos[0]
    if source != destination:
      if usuario == source:
        datos[26] += 1
      if usuario == destination:
        datos[25] += 1
    if usuario == feeder:
      if feed[3]=="LOVE":
        datos[1]+=1
      elif feed[3]=="COMMENT":
        datos[2]+=1
        if feed_text!="":
          datos[8].append(feed_text) #Aqui solo se consideran los textos de los comments.
      elif feed[3]=="WALLPOST":
        datos[3]+=1
      elif feed[3]=="SNAPSHOT":
        datos[4]+=1
      if feed_text!="":
        datos[5].append(feed_text) #Consideramos 'status' como cualquier texto de un love, comment, wallpost o snapshot.
LpU=loves/total_usuarios
CpU=comments2/total_usuarios
WpU=wallposts/total_usuarios
SpU=snapshots/total_usuarios
print("4.3 NUMERO PROMEDIO DE LOVES POR USUARIO:",(LpU))
print("4.4 NUMERO PROMEDIO DE COMMENTS POR USUARIO:",(CpU))
print("4.5 NUMERO PROMEDIO DE WALLPOSTS POR USUARIO:",(WpU))
print("4.6 NUMERO PROMEDIO DE SNAPSHOTS POR USUARIO:",(SpU))

print("Paciencia, escribiendo archivo .txt de los datos de los usuarios en aproximadamente 10 segundos...")
for datos in lista_general:
  subj_sumada_status = 0
  pol_sumada_status = 0
  total_feed_texts_usuario = len(datos[5])
  valores_sub_ft=[]
  valores_pol_ft=[]
  if total_feed_texts_usuario != 0:
    for ft in datos[5]:
      suma_parcial_s = 0
      suma_parcial_p = 0
      #Calculamos la subjectivity y polarity de cada status
      blob = TextBlob(ft)
      n_oraciones = len(blob.sentences)
      for sentence in blob.sentences:
        suma_parcial_s += sentence.sentiment.subjectivity
        suma_parcial_p += sentence.sentiment.polarity
      subj_feed_text = suma_parcial_s/n_oraciones
      pol_feed_text = suma_parcial_p/n_oraciones
      valores_sub_ft.append(subj_feed_text)
      subj_sumada_status += subj_feed_text
      valores_pol_ft.append(pol_feed_text)
      pol_sumada_status += pol_feed_text
    subj_promedio_status = subj_sumada_status/total_feed_texts_usuario
    datos[6] = round(subj_promedio_status,3)
    desv_sub_ft = pstdev(valores_sub_ft)
    datos[9] = round(desv_sub_ft,3)
    pol_promedio_status = pol_sumada_status/total_feed_texts_usuario
    datos[11] = round(pol_promedio_status,3)
    desv_pol_ft = pstdev(valores_pol_ft)
    datos[13] = round(desv_pol_ft,3)

  subj_sumada_comments = 0
  pol_sumada_comments = 0
  total_comments_usuario =len(datos[8])
  valores_sub_com=[]
  valores_pol_com=[]
  if total_comments_usuario != 0:
    for comment in datos[8]:
      suma_parcial2_s = 0
      suma_parcial2_p = 0
      #Calculamos la subjectivity y polarity de cada comment
      blob = TextBlob(comment)
      n_oraciones2 = len(blob.sentences)
      for sentence in blob.sentences:
        suma_parcial2_s += sentence.sentiment.subjectivity
        suma_parcial2_p += sentence.sentiment.subjectivity
      subj_comment = suma_parcial2_s/n_oraciones2
      pol_comment = suma_parcial2_p/n_oraciones2
      valores_sub_com.append(subj_comment)
      valores_pol_com.append(pol_comment)
      subj_sumada_comments += subj_comment
      pol_sumada_comments += pol_comment
    subj_promedio_comments = subj_sumada_comments/total_comments_usuario
    datos[7] = round(subj_promedio_comments,3)
    desv_sub_com=pstdev(valores_sub_com)
    datos[10] = round(desv_sub_com,3)
    pol_promedio_comments = pol_sumada_comments/total_comments_usuario
    datos[12] = round(pol_promedio_comments,3)
    desv_pol_com=pstdev(valores_pol_com)
    datos[14] = round(desv_pol_com,3)

query = ("SELECT name, review FROM reviews")
cursor.execute(query)
for review in cursor:
  avatar = str(review[0])
  for datos in lista_general:
    if datos[0]==avatar:
      datos[15].append(str(review[1]))
query = ("SELECT name, comment FROM comments")
cursor.execute(query)
for comment in cursor:
  avatar = str(comment[0])
  for datos in lista_general:
    if datos[0]==avatar:
      datos[16].append(str(comment[1]))
for datos in lista_general:
  n_review = len(datos[15])
  subj_sumada_reviews = 0
  pol_sumada_reviews = 0
  valores_sub_r=[]
  valores_pol_r=[]
  for review_text in datos[15]:
    if n_review != 0:
      suma_parcial_sr = 0
      suma_parcial_pr = 0
      #Calculamos la subjectivity y polarity de cada review
      blob = TextBlob(review_text)
      n_oraciones = len(blob.sentences)
      for sentence in blob.sentences:
        suma_parcial_sr += sentence.sentiment.subjectivity
        suma_parcial_pr += sentence.sentiment.polarity
      subj_review = suma_parcial_sr/n_oraciones
      pol_review = suma_parcial_pr/n_oraciones
      valores_sub_r.append(subj_review)
      subj_sumada_reviews += subj_review
      valores_pol_r.append(pol_review)
      pol_sumada_reviews += pol_review
    subj_promedio_r = subj_sumada_reviews/n_review
    datos[17] = round(subj_promedio_r,3)
    desv_sub_review = pstdev(valores_sub_r)
    datos[19] = round(desv_sub_review,3)
    pol_promedio_r = pol_sumada_reviews/n_review
    datos[21] = round(pol_promedio_r,3)
    desv_pol_review = pstdev(valores_pol_r)
    datos[23] = round(desv_pol_review,3)

  n_com = len(datos[16])
  subj_sumada_com = 0
  pol_sumada_com = 0
  valores_sub_com=[]
  valores_pol_com=[]
  for comment_text in datos[16]:
    if n_com != 0:
      suma_parcial_sc = 0
      suma_parcial_pc = 0
      #Calculamos la subjectivity y polarity de cada review
      blob = TextBlob(comment_text)
      n_oraciones = len(blob.sentences)
      for sentence in blob.sentences:
        suma_parcial_sc += sentence.sentiment.subjectivity
        suma_parcial_pc += sentence.sentiment.polarity
      subj_com = suma_parcial_sc/n_oraciones
      pol_com = suma_parcial_pc/n_oraciones
      valores_sub_com.append(subj_com)
      subj_sumada_com += subj_com
      valores_pol_com.append(pol_com)
      pol_sumada_com += pol_com
    subj_promedio_com = subj_sumada_com/n_com
    datos[18] = round(subj_promedio_com,3)
    desv_sub_com = pstdev(valores_sub_com)
    datos[20] = round(desv_sub_com,3)
    pol_promedio_com = pol_sumada_com/n_com
    datos[22] = round(pol_promedio_com,3)
    desv_pol_com = pstdev(valores_pol_com)
    datos[24] = round(desv_pol_com,3)

query = ("SELECT name FROM sellers")
cursor.execute(query)
for name in cursor:
  nombre = str(name[0])
  for datos in lista_general:
    avatar = datos[0]
    if avatar == nombre:
      datos[27] = 1

cursor.close()
cnx.close()
      
archivo = open("usuarios.txt","w")
for d in range(4000):
  lista_general[d][0] = lista_ids_usuarios[d]
for datos in lista_general:
  del datos[5] #borramos la lista de textos de status que no interesan
  del datos[7] #borramos la lista de textos de comments que no interesan
  del datos[13] #borramos la lista de textos de reviews en el store que no interesan
  del datos[13] #borramos la lista de textos de comments en el store que no interesan
  for k in range(0,24):
    archivo.write(str(datos[k]))
    if (k < 23):
      archivo.write("/")
  archivo.write("\n")
archivo.close()
print("Archivo usuarios.txt creado.")
print("FINAL:", datetime.datetime.time(datetime.datetime.now()))


#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------
#PARTE 2

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
print (predicted)

print("Para cada usuario las probabilidades predichas de ser comprador o vendedor se ven respectivamente en la lista:")
probs = model2.predict_proba(X_test)
print (probs)

auc = (metrics.roc_auc_score(y_test, probs[:, 1]))
print("La metrica AUC obtenida para el modelo es: " + str(auc))

print("Las metricas Precision, Recall y F1 se pueden ver a continuacion para cada prediccion (0=comprador 1=vendedor):")
print (metrics.classification_report(y_test, predicted))

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
print (predicted)

print("Para cada usuario las probabilidades predichas de ser comprador o vendedor se ven respectivamente en la lista:")
probs = model2.predict_proba(X_test)
print (probs)

auc = (metrics.roc_auc_score(y_test, probs[:, 1]))
print("La metrica AUC obtenida para el modelo es: " + str(auc))

print("Las metricas Precision, Recall y F1 se pueden ver a continuacion para cada prediccion (0=comprador 1=vendedor):")
print (metrics.classification_report(y_test, predicted))

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
print (predicted)

print("Para cada usuario las probabilidades predichas de ser comprador o vendedor se ven respectivamente en la lista:")
probs = model2.predict_proba(X_test)
print (probs)

auc = (metrics.roc_auc_score(y_test, probs[:, 1]))
print("La metrica AUC obtenida para el modelo es: " + str(auc))

print("Las metricas Precision, Recall y F1 se pueden ver a continuacion para cada prediccion (0=comprador 1=vendedor):")
print (metrics.classification_report(y_test, predicted))

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
print (predicted)

print("Para cada usuario las probabilidades predichas de ser comprador o vendedor se ven respectivamente en la lista:")
probs = model2.predict_proba(X_test)
print (probs)

auc = (metrics.roc_auc_score(y_test, probs[:, 1]))
print("La metrica AUC obtenida para el modelo es: " + str(auc))

print("Las metricas Precision, Recall y F1 se pueden ver a continuacion para cada prediccion (0=comprador 1=vendedor):")
print (metrics.classification_report(y_test, predicted))

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
