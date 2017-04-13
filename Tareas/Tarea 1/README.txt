1. Por favor usar Brackets para corregir, ya que sino no permite acceder al JSON 
por alguna razón que desconozco.

2. El archivo principal HTML para acceder a la página es el home.html, 
los archivos tab1.html y tab2.html son interiores a la pagina.

3. Cambié las siguientes palabras del archivo input3.json 
para que funcionara correctamente:
- "chack-ins" -> "checkins"
- "check-ins" -> "checkins"

4. Hay que agregar los archivos "foursquare_checkins.csv" y "foursquare_friendship.csv" 
a la carpeta del repositorio, para que funcionen los archivos python.

5. Para leer el archivo JSON usé JQuery con el archivo local "input3.json".

6. El archivo python "muestreo_500_random.py" accede al archivo "foursquare_checkins.csv" 
y crea un archivo "500_random.js" que contiene una lista con 500 coordenadas aleatoriamente
escogidas de tal archivo. Luego el archivo "tab1.html" accede ese archivo "500_random.html"
y los muestra en el mapa.

7. El archivo python "resumen_del_dataset.py" accede a los archivos "foursquare_checkins.csv" 
y "foursquare_friendship.csv" para entregar los datos generales del dataset.

8. Para las rutas dinámicas, se debe esperar a que se termine de mostrar la ruta para realizar
una nueva búsqueda. Es por esto que al pedir las rutas dinámicas se ocultan los botones. 
(Esto para evitar errores de visualización de las rutas, o superposicion de ellas).

9. Para obtener rutas dinamicas entre 2 fechas, el checkbox de rutas dinamicas debe estar
activado, dos fechas seleccionadas y se debe hacer click al boton "Filtrar".

10. Para visualizar las imágenes al hacer click sobre los marcadores hice referencia a 
links de imagenes de Google Street View. La mayoría de los lugares tienen fotos en 
Google Street View y en dichos marcadores se muestran imágenes reales de dichos lugares
(ver: imagen_disponible.jpg), pero hay algunos que no tienen, es por esta razón que algunos
marcadores muestran una imagen gris con la frase "Sorry, we have no imagery here."
(ver: imagen_no_disponible.jpg).



