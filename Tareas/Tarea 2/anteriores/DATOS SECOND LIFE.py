import mysql.connector

cnx = mysql.connector.connect(user='root', password="1305", database='iic1005')
cursor = cnx.cursor()

usuarios=0
query = ("SELECT avatar FROM about")
cursor.execute(query)
for usuario in cursor:
  usuarios+=1
print("1. NUMERO DE USUARIOS:",usuarios)

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

query = ("SELECT id, comments FROM reviews")
cursor.execute(query)
total_reviews = 0
total_comments = 0
for x in cursor:
  total_reviews += 1
  total_comments += int(x[1])
query = ("SELECT product_id FROM products")
cursor.execute(query)
total_products = 0
for product in cursor:
  total_products += 1
promRP = total_reviews/total_products
promCP = total_comments/total_products
print("4.1 PROMEDIO DE REVIEWS POR PRODUCTO:",promRP)
print("4.2 PROMEDIO DE COMMENTS POR PRODUCTO:",promCP)

loves=0
comments2=0
wallposts=0
snapshots=0
query = ("SELECT * FROM feed")
cursor.execute(query)
for feed in cursor:
  if feed[3]=="LOVE":
    loves+=1
  if feed[3]=="COMMENT":
    comments2+=1
  if feed[3]=="WALLPOST":
    wallposts+=1
  if feed[3]=="SNAPSHOT":
    snapshots+=1
LpU=loves/usuarios
CpU=comments2/usuarios
WpU=wallposts/usuarios
SpU=snapshots/usuarios
print("4.3 NUMERO PROMEDIO DE LOVES POR USUARIO:",(LpU))
print("4.4 NUMERO PROMEDIO DE COMMENTS POR USUARIO:",(CpU))
print("4.5 NUMERO PROMEDIO DE WALLPOSTS POR USUARIO:",(WpU))
print("4.6 NUMERO PROMEDIO DE SNAPSHOTS POR USUARIO:",(SpU))

cursor.close()
cnx.close()
