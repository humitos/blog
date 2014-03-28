.. link:
.. description:
.. tags: olpc, python, software libre
.. date: 2012/03/28 20:55:32
.. title: ¡Otro parche más!
.. slug: otro-parche-mas


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2012/03/28/otro-parche-mas/


Como conté en un `post
anterior <http://humitos.wordpress.com/2012/03/26/mi-primer-commit-en-olpc/>`__,
metí un parche para la OLPC en la Actividad Terminal. Hoy, me acaban de
aceptar
`otro <http://git.sugarlabs.org/maze/mainline/commit/335ad73456ba3ec8f56811abddcaca4650199db1>`__,
pero en esta oportunidad en la `Actividad
Maze <http://activities.sugarlabs.org/en-US/sugar/addon/4071>`__, que es
un juego de laberinto dónde hay que llevar el personaje (que en este
caso es un círculo :P )  a la salida (que es un cuadrado) atravesando
todo el laberinto.

Es un juego muy sencillo, pero entretenido. Es como esos típicos que
vienen en las revistas para chicos que se empieza una línea en extremo y
hay que llegar al otro, generalmente en dónde el ratón tiene que comer
el queso o similar :D

Lo bueno de este parche es que es un poquito más complejo que el
anterior. Lo que hace es guardar el estado del juego (el nivel) en el
que el chico se encontraba antes de cerrar la Actividad y volver a
cargar ese nivel al momento de iniciarla nuevamente.

|image0|

Es realmente gratificante. Este proyecto (OLPC) es algo que me picó hace
bastante tiempo, y nunca había tenido la posibilidad de colaborar. Hay
muy buena gente y muy buena onda. Además, se aprende un montón. Estoy
muy contento.

El otro día *manuq* (Manuel Quiñones) me mostró un
`mapa <http://one.laptop.org/map>`__ y me dijo: "Es muy loco pensar que
todos esos niños están usando una porción de código que escribí yo". Y
tenía razón, esmuy loco.

*Además, ya mandé otro... y parece que me lo van a aceptar también :)*

.. |image0| image:: http://humitos.files.wordpress.com/2012/03/1237658064.png
   :target: http://humitos.files.wordpress.com/2012/03/1237658064.png
