.. title: Administrar mapas de Maps.me y OsmAnd
.. slug: administrar-mapas-de-mapsme-y-osmand
.. date: 2015-12-24 09:21:40 UTC-05:00
.. tags: openstreetmap, mapas, android, maps.me, osmand
.. category: 
.. link: 
.. description: 
.. type: text

El primer problema que tuve con los mapas de `OsmAnd
<http://osmand.net/>`_ es que, tarde o temprano, se te acaban las
descargas disponibles de mapas que trae la versión gratuita. Ya sea
por actualizarlos o bien porque vas necesitando mapas de otros países
a medida que te vas moviendo ;)

Luego, vinieron los problemas con `Maps.Me <http://maps.me/en/home>`_
que si bien uno puede descargar la cantidad de mapas que desee de
forma ilimitada, se ve que tienen algún problema en sus servidores ya
que es muy probable que la descarga demore mucho o que finalmente
termine fallando. A tal punto que ellos mismos `tienen una FAQ en su
sitio <http://maps.me/en/help#faq>`_ sobre este inconveniente.

Todo esto ya me venía diciendo que necesitaba una mejor forma de
administrar los mapas de OpenStreetMap en mi dispositivo
Android. Además, sumado a eso, a veces necesitaba compartir alguno de
los mapas (más actualizados) que yo tenía con mi compañera de
viaje. Por lo tanto, debería tener "a mano" una forma de enviarle unos
40~100 Mb de datos de una forma sencilla y que estos programas lo
puedan leer sin problemas.

Y para cerrar las *necesidades*, también quería poder exponer estos
mapas "ya descargados de internet" como servicio de nuestra
:doc:`red-libre` para que cuando no haya conexión todos podamos
descargarlos sin problemas.

Pero claro, para eso, necesitaba una buena forma de administrar todos
estos mapas y que sea confiable.

OsmAnd
------

OsmAnd tiene un sitio web de `descarga directa de mapas
<http://download.osmand.net/rawindexes/>`_ de donde podemos descargar
todos los mapas que deseemos para luego copiar a nuestro
dispositivo. Los trucos que debemos saber aquí son:

* Es necesario descomprimir el archivo `.zip` que bajamos
* Debemos copiar el archivo `.obf` dentro de la carpeta `osmand` (en
  mi Nexus 5 con Android 6.0.1 está en el directorio raíz)
* Hay que renombrar el archivo .obf quitando el `_2` de su nombre

.. admonition:: Resumir descargas con wget

   Si bajás los archivos de mapas con wget, siempre está la opción
   `-c` para resumir las descargas. Sin embargo, una vez descargado
   por completo el archivo, si volvemos a ejecutar ese mismo comando
   despues de un tiempo y ha habido una nueva actualización, el
   comando descargará solo la parte que le falta. Sin embargo, cuando
   lo copiemos a al dispositivo Android este mapa no será leído.

   .. code:: bash

      wget -c \
        "http://download.osmand.net/download.php?standard=yes&file=Peru_southamerica_2.obf.zip" \
        -O Peru_southamerica_2.obf.zip

Maps.Me
-------

Esta aplicación también tiene su propio `sitio de descarga de mapas
<http://direct.mapswithme.com/direct/latest/>`_ de una forma directa
(sin hacerlo desde su propia app).

En Maps.Me necesitamos descargar 2 archivos si es que queremos tener
la característica de *routing*. En cualquier caso, siempre debemos
descargar el `.mwm`, no es que si queremos routing *solo descargamos*
el `.routing`.

* Descargamos los archivos `.mwm` y `.routing` del país que deseamos
* Abrimos el archivo `settings.ini` que se encuentra en la carpeta
  `MapsWithMe` de nuestro dispositivo (en mi Nexus 5 está en el
  directorio raíz). Ahí buscamos el valor de `DataVersion` (una
  fecha), abrimos esa carpeta (o al creamos si no existe) y copiamos
  los archivos `.mwm` y `.routing` dentro de ella.

.. admonition:: Mapas desactualizados

   El tip del `DataVersion` me solucionó la notificación de Maps.Me
   diciéndome que mis mapas estaban desactualizados. Si por algún
   motivo te sigue indicando que está *outdated* deberías revisar que
   el nombre de la carpeta coincida con el nombre del DataVersion.
