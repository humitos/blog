.. title: pip cache
.. slug: pip-cache
.. date: 2015-01-19 18:21:58 UTC-03:00
.. tags: pip, python, cache, software libre, programación, argentina en python
.. link: 
.. description: 
.. type: text

Durante unos días estuve buscando algo similar a apt-cacher-ng_. Un
software que conocí cuando trabajaba en Santa Fe, que me servía para
hacer de proxy de paquetes `.deb`. Con esto me ahorraba de bajar cientos
de veces el mismo paquete para ser instalado en muchas máquinas.

Básicamente le decía a APT que use como proxy el IP y puerto donde
estaba corriendo el demonio de apt-cacher-ng_ y este se ocupaba de
fijarse si ya lo tenía descargado, en ese caso no lo bajaba de nuevo,
y si no, lo bajaba, lo guardaba en el caché y lo servía.

El problema
-----------

Eso está muy bueno para paquetes `.deb`, que son los paquetes que
utilizan las distribuciones basadas en Debian. Pero, ¿qué hay de los
`.egg` o paquetes que usa Python?

.. TEASER_END

Mi problema es que cuando organizamos un Sprint, los asistentes
necesitan instalar un montón de estos paquetes y siempre se termina
saturando la red, pero hay un montón de gente que baja los mismos
paquetes (aquellos que van a trabajar en el mismo proyecto)

.. admonition:: Nota

   En la PyCon Argentina `@gilgamezh`_ llevó un mirror de pypi_, pero
   eso conlleva bajarse 120Gb y me dijo que le tomó 2 días en hacerlo.

   Y claramente, no se necesitaban esos 120Gb :)

Entonces, ¿no hay una forma de hacer un proxy de paquetes Python de la
misma forma que lo hace apt-cacher-ng_ para los `.deb`?

.. _apt-cacher-ng: https://www.unix-ag.uni-kl.de/~bloch/acng/
.. _pypi: http://pypi.python.org/

La solución
-----------

¡devpi_ al rescate!

Este programa sirve para hacer exactamente eso que hace apt-cacher-ng_
pero con paquetes de Python.

La forma de configurarlo en la máquina que va a hacer de servidor
(cache de paquetes) en pocos pasos:

.. code:: bash

   pip install -U devpi-server
   devpi-server --start

Luego, en la máquina que va a ser el cliente (quienes van a bajar los
paquetes Python de pypi_):

.. code:: bash

   pip install -i http://<ip-servidor-devpi>:3141/root/pypi/ simplejson

También podés usar una variable de entorno:

.. code:: bash

   export PIP_INDEX_URL=http://<ip-servidor-devpi>:3141/root/pypi/+simple/

Y si querés que sea permanente (útil para varios días de sprinto o
conferencias), editás el archivo `$HOME/.pip/pip.conf`:

.. code:: ini

   [global]
   index-url = http://<ip-servidor-devpi>:3141/root/pypi/+simple/


¡Decime si no es un golazo! Hay más opciones de configuración para
hacer cosas más avanzadas que también te recomiendo mirar. Por
ejemplo, tener una interfaz web.

.. admonition:: Nota

   Aunque no lo he probado, vale la pena tenerlo en cuenta,
   devpi-builder: https://pypi.python.org/pypi/devpi-builder/2.2.0


.. _devpi: http://doc.devpi.net/latest/index.html
.. _@gilgamezh: https://twitter.com/gilgamezh
