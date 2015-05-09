.. title: ¡Nos compramos un robot!
.. slug: nos-compramos-un-robot
.. date: 2015-04-13 15:11:04 UTC-03:00
.. tags: robótica, argentina en python, viaje, san bernardino, paraguay
.. category: 
.. link: 
.. description: 
.. type: text

Ya lo dije, el :doc:`PyDay Asunción
<pydayasuncion-un-exito-arrollador>` fue éxito y hoy sigue dando sus
frutos.

El Sábado pasado *participamos* (en realidad solo asistimos, porque no
ayudamos en mucho -nada, diría yo) al "`HACKÁra Asuka Guaraní
<https://twitter.com/JukyParaguay/status/586193877461262336>`_" para
hacer la traducción de Sugar al Guaraní. Esta idea se propuso en el
PyDay de Asunción, y semanas más tarde se llevó adelante:
¡Felicitaciones a todos por eso!

Ahí, en el PyDay Asunción yo le compré un robot "RoDi" a Gary Servin
(disertante en el PyDay) con la idea de armar algún curso
introductorio a la programación para chicos utilizando Python. Sin
embargo, no tenía ni idea de RoDi y no había tenido tiempo de probarlo
hasta hoy que me puse a jugar un poco.

El robot sale USD 40 (lo cuál es muy barato). Entonces, estaría bueno
ver de comprar 2 o 3 más para tener un promedio de 10 alumnos y que
trabajen en equipos de 2 o 3. ¿Cómo lo ven?

.. figure:: rodi.thumbnail.jpg
   :target: rodi.jpg

   El robot RoDi

.. TEASER_END

La dinámica es sencilla. Te conectás por WiFi a RoDi y le hacés GETs
HTTP a diferentes URLs para que haga diferentes cosas (este `firmware
<https://github.com/tchx84/rodi-web>`_ lo realizó Martín Abente -otro
crack y disertante del PyDay).

Todo bien con RoDi, con Gary y Martín, pero a mí me gusta Python y es
lo que quiero enseñar :) . Así que `me hice una API super sencilla
<https://github.com/humitos/rodi-py>`_ utilizando `requests
<https://pypi.python.org/pypi/requests/>`_ para empezar a
gestionar la idea loca de hacer un curso de Python + Robótica para
chicos y ver cómo me va. En principio sería un juego, una aventura más
que nada. Tengo algunas ideas en la cabeza, pero hay que meterle
fichas y hacerla más tangible...

.. code:: python

   >>> import rodi
   >>> robot = rodi.RoDi()
   >>> robot.blink(1000)
   >>> robot.move_forward()
   >>> robot.move_left()
   >>> robot.move_backward()
   >>> # easy, ha?
   ...

Y aquí un video de prueba:

.. media:: https://www.youtube.com/watch?v=jcyX-RvSIf0
