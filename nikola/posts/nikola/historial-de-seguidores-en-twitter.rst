.. title: Historial de seguidores en Twitter
.. slug: historial-de-seguidores-en-twitter
.. date: 2016-02-09 20:49:31 UTC-03:00
.. tags: perú, las lomas, twitter, python, script, argentina en python
.. category: 
.. link: 
.. description: 
.. type: text

Desde que empecé a usar Twitter de forma activa me llamó mucho la
atención cómo funciona, pero no técnicamente, sino más bien en lo
social. El alcance que tiene a poder ver el contenido de casi
cualquier persona y hacer re-tuits de personas a las que no seguís. De
hecho, gracias a ese *feature* hemos podido llegar a muchos más
lugares con el proyecto.

Si bien no he podido dedicarme mucho tiempo a escribir algunos scripts
que hagan este análisis por mí, comencé con algo simple: el historial
de seguidores.

¿Cómo es eso? La idea es poder saber quienes te siguen, quién es un
nuevo seguidor y quién te dejó de seguir. Claramente, los últimos son
los más importantes para evaluar: ¿porqué perdí a este seguidor? es la
pregunta del millón.

El problema se dividió -automáticamente, en dos partes. La primera:
obtener todos los seguidores de la cuenta `@argenpython
<https://twitter.com/argenpython>`_ de forma periódica. La segunda:
hacer diff de esos seguidores de forma incremental. ¿Qué quiero decir
con incremental? Que no necesito saber la diferencia entre el primer
reporte y el último, porque si en los reportes del medio alguien me
empezó a seguir y luego me dejó de seguir, también quiero saberlo.

.. TEASER_END

La obtención de los seguidores lo resolví con este pequeño script (en
un @daily de CRON):

.. code:: bash

   fades -d twitter -x twitter-follow --oauth argenpython > argenpython.followers_`date +"\%Y\%m\%d"`.txt

Para hacer la diferencia de todos esos seguidores recolectados
diariamente con el script anterior, *"escribí"* [#]_ un script en
Python:

.. listing:: listings/historial-de-seguidores-en-twitter/multiplediff.py python

Finalmente, para saber cuáles son los seguidores que *hemos perdido en
el camino* utilicé este comando de bash:

.. code:: bash

   python3 multiplediff.py | grep "^-b" | wc -l

Eso me arrojó 39 como resultado. Por lo tanto, como este script está
corriendo desde el 1 de Enero de 2016, puedo decir que *hemos perdido
39 seguidores* en este mes.

.. [#] dijo el más mentiroso del mundo, el código me lo pasó `Ariel
   Rossanigo <https://twitter.com/ArielRossanigo>`_ por Twitter,
   justamente. Yo solo le hice unas pequeñas y mínimas modificaciones.
