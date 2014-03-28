.. link:
.. description:
.. tags: ubuntu
.. date: 2007/08/30 23:48:18
.. title: Slax Linux en USB pendrive
.. slug: slax-linux-en-usb-pendrive


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/08/30/slax-linux-en-usb-pendrive/


|Slax linux|\ Hace tiempo que quería *meter*\ linux en mi pendrive.
Justamente **hoy** lo conseguí. Antes había probado la distro
`Slax <http://www.slax.org/?lang=es>`__ que está basada en
`Slackware <http://www.slackware.com/>`__ y me había gustado mucho, ya
que es bastante rápida para cargar, ocupa 211 Mb y trae el KDE que es el
Desktop que más me gusta.

Lo había grabado en un CD para probarlo y estuve investigando cómo
agregarle funcionalidades y programas, y esto la verdad que es muy fáci.
Simplemente se agregan los módulos correspondientes de los programas que
queremos y listo (descargamos un archivo y lo agregamos al iso o lo
hacemos on-the-fly).

Con la versión 6 rc6 no me costó nada de nada hacer que la pc me bootee
desde el pendrive. Me bajé la versión que menciono desde la página
oficial, concretamente
`ésta <ftp://ftp.linux.cz/pub/linux/slax/SLAX-6.x/rc6/slax6rc6.iso>`__.
Luego monté esta imágen .iso con el comando:

    *$ sudo mount slax6rc6.iso -o loop -t iso9660
    /home/manuel/virtualcd/*

Después copié todos las carpetas que se muestran ese directorio *(boot y
slax)* al pendrive. Y por último lo que hice fué desde la carpeta
*/boot* del pendrive ejecutar el script:

    *$ ./bootinst.sh*

Listo! Ahora lo único que resta es configurar el
`BIOS <http://es.wikipedia.org/wiki/BIOS>`__ para que bootee desde el
USB antes que del HDD (disco duro).

Después seguí investigando para poder guardar todas las configuraciones
(que *eso* era realmente lo que me importaba más que nada; ya que desde
el CD ya lo había conseguido pero era bastante complicado, o a veces no
tenía una grabadora en el lugar que lo estaba corriendo). Para esto hay
que descomprimir el archivo *slaxsave.zip*\ que está la carpeta */slax*
del pendrive, eligiendo el tamaño que queremos que ocupe el archivo de
configuración. Por el momento hay 4 archivos, uno de 1 Gb, otro de 512,
256, y 128 Mb. Yo elegí el de 128 Mb pero luego automáticamente creció
cuando agregé algunas cosas. A este archivo lo descomprimimos nuevamente
y crea en el directorio */slax* el archivo *slaxsave.dat* que es dónde
se guardarán los datos de las configuraciones.

Después de esto, booteamos desde el pendrive y las configuraciones se
guardarán de forma automática en este archivo.

.. |Slax linux| image:: http://img442.imageshack.us/img442/8051/slaxrt4.png
