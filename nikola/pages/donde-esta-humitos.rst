.. title: ¿Donde está humitos?
.. slug: donde-esta-humitos
.. date: 2014-11-24 13:50:09 UTC-03:00
.. tags: argentina en python, mapas, blog, python
.. link: 
.. description: 
.. type: text

Este mapa es útil para saber en qué lugar estoy *aproximadamente* en
este momento, con el fin de contactar con gente de la zona para así
poder coordinar y organizarnos para encontrarnos.

.. raw:: html

   <div id="map"></div>

¿Cómo funciona?
---------------

En pocas palabras, cuando me conecto a internet se envía una señal a
mi blog para que actualice la posición en la que me encuentro,
utilizando la información de esa conexión a internet para saber dónde
estoy.

----

¿Cómo funciona *exactamente*?
-----------------------------

En profundidad, lo que hago es, mediante javascript, descargar el
archivo *point.json* que es dónde están las coordenadas de mi posición
actual y mostrarlo en el mapa:

.. TODO: acá hay un bug con Nikola que no me permite usar la directiva
   "include" (https://github.com/getnikola/nikola/issues/1506)

.. listing:: geolocation.js javascript

#. Descarga el *point.json*
#. Crea el mapa utilizando `leaflet.js <http://leafletjs.com/>`_
#. Agrega el punto que está en *point.json* al mapa
#. Centra el mapa en esa posición


Ese *point.json* lo genero con un script Python.

.. include:: geolocation.py 
   :code: python

#. Utiliza la librería *geocoder* para obtener las coordenadas de mi
   dirección de IP
#. Muestra en pantalla la longitud, latitud y el nombre del lugar
#. Guarda en el archivo *point.json* la longitud y latitud

.. note::

   Utilizo un *time.sleep(5)* así le doy un tiempo a NM para tener
   acceso a internet.


Ese script Python lo ejecuto con NetworkManager cuando este se conecta
a una red.

.. include:: geoblog
   :code: bash

Básicamente lo que hace es:

#. Loguea la fecha
#. Si la interfaz es levantada (*up*), ejecuta un script Python
#. Loguea la salida de ese script
#. Copia al servidor el archivo *point.json*

.. note::

   Es necesario usar *&* al final de cada comando así se ejecuta en
   background ya que NetworkManager `tiene un bug
   <https://bugzilla.redhat.com/show_bug.cgi?id=982734>`_ que mata los
   scripts si demoran más de 3 segundos. Como yo necesito acceso a
   internet para comprobar mi posición, me lo estaba matando.

¡Eso es todo!
