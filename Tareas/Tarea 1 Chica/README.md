***
El programa crea el archivo de texto 'pronostico.txt' en 'home', 
pero ademas envia al mail 'javierlopez_iic1005@hotmail.com' el mismo pronostico del tiempo.
***

Para que el script se ejecute a las 7 de la mañana todos los días, se deben cumplir los siguientes puntos:

1. El programa 'pronostico.py' funciona junto con 'pywapi.py' por lo tanto 
ambos archivos deben estar ubicados en 'home'.

2. Luego, para automatizar el programa, se debe ingresar a la terminal.

3. Ejecutar el comando: crontab -e

4. Ingresar el texto: 0 7 * * * python pronostico.py

5. Guardar los cambios hechos en el cron.


