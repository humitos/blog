.. title: Seguridad de los paquetes de Python
.. slug: seguridad-de-los-paquetes-de-python
.. date: 2014/04/17 14:45:02
.. tags: python, software libre
.. link: 
.. description: 
.. type: text


El martes pasado publiqué mi primer paquete de Python
(:doc:`pega-todo-en-linkodeorg`) utilizando el sistema PyPI. Por un
lado, me gustó que sea super fácil de subir tu paquete al sistema de
paquetes de Python, lo que permite que después sea super fácil de
instalarlos también mediante el uso de `easy_install` o `pip` en una
sola línea. Además, es muy sencillo de especificar los requerimientos
de tu paquete (puede que dependa de otros) y basta con solo nombrarlos
y agregarle el número de version. Hasta ahí, ¡todo una ganga!

Esta configuración se hace mediante un script de configuración que es
requerido por PyPI que se llama `setup.py` y que no es más que un
script Python, en dónde está permitido hacer todo lo que sea necesario
para instalar nuestro paquete. Acá viene lo que me llamó la atención:
como podés ejecutar cualquier cosa que sea Python dentro de ese
script, es muy fácil de romper cuantas computadoras quieras ya que
podés *borrar* todo lo que quieras o bien, y más peor aún, *robar*
cualquier tipo de información que tenga el usuario en la PC y mandarla
por email a dónde más te guste, en simples pasos.

Es más, muchas veces queremos instalar un paquete Python pero no
dentro de nuestro `virtualenv`, sino que queremos que esté disponible
para todos los proyectos en los que estamos trabajando y para eso,
necesitamos instalarlo diréctamente en los paquetes del sistema. Para
eso, ejecutamos el mismo comando que antes, pero le agregamos `sudo`,
algo así::

  sudo pip install <nombre-del-paquete>

Eso, sí, así como lo ves, nos puede romper toda la máquina.

Entiendo cuál es el problema y no estoy seguro de cuál es la solución,
ya que la idea de PyPI es que *cualquiera* pueda publicar un paquete y
ponerlo a disposición de todo el mundo. Es por eso, que los paquetes
no pasan por una verificación previa y a todos se les permite el
acceso a este servicio.

`Escribí un ejemplo de setup.py`_ que borra un archivo creado por root
bajo la carpeta `/tmp`. La forma de comprobar esto sería algo así:


.. code:: bash

  # ejecuando como un usuario sin privilegios de root
  sudo touch /tmp/sudo.file
  python setup.py -h

Eso nos va a preguntar si queremos borrar el archivo `/tmp/sudo.file`
y aunque le pongamos que sí, los permisos que tenemos como usuario
normal no lo va a borrar y nos va a dar un error. Sin embargo, si
ejecutamos el mismo script, pero como root (o enmascarado através de
sudo) sí lo va a borrar e incluso no nos va a preguntar nada:

.. code:: bash

  # ejecuando como un usuario CON privilegios de root
  sudo python setup.py -h

Busqué un poco en Google sobre esto para ver si encontraba algún foro
de discusión así podía leer sobre otras opiniones pero no
encontré. ¿Qué se anda diciendo por ahí sobre este tema? ¿Qué opinan
los que leyeron este post?


.. _Escribí un ejemplo de setup.py: /listings/seguridad-de-los-paquetes-de-python/setup.py.html
