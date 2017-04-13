import mysql.connector
import datetime
from textblob import TextBlob
from statistics import pstdev

print("COMIENZO:", datetime.datetime.now())

cnx = mysql.connector.connect(user='root', password="1305", database='iic1005')
cnx2 = mysql.connector.connect(user='root', password="1305", database='iic1005')

cursor = cnx.cursor()
cursor2 = cnx2.cursor()

query = ("SELECT avatar FROM about")
query2 = ("SELECT * FROM feed")
cursor.execute(query)
lista_general=[]



for avatar in cursor:
  usuario = str(avatar[0])
  datos_usuario = [usuario,0,0,0,0,[],0,0,[],0,0]
#[usuario(0), c_loves(1), c_comments(2), c_wallposts(3), c_snapshots(4), [todos los status en feed](5), prom_subj_status(6), desv_subj_status(7),[todos los comments en feed](8), prom_subj_comments(9), desv_subj_comments(10)]
  lista_general.append(datos_usuario)

cursor2.execute(query2)
for feed in cursor2:
  feeder = str(feed[1])
  feed_text = str(feed[4])
  for datos in lista_general:
    usuario = datos[0]
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

for datos in lista_general:
  subj_sumada_status = 0
  total_feed_texts_usuario = len(datos[5])
  valores_ft=[]
  if total_feed_texts_usuario != 0:
    for ft in datos[5]:
      suma_parcial = 0
      #Calculamos la subjectivity de cada status
      blob = TextBlob(ft)
      n_oraciones = len(blob.sentences)
      for sentence in blob.sentences:
        suma_parcial += sentence.sentiment.subjectivity
      subj_feed_text = suma_parcial/n_oraciones
      valores_ft.append(subj_feed_text)
      subj_sumada_status += subj_feed_text
    subj_promedio_status = subj_sumada_status/total_feed_texts_usuario
    datos[6] = subj_promedio_status
    desv_ft = pstdev(valores_ft)
    datos[7] = desv_ft

  subj_sumada_comments = 0  
  total_comments_usuario =len(datos[8])
  valores_com=[]  
  if total_comments_usuario != 0:
    for comment in datos[8]:
      suma_parcial2 = 0
      #Calculamos la subjectivity de cada comment
      blob = TextBlob(comment)
      n_oraciones2 = len(blob.sentences)
      for sentence in blob.sentences:
        suma_parcial2 += sentence.sentiment.subjectivity
      subj_comment = suma_parcial2/n_oraciones2
      valores_com.append(subj_comment)
      subj_sumada_comments += subj_comment
    subj_promedio_comments = subj_sumada_comments/total_comments_usuario
    datos[9] = subj_promedio_comments
    desv_com=pstdev(valores_com)
    datos[10] = desv_com
  

cursor.close()
cnx.close()

archivo = open("usuarios.txt","w")
archivo.write("AVATAR / N° LOVES / N° COMMENTS / N° WALLPOSTS / N° SNAPSHOTS / SUBJECTIVITY PROMEDIO STATUS / SUBJECTIVITY DESVIACIACION ESTANDAR STATUS / SUBJECTIVITY PROMEDIO COMMENTS / SUBJECTIVITY DESVIACION ESTANDAR COMMENTS\n")
for datos in lista_general:
  del datos[5] #borramos la lista de textos de status que no interesan
  del datos[7] #borramos la lista de textos de comments que no interesan
  for dato in datos:
    archivo.write(str(dato))
    archivo.write(" / ")
  archivo.write("\n")
archivo.close()

print("FINAL:", datetime.datetime.now())
