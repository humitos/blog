.. link:
.. description:
.. tags: debian, software libre
.. date: 2012/02/08 16:32:12
.. title: Instalar HP p1005 en Debian Squeeze...
.. slug: instalar-hp-p1005-en-debian-squeeze

... sin morir en el intento.

Estoy bastante podrido de que "cada vez" que pasa "algo" (no sé
exactamente qué -si es una actualización del sistema operativo, cambian
los drivers de HP, cambia cups, o lo que sea-) se me pudre la impresora.
Deja de funcionar sin que siquiera se dé cuenta de que le estoy mandando
a imprimir algo. Ni noticias.

Ayer le dediqué un buen tiempo a investigar (y encontrar) la forma para
que pueda volver a instalarla sin renegar unas horas como venía haciendo
cada vez que se me *rompía*\ la impresora. Por suerte, como dije antes,
la encontré y paso a explicarla acá por si a algún otro le sirve.

#. Seguir los pasos listados acá
   http://hplipopensource.com/hplip-web/index.html para descargar el
   **.run** que vamos a utilizar. A mí me terminó tirando este
   `link <http://prdownloads.sourceforge.net/hplip/hplip-3.12.2.run>`__
   para Debian Squeeze
#. Una vez terminados los pasos anteriores, descargar el **.run** con el
   botón "Download HPLIP" y luego descargar también el certificado
   digital con el link "(Download Digital Certificate)" ya que sino la
   instalación falla a la mitad *(demoré bastante en descubrir que
   fallaba por esto)*
#. Instalar **foomatic-filters** y **foomatic-filters-ppds** con
   *apt-get*
#. Seguir los pasos listados acá:
   http://hplipopensource.com/hplip-web/install/install/index.html

Creo que eso es todo.

**UPDATE**: a veces pasa que la impresora se instala correctamente pero
luego no imprime (me pasó en una nueva instalación de Fedora 17 64
bits). Lo solucioné con el comando **hp-firmware**.
