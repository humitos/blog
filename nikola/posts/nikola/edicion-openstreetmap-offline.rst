.. title: Edición OpenStreetMap offline
.. slug: edicion-openstreetmap-offline
.. date: 2015-06-21 01:23:29 UTC-03:00
.. tags: argentina en python, openstreetmap, viaje, mapa, josm
.. category: 
.. link: 
.. description: 
.. type: text


Durante mis viajes con `Argentina en Python
<http://argentinaenpython.com.ar>`_ una de las cosas que me gusta
hacer es colaborar con la comunidad de OpenStreetMap_. Siento que esto
es bastante útil ya que estoy todos los días en movimiento y visitando
lugares que, en su mayoría, no está correctamente mapeados o falta
información.

Sin embargo, en la mayoría de los casos, la cantidad de información
que tiene los mapas de OpenStreetMap es la mejor que tenemos
disponible hoy en día. Incluso, mejor que Google Maps. Como todo, no
es perfecto y siempre encuentro algo que falta: en mayor o menor
medida.

.. _OpenStreetMap: http://osm.org

Utilizo mucho osmtracker_ para realizar mis trazas GPS y añadir puntos
a estas trazas. Luego, las importo en JOSM, las corrijo, las adapto y
las subo a OSM.

.. _osmtracker: http://wiki.openstreetmap.org/wiki/OSMtracker_%28Android%29


El problema
-----------

Uno de los problemas que tengo con esto es que *siempre necesito estar
OnLine* para hacer mis ediciones ya que, primero, necesito bajar la
zona del mapa en la que necesito laburar. Eso es algo que no tiene
ningún *problema* en realidad, pero para mí sí lo es. Esto es porque
muchas veces no tengo internet (ya que suelo estar en lugares donde no
es tan accesible) y, cuando tengo internet, necesito hacer otras cosas.

Entonces, la mayoría de las veces que tengo tiempo disponible para
colaborar con OpenStreetMap es *cuando **no** tengo internet*.

Hoy, en la `Python Paraguay #1 Meetup
<http://www.meetup.com/Python-Paraguay/events/223289056/>`_ aprendí a
cortar los mapas de OSM en pedazos utilizando `osmconvert`_ y aproveché
ese conocimiento que adquirí para resolver este problema.


La solución
-----------

Básicamente lo que hago es, cuando tengo internet:

#. Bajo los mapas de Latino América del mirror geofabrik

   .. code:: bash

      wget -c http://download.geofabrik.de/south-america-latest.osm.pbf

#. Descargo el archivo `.poly` del país en el que me interesa trabajar
   utilizando esta web: http://polygons.openstreetmap.fr/

.. TEASER_END

----

Cuando no tengo internet:

#. Abro el archivo `.poly` con JOSM.


   .. figure:: visualizar-poly.thumbnail.jpg
      :target: visualizar-poly.jpg

      paraguay.poly abierto en JOSM


#. Creo una capa nueva.

#. Dibujo un cuadrado con la herramienta "Dibujar nodos (A)" cubriendo
   la zona en la que *me interesa trabajar* dentro de ese país.

   .. figure:: zona-a-trabajar.thumbnail.jpg
      :target: zona-a-trabajar.jpg

      Cuadrado dibujado para trabajar offline en esa zona


#. Guardo esa capa como `.poly`

#. Utilizo osmconvert_ para recortar el mapa de South America
   utilizando el archivo de polígonos que acabo de crear:

   .. code:: bash

      ./osmconvert \
	     south-america.osm.pbf \
	     -B=paraguay.poly \
	     --out-osm \
	     -o=south-america-my_region.osm

#. Abro el archivo `south-america-my_region.osm` desde el JOSM y
   trabajo offline con los GPX que guardé con osmtracker_.

   .. figure:: zona-offline.thumbnail.jpg
      :target: zona-offline.jpg

      Zona para trabajar offline (recortada del archivo de mi pc -sin
      conexión)

#. Una vez finalizado el trabajo, lo guardo.

----

Cuando vuelvo a tener internet:

#. Abro con JOSM el archivo que guardé.

#. Voy a *Archivo -> Actualizar Datos* (Control + U)

#. Subo los datos de la capa que agregué yo

.. _osmconvert: http://wiki.openstreetmap.org/wiki/Osmconvert


Los agradecimientos
-------------------

Esto me permite trabajar cómodo desde cualquier lado y offline sin
preocuparme si voy a tener internet o no cuando llegue a un lugar
donde esté cómodo y pueda trabajar tranquilo escuchando música y
tomando mates :)

Por favor, dejá un comentario con feedback sobre los pro- y cons- de
esta forma de trabajo y otras alternativas en caso de que conozcas.

Gracias a `@51114u9 <https://twitter.com/51114u9>`_, a `@proyectosbeta
<https://twitter.com/proyectosbeta>`_ por el apoyo de siempre en todo
lo referido a OpenStreetMap y a toda la comunidad de `@PythonParaguay
<https://twitter.com/PythonParaguay>`_ ya que esta idea salió en la
Meetup de hoy ;)
