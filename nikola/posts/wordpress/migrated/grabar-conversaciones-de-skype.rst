.. link:
.. description:
.. tags: internet
.. date: 2011/03/30 08:12:01
.. title: Grabar conversaciones de Skype
.. slug: grabar-conversaciones-de-skype


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2011/03/30/grabar-conversaciones-de-skype/


Si te ha pasado que te has sentido **fruteado** por Skype y que
claramente no te quedó el log para mostrar a tus amigos y decirles:
"Che, mirá lo que me dijo el muy culeado", acá viene la solución. Se
llama `Skype Call Recorder <http://atdot.ch/scr/>`_ y lo podés
instalar fácilmente en Debian:

#. Dependencias

   .. code::

      sudo apt-get install libid3-3.8.3c2a libqt4-gui ﻿libmp3lame0

#. Descarga de Skype Call Recorder

   .. code::

      wget http://atdot.ch/scr/files/0.8/skype-call-recorder-debian_0.8_i386.deb

#. Instalación

   .. code::

      sudo dpkg -i skype-call-recorder-debian_0.8_i386.deb

#. Ejecución

   .. code::

      skype-call-recorder

Si utilizás otra distribución que no es Debian, podés consultar la
`sección Downloads <http://atdot.ch/scr/download/>`__ del sitio de Skype
Call Recorder para ver cómo instalarlo en tu distribución. Si usás OSX,
dejá un comentario explicando cómo lo instalaste :)

Acá está el `anuncio
oficial <http://forum.skype.com/index.php?showtopic=138491>`__.

Está buenísimo, podés configurarlo para que siempre te grabe todas las
llamadas o para que te pregunte qué hacer en cada una. Inicialmente
empieza grabando (para que no te pierdas el principio) y luego la podés
cancelar o aceptar. Además, se puede configurar dónde querés que te
guarde las llamadas y el tipo de archivo a usar.

 
