.. link:
.. description:
.. tags: debian, software libre
.. date: 2009/02/26 17:10:42
.. title: Reportar un Bug en Debian
.. slug: reportar-un-bug-en-debian


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2009/02/26/reportar-un-bug-en-debian/


Hoy por la tarde (hace un rato, digamos), me comentaron que existía un
programa llamado `jdownloader <http://jdownloader.org/>`__ en cual sirve
para bajar múltiples archivos desde RapidShare, Megaupload, entre otros.
Lo primero que hice fue buscarlo en los repositorios de Debian: no lo
encontré. Luego fui a Google y caí al sitio web, me fijé si era libre y
no encontré nada al respecto. Sólo que era *open source*. Asique ni lo
bajé.

Después busqué *downloader*\ con el **apt-cacher** y me apareció una
lista bastante pequeña de paquetes, por lo que me intersó leer la
descripción de varios de los que estaban en esa lista, pero no quería ir
haciendo **apt-cache show** por cada uno de los paquetes, entonces me
fui derecho para el **aptitude** a ver si de alguna vez por todas lo
aprendo a usar :)

Entre que veía como se filtraba la lista de cosas y demás, me dí cuenta
que este paquete **tenía un bug**. Sí! había encontrado un bug en
Debian. Se ve que cuando tradujeron el programa le erraron al tipear :P
. Bueno che, no es un bug de los críticos pero es un bug.

|aptitude-bug|

Me fui derecho a la `página de Debian para ver como se reportaba un
bug <http://www.debian.org/Bugs/Reporting>`__, si mal no recuerdo en
Ubuntu había que llenar un formulario web, por lo que presupuse que iba
a ser más o menos parecido o... Mejor, no te olvides que esto es Debian
:) . La cuestión es que dice que es recomendable utilizar el programa
**reportbug**, asique le hice caso. Lo instalé, lo configuré y empezé a
ver como era este nuevo mundo.

Indiqué mis datos, como ser mail, nombre y demás. Le dije que era
*novato* en esto y que quería usar un entorno gráfico de consola. Para
esto tuve que instalar **python-urwid** ya que no es una dependencia
directa del programa. Una vez hecho esto, le dije que el paquete era el
*aptitude* y me bajó una lista de bugs conocidos para este, me fijé si
ya estaba reportado, no lo encontré y le dije que quería crear uno
nuevo. Me abrió el VIM con un montón de datos, como ser, las librerías
que usa, la versión del programa, de mi sistema y un montón de cosas
útiles para los desarrolladores. Ahí mismo escribí la descripción del
problema y le dije que quería enviarlo por mail, se cerró el programa y
me dijo que se había enviado.

Miré como quedó la consola y no decía nada, ni un número de bug ni nada
por el estilo. Asique pensé: "¿Habrá salido el mail?". Pregunté en el
canal de #grulic y mientras tanto iba chequeando el mail. No pasaron ni
5 minutos que ya tenía una respuesta en el mail diciendo que había
llegado correctamente y el número de bug. `Éste
es <http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=517272>`__.
Seguramente le pifié feo feo en el inglés, pero bueno... La intención es
lo que cuenta.

.. |aptitude-bug| image:: http://humitos.files.wordpress.com/2009/02/aptitude-bug.png
   :target: http://humitos.files.wordpress.com/2009/02/aptitude-bug.png
