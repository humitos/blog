.. link:
.. description:
.. tags: debian, internet, software libre
.. date: 2009/10/19 12:53:26
.. title: Hora adelantada en Debian
.. slug: hora-adelantada-en-debian


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2009/10/19/hora-adelantada-en-debian/


Ayer prendí la notebook y encontré que tenía 1 hora adelantada mi
máquina. Esto se debe a que este año no se aplicó la\ `ley
26.350 <http://infoleg.mecon.gov.ar/infolegInternet/anexos/135000-139999/136191/norma.htm>`__.

Lo que debemos hacer para corregir este error es actualizar a la última
versión el paquete **tzdata** quién es el que contiene la información
sobre las zonas horarias en todo el mundo.

Para actualizarlo debemos agregar a nuestras fuentes de paquetes el
repositorio:

::

    deb http://ftp.de.debian.org/debian sid main

Y luego ejecutar la actualización de fuentes con

::

    apt-get update

, después de esto instalar la nueva versión del paquete desde sid:

::

    apt-get install -t sid tzdata

Listo.

Fuentes:

-  http://www.summarg.com/foro/sistemas-operativos-f81/horario-argentina-1-hora-adelantado-en-distribuciones-debian-t3333/
-  http://ubuntuforums.org/archive/index.php/t-938859.html
-  http://packages.debian.org/sid/all/tzdata/download

