.. link:
.. description:
.. tags: python
.. date: 2007/08/30 21:36:51
.. title: Técnicas para hacer bucles
.. slug: tecnicas-para-hacer-bucles


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/08/30/tecnicas-para-hacer-bucles/


Siempre hice cualquier cosa al iterar sobre algo en Python. Y leyendo el
libro de Guido Van Rossum *"Guía de aprendizaje de Python"* encontré una
sección llamada como el título del post. Lo que pongo acá es un mail que
mandé a la lista de PyAr (Python Argentina); a la cual pertenezco ya
hace desde un año más o menos.

Todo esto es muy práctico para iterar sobre listas, diccionarios,
tuplas, etc. Para recorrer diccionarios y recuperar la clave y el valor
simultaneamente podemos hacer:

>>> en_es = {'shoot': 'disparar', 'hello': 'hola', 'back': 'volver'}
>>> for k, v in en_es.iteritems(): ... print "'%s' en castellano
significa '%s'" % (k,v) ... 'shoot' en castellano significa 'disparar'
'hello' en castellano significa 'hola' 'back' en castellano significa
'volver' >>>

Otra cosa que siempre he hecho bastante *feo*, es iterar sobre una
secuencia haciendo uso de la función range() para saber en qué posición
de la secuencia me encuentro y además saber que hay en la misma...

>>> for i, v in enumerate(["in", "cre", "i", "ble"]): ... print
"posicion numero %d = %s" % (i, v) ... posicion numero 0 = in posicion
numero 1 = cre posicion numero 2 = i posicion numero 3 = ble >>>

Podemos recorrer dos secuencias fácilmente haciendo:

>>> colores = ["amarillo", "naranja", "verde"] >>> frutas = ["banana",
"naranja", "manzana"] >>> for c, f in zip(colores,frutas): ... print "La
%s es de color %s" % (f,c) ... La banana es de color amarillo La naranja
es de color naranja La manzana es de color verde >>>

Saludos!
