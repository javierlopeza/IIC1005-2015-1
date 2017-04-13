#------MUESTREO 500 RANDOM-------
from random import * 
archivo=open("foursquare_checkins.csv")
archivo_listado=archivo.readlines()[1:]
lista_500=[]
total_checkins=len(archivo_listado)
n_aleatorios=[]
while len(n_aleatorios)<500:
	nR=randint(0,total_checkins)
	if not(nR in n_aleatorios):
		n_aleatorios.append(nR)
	n_aleatorios=sorted(n_aleatorios)
for ln in n_aleatorios:
	checkin=archivo_listado[ln].split(",")
	lat = checkin[1]
	lon = checkin[2]
	lista_500.append([lat,lon])
texto_js = "var random_500 = "+ str(lista_500)
archivo_js = open("500_random.js", "w")
archivo_js.write(texto_js)
archivo_js.close()


