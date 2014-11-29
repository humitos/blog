.. link:
.. description:
.. tags: auto, garmin, gps, internet, portland, software libre, viaje
.. date: 2013/06/19 18:07:18
.. title: Actualizar GPS Garmin Nuvi 265W
.. slug: actualizar-gps-garmin-nuvi-265w


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2013/06/19/actualizar-gps-garmin-nuvi-265w/


Hace un par de días me compré un `GPS Garmin Nuvi
265W <http://www.amazon.com/Garmin-4-3-Inch-Widescreen-Bluetooth-Navigator/dp/B001ELJ9QK>`__
en Portland a través de `craigslist.com <http://craigslist.com>`__. Un
sitio dónde la gente vende cosas usadas que en general se las quiere
sacar de encima. Onda, no es que están buscando sacar una ganancia, sino
que en vez de tirarlo o donarlo tratan de sacarle unos mangos antes. Hay
cosas muy pero muy baratas. Yo al GPS lo pagué 45 dólares y una amiga
mia se compró un freezer por 60. ¡Cosa de locos!

Cuestión es que tiene los mapas de USA y alrededores, que mientras estoy
viajando, me vienen bien. Pero, ¿qué onda cuando llegue a Argentina?
¿tendrá los mapas de allá también? Lo que hice para ver eso fue ponerle
que quiero ir a Paraná, Entre Ríos y ver que en ese lugar solo tiene
marcada la RN18 y nada más. O sea, no tiene los mapas de Argentina.

Buscando un poco en internet caí en el `Proyecto
MapeAR <http://www.proyectomapear.com.ar/>`__. Me creé una cuenta y me
descargué la última versión de los mapas. Seguí los pasos que dice ahí
pero no funcionó. Así que tuve que seguir investigando un poco más y lo
conseguí. Además, como estoy en USA no quería perder los mapas que el
GPS trajo porque los voy a necesitar, así que usé una SD para no
sobreescribir los que ya trae. Estos son los pasos que seguí:

#. Descargar el archivo de mapas desde el Proyecto MapeAR
#. Descomprimirlo (es un .exe autoextraíble, así que tuve que usar Wine)
#. Crear una carpeta llamada "Garmin" en la tarjeta SD
#. Copiar el archivo "GMAPSUPP-2.img" dentro de la carpeta "Garmin" de
   la SD
#. Cambiar el nombre del archivo a "GMAPSUPP.img" (notar que le quité el
   "-2" que por alguna razón no lo reconoce)
#. Quitar la SD y ponerla en el GPS

Listo, ahora cuando puse "Paraná, Entre Ríos" en el GPS pude ver todas
las calles perfectamente y además, me mantuvo los mapas de USA que ya
traía.

 

**ACTUALIZACIÓN:** ayer Gastón me preguntó cómo actualicé los mapas de
USA en mi Garmin y no me acordaba bien. Hoy encontré el `post en
Taringa! <http://www.taringa.net/posts/info/16187657/Mapas-USA-2013-para-Garmin.html>`__
que es de dónde los bajé.

Además, también me contó que los mapas de MapeAr no son libres y que hay
un proyecto libre que se llama `OpenStreetMap que es para
Garmin <http://garmin.openstreetmap.nl/>`__. Así que, busqué Argentina y
descargué los mapas de Argentina (que resultó ser un archivo de 129Mb
-re liviano). Por lo que puedo ver en Paraná, hay algunos detalles en mi
barrio que no tiene (calles que no existen) y algunos nombres de calle
no están. Pero bueno, lo voy a probar un poco más a ver qué pasa.
