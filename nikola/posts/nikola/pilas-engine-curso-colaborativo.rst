.. title: pilas-engine: curso colaborativo
.. slug: pilas-engine-curso-colaborativo
.. date: 2016-01-31 03:28:12 UTC-03:00
.. tags: python, pilas-engine, software, código, flask, redis, websocket
.. category: 
.. link: 
.. description: 
.. type: text

En Santa Cruz, Bolivia empecé a pensar en una idea de hacer un
curso/workshop de `pilas-engine <http://pilas-engine.com.ar/>`_
colaborativo. Sí, una especie de taller como los de Django Girls que
venimos haciendo, pero en el que desarrollemos un juego entre todos.

Lo que me gustaría trabajar acá es el concepto de auto-aprendizaje,
trabajo en equipo y organización de un proyecto. La idea para lograr
esto sería realizar un taller de un día entero de duración donde
empezamos presentando pilas-engine y sus conceptos básicos, hablamos
un poco de `Trello <http://trello.com/>`_ para gestionar las tareas
que discutiremos entre todos y finalmente `github
<http://github.com/>`_ para compartir nuestro código con los demás.

Los asistentes trabajarían en pequeños grupos (estratégicamente
seleccionados) en las tareas que les correspondan, teniendo en cuenta
que todos estamos haciendo *el mismo* juego y no que cada grupo está
haciendo el suyo. Lo importante de esto es que luego debemos juntar el
código de todos los grupos y poder jugar todos juntos (de modo
multijugador) al mismo juego que escribimos entre todos.

Como todo, esa es la idea inicial, luego habrá que ir puliéndola para
que quede algo realmente *hacible*.

Entonces, lo primero que me puse a investigar era qué juego podíamos
implementar entre todos. De nuevo, teniendo en mente que debemos
programarlo en un sólo día. Ahí encontré `Circle Game
<http://sysach.com/circle-game/>`_, que cumple con casi todas mis
necesidades.

.. figure:: circle-game.thumbnail.jpg
   :target: circle-game.jpg

   Circle Game

Este juego es una versión circular de *la viborita*, en donde uno es
un círculo y solo puede comer círculos más pequeños que uno
mismo. Cada vez que come un círculo, crece un poquito más. Si un
círculo más grande te toca, perdiste.

.. TEASER_END

El problema es que necesitaba una forma de hacer que eso sea
multijugador y que todos puedan jugar sin depender de la máquina que
tengan o incluso de que tengan computadora. Es probable que haya
personas que asistan sin computadoras y trabajen juntos con
otros. Creo que hasta 1 computadora por grupo de 3 personas sería
suficiente, e incluso, interesante para poner en práctica.

Empecé a pensar que deberían poder jugar con su tablet, smartphone o
computadora. ¿Qué tienen todas esas cosas en común? ¡Un browser! La
solución tenía que venir por ese lado entonces.

Empecé a buscar cosas y caí en este artículo sobre `Touch Events en
Javascript
<http://www.javascriptkit.com/javatutors/touchevents.shtml>`_. Luego
para conectar esos eventos con algún servidor pequeño en `Flask
<http://flask.pocoo.org/>`_ pensé en utilizar WebSockets y llegué a
`jquery-websockets
<https://code.google.com/archive/p/jquery-websocket/>`_.

Lo único que me faltaba era comunicar nuestro servidor de Flask que
estaba recibiendo toda la información de la posición del jugador con
el jugador en sí que iba a estar siendo renderizado por
pilas-engine. Y aquí es donde más problemas tuve y creo que la
solución que encontré no es del todo buena -*aunque funciona*: `Redis
<redis.io/>`_. Básicamente tengo una cola donde el server Flask carga
los datos de las posiciones y el método `actualizar(self)`, del actor
que quiero mover desde pilas-engine, va tomando los valores en orden
cada vez que se llama.

De esa forma logré mover el Mono que está en la pantalla de
pilas-engine utilizando un teléfono SmartPhone sin grandes
prestaciones con un browser cualquiera.

.. media:: https://www.youtube.com/watch?v=CayxmTLefF8

El código que realiza toda esta magia está en un repositorio de
GitHub: `humitos/ballsgame <https://github.com/humitos/ballsgame>`_.

Ahora me queda probarlo un poco más, ver como se comporta con 10~15
usuarios e ir pensando en cambiar Redis por algo que haga esa
comunicación de una forma mas rápida. ¿Tienen alguna sugerencia?
