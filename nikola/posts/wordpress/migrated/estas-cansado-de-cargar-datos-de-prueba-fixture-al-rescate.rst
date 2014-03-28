.. link:
.. description:
.. tags: busstopped, proyectos, python
.. date: 2011/03/12 18:36:15
.. title: ¿Estás cansado de cargar datos de prueba? Fixture al rescate
.. slug: estas-cansado-de-cargar-datos-de-prueba-fixture-al-rescate


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2011/03/12/estas-cansado-de-cargar-datos-de-prueba-fixture-al-rescate/


Entre ayer y hoy me puse a ver cómo crear Unittests para el proyecto
BusStopped que estoy haciendo bajo la plataforma GAE (Google App Engine)
utilizando Python como lenguaje.

Estuve probando y viendo varias formas de hacerlo. Primero, empecé a
hacerlo a lo *macho* sin ninguna librería de apoyo, importando el módulo
unittest de python y corriendo el script a mano como dice su
documentación.

Después instalé *nosetest* y tuve que toquetear un poco el **sys.path**
para que me encuentre los módulos necesarios y me empecé a ensuciar un
poco las manos hasta que lo saqué.

Igualmente había algo que no me gustaba, y era que la db que se usaba
era la misma que la del servidor de desarrollo entonces ya no me gustaba
mucho. De ahí me fui a probar
`gaeunit <http://code.google.com/p/gaeunit/>`__, que es una aplicación
de GAE que te escanea el directorio *test* y te ejecuta todos los tests
que hay ahí mostrándote los resultados en una página web. Además,
también funciona en el servidor de producción.

El problema con el que me encontré con este es que no es muy
configurable (tenés que modificar el código para cambiar el directorio a
escanear) y que además *no es compatible con TipFy*\ por decirlo de
alguna forma. Esto es porque las librerías externas que uso las meto en
una carpeta llamada **/lib** dentro de la app de GAE y TipFy las levanta
automáticamente.

Entonces, tuve que configurar el sys.path en el script de gaeunit.py
para que lea esas librerías también. Pero, después de esto me dí cuenta
que como *gaeunit*\ usa una DB independiente de la del servidor de
desarrollo, de alguna forma tenía que cargar los datos y... Ahí otra vez
empezó la complicación: GAE no tiene algo similar a los Fixture de
Django :(

Buscando un poco en Google me encontré con
`Fixture <http://farmdev.com/projects/fixture/index.html>`__ que es un
módulo de Python para cargar fixtures de diferentes formas en diferentes
proyectos y lo mejor de todo es que `tiene algo específico para Google
App
Engine <http://farmdev.com/projects/fixture/using-fixture-with-appengine.html#using-fixture-with-appengine>`__.
