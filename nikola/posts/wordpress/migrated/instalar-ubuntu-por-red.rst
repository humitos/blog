.. link:
.. description:
.. tags: software libre, ubuntu
.. date: 2007/10/24 18:20:13
.. title: Instalar Ubuntu por red
.. slug: instalar-ubuntu-por-red


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/10/24/instalar-ubuntu-por-red/


Como comenté en un post anterior. Estuve un tiempo considerable
intentando instalar Ubuntu por la red **sin** que este se descargue
completo desde internet. Sino que utilice una imágen del cd de Ubuntu.

Para esto se necesitan varias cosas. Primeramente tener dos computadoras
conectadas vía red ;) . Además haber descargado el disco (imagen .iso)
de Ubuntu en su versión **desktop** para una fácil instalación ya que lo
que hacemos es, primeramente, bootear la pc cliente mediante *netboot*
por *pxe/bootp*, adquirir una dirección de ip y pasar el kernel para
bootear por tftp. Este kernel muestra una pantalla de selección de
opciones en la que debemos elegir la que vamos a crear (*Live
CD/install*) que le pasará el control al segundo kernel que se tomará
del *Live CD*.

Por otra parte también debemos tener instalados el servidor **dhcp**,
uno de **tftp** y otro de **nfs**. Los paquetes que instalé en la
máquina servidor (Kubuntu 7.04 tenía en ese momento) fueron:
*dhcp3-server*, *nfs-kernel-server*, *tftpd*.

Lo primero que hice fue configurar el servidor DHCP,  agregando al
archivo */etc/dhcp3/dhcpd.conf*\ éstas líneas (mi archivo de
configuración me quedó `así <http://www.paste-it.net/4148/raw/>`__):

::

    host pxeinstall {
      hardware ethernet 00:11:2f:1e:3c:d3;
      fixed-address 10.0.0.4; # dirección de la máquina cliente
      next-server 10.0.0.5;     # dirección de la máquina servidor de TFTP
      filename "pxelinux.0";
    }

Después de configurar esto, descargué la imagen .iso de Ubuntu desktop y
la monté en la carpeta ~/tftp configuré el servidor **nfs** para que la
dirección de ip asignada a la máquina cliente tenga acceso a esta
carpeta (archivo */etc/exports*) y reinicié el servicio.

Luego configuré el servidor tftp. Para esto bajé el archivo
`netboot.tar.gz <http://archive.ubuntu.com/ubuntu/dists/gutsy/main/installer-i386/current//images/netboot/386/netboot.tar.gz>`__
y lo descomprimí en la carpeta dónde está configurado el servidor tftp.
Copié los archivos *vmlinuz*\ y *initrd.gz* desde la carpeta */casper*
de la imagen del CD al directorio del servidor tftp. Los copié con el
siguiente comando para así también renombrarlos y no confundir luego:

    *cp -a ~/ftp/casper/vmlinuz
    /var/lib/tftpboot/vmlinuz.fromUbuntu704DesktopCd cp -a
    ~/ftp/casper/initrd.gz
    /var/lib/tftpboot/initrd.gz.fromUbuntu704DesktopCd*

Para finalizar edité el archivo */var/lib/tftpboot/pxelinux.cfg/default*
agregando las líneas (mi archivo quedó
`así <http://www.paste-it.net/4149/raw/>`__):

::

    DEFAULT manuel

    LABEL manuel
            kernel vmlinuz.fromUbuntu704DesktopCd
            append initrd=initrd.gz.fromUbuntu704DesktopCd boot=casper netboot=nfs nfsroot=10.0.0.5:/home/manuel/ftp --

Por útlimo en la máquina cliente tipeamos el nombre del LABEL que le
hallamos puesto cuando aparece el menú (yo le puse *manuel*) y listo!
Arranca el LiveCD de forma transparent. Click en **Instalar** y a
esperar los 5 minútos que demora (se instala **rapidísimo**)
