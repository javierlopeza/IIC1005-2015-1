1. El programa base dado 'No entiende' cuando se le da un objeto/clase con un '_' entre palabras, es decir,
sucede lo siguiente:

	1 ?- conversar.
	|: Ozai es un fire_bender.
	No entiendo.
	|: Ozai es un firebender.
	entiendo.

por lo que para que funcione bien se deben escribir las clases, subclases y objetos como palabras juntas.
Lo mismo sucede para las relaciones entre clases, el programa 'No entiende' si se le da la clase 'mas_fuerte',
por lo que la relacion se debe dar como 'masfuerte' para que lo entienda el programa, es decir, sucede lo siguiente:

	1 ?- conversar.
	|: Aang es un avatar.
	entiendo.
	|: Ozai es un firebender.
	entiendo.
	|: Los avatar son mas_fuerte que los firebender.
	No entiendo.
	|: Los avatar son masfuerte que los firebender.
	entiendo.
	|: Quien es masfuerte?.
	Aang es masfuerte que Ozai.

2. El archivo 'lenguaje_natural.pl' es el correspondiente a la parte 2 de la tarea, es decir,
solo entiende relaciones entre las clases (no contiene los bonus).
El archivo 'lenguaje_natural_transitividad.pl' es el correspondiente al bonus 1 de 'Transitividad'.
