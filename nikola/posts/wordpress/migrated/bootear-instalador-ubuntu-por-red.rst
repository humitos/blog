.. link:
.. description:
.. tags: software libre, ubuntu
.. date: 2007/10/08 14:56:13
.. title: Bootear instalador Ubuntu por Red
.. slug: bootear-instalador-ubuntu-por-red


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/10/08/bootear-instalador-ubuntu-por-red/


***Update:**\ siguiente este
`link <https://help.ubuntu.com/community/Installation/LocalNet>`__, pude
concretar\ **todo** lo que no pude hacer cuando escribí este post.
[STRIKEOUT:Cuando tenga más tiempo comento cómo lo hice ya que el link
está en inglés.]*

***Update:*** *comenté cómo logré instalar Ubuntu por la red en este
`post <http://humitos.wordpress.com/2007/10/24/instalar-ubuntu-por-red/>`__.*

Hace un tiempo bastante considerable que estoy intentando esto.
Principalmente lo que quería es instalar Ubuntu en una computadora que
no tiene ningún Sistema Operativo, no tiene lectora de CD's pero si
tiene disquetera. Asique pensé de qué formas podía bootear un instalador
de Linux en esa PC. Y se me ocurrieron estas:

-  USB, incluso en un post anterior expliqué cómo meter `Slax Linux en
   un Pen
   Drive <http://humitos.wordpress.com/2007/08/30/slax-linux-en-usb-pendrive/>`__.
   Luego debería investigar cómo hacer desde una distribución Linux Live
   instalarlo.
-  Floppy, botear con un disquete en el que entre una distro de linux y
   nuevamente investigar cómo instalar algún linux (incluso Debian tiene
   un instalador para esto).
-  NetBoot, bootear el sistema por medio de una red, conectándose a otra
   computadora que permita este booteo.

Decidí por NetBoot ya que me parecía muy interesante y aparte de las
otras formas tenía que descargar todo el sistema desde internet, lo cual
*supuestamente* por esta opción no. Por el momento yo logré bootear por
la red únicamente el instalador para luego descargar el sistema por
internet, todavía no he podido configurar el servidor
`TFTP <http://es.wikipedia.org/wiki/TFTP>`__ para pasar el disco de
Ubuntu.

Para poder llevar adelante la configuración de esto es necesario tener
conocimientos de algunas cuestiones de redes, que yo no los tengo, por
lo que me costó **mucho** llevarlo adelante e incluso no pude cubrir
todas mis espectativas.

Lo primero que debemos ver es si la máquina en la cuál queremos bootear
por la red tiene esta capacidad, incluso aunque en el BIOS figure la
opción puede que no la tenga, ya que se necesita que la placa de red
tenga un software llamado
`PXE <http://en.wikipedia.org/wiki/Preboot_Execution_Environment>`__ que
nos permite conectarnos a la otra PC para bootear.

Para saber esto busqué en Google el modelo de mi placa madre y me fijé
si tenía esta funcionabilidad y cómo se activaba ya que cuando la busqué
en el BIOS no la encontré :D . Luego de saber esto necesitamos montar un
servidor `DHCP <http://es.wikipedia.org/wiki/Dhcp>`__ y uno TFTP,
incluso pueden ser máquinas distintas. En mi caso utilicé la misma para
los dos.

**Configurando el servidor DHCP:**

Encontré dos mil millones de manera de hacer esto, siguiendo los pasos
al pié de la letra con ninguna dí en la tecla. Pero bueno, hice varios
experimentos hasta que llegué a ver la pantallita del instalador de
Ubuntu!

Lo que tuve que hacer para esto primeramente instalar el paquete
*dhcp3-server* y luego editar el archivo de configuración
*/etc/dhcp3/dhcpd.conf*\ para que quede
`así <http://www.paste-it.net/3865/raw>`__, lo único que hice fué
agregar estas líneas:

::

    subnet 10.0.0.0 netmask 255.255.255.0 {
      range 10.0.0.0 10.0.0.253;
      filename "pxelinux.0";
    }

    host pxeinstall {
      hardware ethernet 00:11:2f:1e:3c:d3;
      fixed-address 10.0.0.4;
      next-server 10.0.0.5;
      filename "pxelinux.0";
    }

**Configurando el servidor TFTP:**

Lo primero que hice fue instalar el paquete *tftpd-hpa*, luego
configurar el archivo */etc/inetd.conf* agregando la siguiente línea, de
modo que quede `así <http://www.paste-it.net/3866/raw/>`__:

::

    tftp    dgram   udp    wait    root    /usr/sbin/in.tftpd /usr/sbin/in.tftpd -s /var/lib/tftpboot

Copié desde el CD de Ubuntu para la instalación alternativa (Alternate
CD) la el contenido de la carpeta *install/netboot/*:

    *$ sudo cp -r /media/cdrom/install/netboot/\* /var/lib/tftpboot/*

Y por último edité el archivo
*/var/lib/tftpboot/ubuntu-installer/i386/pxelinux.cfg/default* para que
me quede `así <http://www.paste-it.net/3867/raw/>`__ modificando las
líneas de **LABEL install** dejándolo como sigue:

::

    LABEL install
            kernel ubuntu-installer/i386/linux
            append vga=normal initrd=ubuntu-installer/i386/initrd.gz boot=casper netboot=nfs nfsroot=10.0.0.5:/media/iso/  --

**Finalizando las configuraciones:**

A este momento creo que lo último que queda es reiniciar el servicio de
*dhcp* que se puede hacer ejecutando el comando:

    *$ sudo /etc/init.d/dhcp3-server restart*

Luego encender la otra máquina con los cables de red conectados de forma
correcta :D . Lo único que tuve que hacer fué prender varias veces la PC
ya que tengo un Router que también tiene servidor DHCP por lo que a
veces a la máquina en la que quería instalar Linux la agarraba este y no
cargaba el instalador. Secuencia en fotos de lo que fue pasando en la
máquina cliente.

|image0|

|image1|

|image2|

|image3|

|image4|

**Otras cuestiones:**

*Espero que con los comentarios me corrijan todo tipo de errores que
puedo llegar a tener, ya que fue un experimento a prueba y error, y
quizás me estoy olvidando algo. Incluso si saben de un link que al
seguirlo al pie de la letra funcione, lo publiquen.*

*Por otro lado, las fotos las saqué con una cámara digital, ya que no sé
como capturar las pantallas del BIOS por ejemplo, y del instalador de
Ubuntu, osea, no puedo capturar pantallas sin haber cargado un X.*

[STRIKEOUT:*Hasta el día de hoy tampoco pude hacer que no descargue
todos los archivos para la instalación de Ubuntu desde internet, e
incluso quise instalarlo descargando **todo** y se tildó a la mitad de
la instalación porque no pudo descargar algunos archivos.*]

*A través de sus comentarios y lo que pueda seguir investigando con el
tiempo este post será actualizado y corregido, espero la colaboración de
ustedes.*

.. |image0| image:: http://img230.imageshack.us/img230/7461/hpim2154eg7.th.jpg
   :target: http://img230.imageshack.us/img230/7461/hpim2154eg7.jpg
.. |image1| image:: http://img260.imageshack.us/img260/4263/hpim2155in6.th.jpg
   :target: http://img260.imageshack.us/img260/4263/hpim2155in6.jpg
.. |image2| image:: http://img46.imageshack.us/img46/5214/hpim2152jk7.th.jpg
   :target: http://img46.imageshack.us/img46/5214/hpim2152jk7.jpg
.. |image3| image:: http://img260.imageshack.us/img260/6419/hpim2156vi2.th.jpg
   :target: http://img260.imageshack.us/img260/6419/hpim2156vi2.jpg
.. |image4| image:: http://img219.imageshack.us/img219/706/hpim2160qe1.th.jpg
   :target: http://img219.imageshack.us/img219/706/hpim2160qe1.jpg
