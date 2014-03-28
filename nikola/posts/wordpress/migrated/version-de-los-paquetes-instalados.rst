.. link:
.. description:
.. tags: debian, general, software libre
.. date: 2010/08/16 12:54:49
.. title: Versión de los paquetes instalados
.. slug: version-de-los-paquetes-instalados


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2010/08/16/version-de-los-paquetes-instalados/


Ayer a la noche tuve un problema con una actualización de APT, ya que al
hacer "apt-get upgrade" me quería eliminar varios paquetes que yo no
quería quitar, pero se ve que por un problema de dependencias no podía
dejarlos instalados.

Buscando un poco en Google caí a esta guía:
http://www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html , y
aunque no resolví el problema leyendo eso, encontré un comando muy útil:
**apt-show-versions**

La idea de éste comando es mostrar la versión que tenés instalada en el
sistema de un paquete en particular, así como también saber a qué
release pertenece y si hay una versión más actualizada en internet. En
algún sentido sirve para lo mismo que "dpkg -l" pero con un poco más de
onda para mí:

.. code:: bash

   humitos@teresa: ~$ apt-show-versions iceweasel  iceweasel/testing uptodate 3.5.11-1  
   humitos@teresa: ~$ dpkg -l iceweasel
   Desired=Unknown/Install/Remove/Purge/Hold
   | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend  
   |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)  
   ||/ Nombre                                  VersiÃ³n     DescripciÃ³n  
   +++-=======================================-==========================
   ii  iceweasel                               3.5.11-1     Web browser based on Firefox
   humitos@teresa: ~$ ``
