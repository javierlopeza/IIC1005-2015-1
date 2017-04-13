import mysql.connector
import datetime

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
  datos_usuario = [usuario,0,0,0,0]
  lista_general.append(datos_usuario)

cursor2.execute(query2)
for feed in cursor2:
  feeder = str(feed[1])
  for datos in lista_general:
    usuario = datos[0]
    if usuario == feeder:
      if feed[3]=="LOVE":
        datos[1]+=1
      elif feed[3]=="COMMENT":
        datos[2]+=1
      elif feed[3]=="WALLPOST":
        datos[3]+=1
      elif feed[3]=="SNAPSHOT":
        datos[4]+=1
        
cursor.close()
cnx.close()

archivo = open("usuarios.txt","w")
archivo.write("USUARIO / LOVES / COMMENTS / WALLPOSTS / SNAPSHOTS\n")
for datos in lista_general:
  for dato in datos:
    archivo.write(str(dato))
    archivo.write(" / ")
  archivo.write("\n")
archivo.close()

print("FINAL:", datetime.datetime.now())
