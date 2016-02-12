.. title: Audio en RaspberryPi
.. slug: audio-en-raspberrypi
.. date: 2016-02-08 15:42:41 UTC-03:00
.. tags: raspberrypi, red libre, perú, las lomas
.. category: 
.. link: 
.. description: 
.. type: text

La RaspberryPi se convirtió en esa cosa *super poderosa* que está
prendida todo el tiempo y que brinda un montón de servicios. Sí, ¿para
qué tener prendida mi notebook para ver un video? Para eso está
kodi_. ¿Para qué voy a tener un router y configurarlo extensivamente
y así y todo que no sirva todo lo que quiero? Para eso está
pyfispot_. Y, finalmente, ¿para qué voy a tener la pc prendida solo
para escuchar música? Para eso está `mplayer` y mps-youtube_.

.. figure:: IMG_20160208_144255.thumbnail.jpg
   :target: IMG_20160208_144255.jpg

   La RaspberryPi colgada, como siempre...



Cuando utilizo kodi_ siempre lo hago conectado a un TV con entrada de
HDMI, así el video y el audio se configuran solo sin ningún
problema. Luego manejo todo desde el celular con yatse_. Sin embargo,
a veces -como ahora- no tenemos un televisor pero sí queremos escuchar
música como si estuviésemos con kodi_: nuestras notebooks apagadas
pero la raspi reproduciendo música. Ok, instalé `mplayer` para eso y
pude reproducir la música que tengo localmente en la raspi sin
problemas. Lo único que tuve que hacer fue decirle a la raspi que
quiero utilizar el Audio Jack Analógico y no el HDMI:

.. code:: bash

   sudo amixer cset numid=3 1

Luego le doy permisos para usar el audio a mi usuario:
   
.. code:: bash

   sudo usermod -G audio -a alarm

Sin embargo, como dije antes, esto me permite escuchar sólo la música
que tengo localmente y con kodi_ nosotros escuchábamos música de
YouTube también. Ahí es que llegué a mps-youtube_, lo instalé y ya lo
estoy usando:

.. code:: bash

   ~/fades/bin/fades -d mps-youtube -x mpsyt

No hace falta que diga nada más. Es muy fácil de usar y tiene una
ayuda integrada.

.. admonition:: Versión obsoleta en Ubuntu 14.04
	     
      Si estás utilizando la versión LTS de Ubuntu, es probable que
      tengas una version obsoleta de mplayer, por lo que debes
      actualizarla. Sin embargo, en mi máquina no actualiza a una
      versión capaz de funciona correctamente con `mpsyt` por lo tanto
      instalé `mpv` y lo configué en `mpsyt` con este comando:

      .. code::

	 set player mpv
      
.. _kodi: http://kodi.tv/
.. _mps-youtube: https://pypi.python.org/pypi/mps-youtube
.. _pyfispot: https://github.com/humitos/pyfispot
.. _yatse: http://yatse.tv/

