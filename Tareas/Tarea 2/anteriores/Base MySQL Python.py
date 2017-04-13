import mysql.connector
from textblob import TextBlob
from statistics import pstdev

cnx = mysql.connector.connect(user='root', password="1305", database='iic1005')
cursor = cnx.cursor()

query = ("SELECT * FROM feed limit 1000")

cursor.execute(query)
comments=[]
for x in cursor:
  if x[1]=='sheyenne.rhiadra':
    if x[4]!="":
      comments.append(str(x[4]))

suma=0
data=[]
for c in comments:
  a=0
  blob = TextBlob(c)
  for sentence in blob.sentences:
    a+=sentence.sentiment.subjectivity
  sub_c=a/len(blob.sentences)
  data.append(sub_c)
  suma+=sub_c

print(suma/len(comments))
print("desv",pstdev(data))


cursor.close()
cnx.close()
