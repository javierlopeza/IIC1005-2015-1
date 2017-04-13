import mysql.connector
from textblob import TextBlob

cnx = mysql.connector.connect(user='root', password="1305", database='iic1005')
cursor = cnx.cursor()

query = ("SELECT id, avatar FROM about limit 15")
cursor.execute(query)
for x in cursor:
  print(x)



cursor.close()
cnx.close()
