import mysql.connector
import datetime
from textblob import TextBlob

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
  datos_usuario = [usuario,0,0,0,0,[],0,[],0]
#[usuario(0), c_loves(1), c_comments(2), c_wallposts(3), c_snapshots(4), [todos los status en feed](5), prom_subj_status(6), [todos los comments en feed](7), prom_subj_comments(8)]
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
          datos[7].append(feed_text)
      elif feed[3]=="WALLPOST":
        datos[3]+=1
      elif feed[3]=="SNAPSHOT":
        datos[4]+=1
      if feed_text!="":
        datos[5].append(feed_text)

for datos in lista_general:
  subj_sumada_status = 0
  subj_sumada_comments = 0
  total_feed_texts_usuario = len(datos[5])
  total_comments_usuario =len(datos[7])
  if total_feed_texts_usuario != 0:
    for ft in datos[5]:
      suma_parcial = 0
      #Calculamos la subjectivity de cada status
      blob = TextBlob(ft)
      n_oraciones = len(blob.sentences)
      for sentence in blob.sentences:
        suma_parcial += sentence.sentiment.subjectivity
      subj_feed_text = suma_parcial/n_oraciones
      subj_sumada_status += subj_feed_text
  if total_comments_usuario != 0:
    for comment in datos[7]:
      suma_parcial2 = 0
      #Calculamos la subjectivity de cada comment
      blob = TextBlob(comment)
      n_oraciones2 = len(blob.sentences)
      for sentence in blob.sentences:
        suma_parcial2 += sentence.sentiment.subjectivity
      subj_comment = suma_parcial2/n_oraciones2
      subj_sumada_comments += subj_comment

      
    subj_promedio_status = subj_sumada_status/total_feed_texts_usuario
    subj_promedio_comments = subj_sumada_comments/total_comments_usuario
    datos[6] = subj_promedio_status
    datos[8] = subj_promedio_comments
  

cursor.close()
cnx.close()

archivo = open("usuarios.txt","w")
archivo.write("USUARIO / LOVES / COMMENTS / WALLPOSTS / SNAPSHOTS / SUBJECTIVITY PROMEDIO STATUS / SUBJECTIVITY PROMEDIO COMMENTS\n")
for datos in lista_general:
  del datos[5] #borramos la lista de textos de status que no interesan
  del datos[6] #borramos la lista de textos de comments que no interesan
  for dato in datos:
    archivo.write(str(dato))
    archivo.write(" / ")
  archivo.write("\n")
archivo.close()

print("FINAL:", datetime.datetime.now())
