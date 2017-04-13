#------TOTAL USUARIOS------- 
archivo=open("foursquare_checkins.csv")
archivo_listado=archivo.readlines()[1:]
lista_usuarios_repetidos=[]  
for e in archivo_listado:
	usuario_a_agregar=e.split(",")[0]
	lista_usuarios_repetidos.append(usuario_a_agregar)
#Eliminar duplicados.
lista_usuarios=sorted(list(set(lista_usuarios_repetidos)))
total_usuarios=len(lista_usuarios)
print("Total usuarios:",total_usuarios)


#------TOTAL UBICACIONES-------
archivo=open("foursquare_checkins.csv")
archivo_listado=archivo.readlines()[1:]
lista_ubicaciones_repetidas=[]
for e in archivo_listado:
	ubicacion_a_agregar=e.split(",")[4]
	lista_ubicaciones_repetidas.append(ubicacion_a_agregar)
#Eliminar duplicados.
lista_ubicaciones=sorted(list(set(lista_ubicaciones_repetidas)))
total_ubicaciones=len(lista_ubicaciones)
print("Total ubicaciones:",total_ubicaciones)


#------TOTAL CHECK-INS-------
archivo=open("foursquare_checkins.csv")
archivo_listado=archivo.readlines()[1:]
total_checkins=len(archivo_listado)
print("Total check-ins:",total_checkins)


#------PROMEDIO AMIGOS POR USUARIO-------
archivo_amistades=open("foursquare_friendship.csv")
total_amistades=len(archivo_amistades.readlines()[1:])
promedio_amigos_por_usuario=total_amistades/total_usuarios
print("Promedio de amigos por usuario:", promedio_amigos_por_usuario)

#------PROMEDIO DE CHECK-INS POR USUARIO-------
promedio_checkins_por_usuario=total_checkins/total_usuarios
print("Promedio de check-ins por usuario:", promedio_checkins_por_usuario)

#------PROMEDIO DE CHECK-INS POR LUGAR-------
promedio_checkins_por_lugar=total_checkins/total_ubicaciones
print("Promedio de check-ins por lugar:", promedio_checkins_por_lugar)
