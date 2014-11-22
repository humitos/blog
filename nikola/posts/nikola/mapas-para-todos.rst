.. title: Mapas para todos
.. slug: mapas-para-todos
.. date: 2014-10-13 16:54:17 UTC-03:00
.. tags: argentina en python, mapas, proyecto mapear, openstreetmap, garmin, gps, viajes, auto, osm
.. link:
.. description:
.. type: text

En otra :doc:`oportunidad ya he hablado sobre el GPS
<actualizar-gps-garmin-nuvi-265w>`, Proyecto Mapear y `Openstreetmaps
<http://openstreetmap.org/>`_. En ese tiempo estaba usando mucho
Proyecto Mapear y tenía a Openstreetmap como segunda opción ya que me
parecía que no contaba con tanta información...

Después de unos meses, estuve investigando un poco más en profundidad
cómo funcionaba esto de OSM y decidí suscribirme a la `lista de correo
de Argentina <https://lists.openstreetmap.org/listinfo/talk-ar>`_ y
preguntar algunas cositas. Ahí me recomendaron usar `josm
<https://josm.openstreetmap.de/>`_, un editor para los mapas. Muy
copado, por cierto.

Así que, me puse a investigar un poco cómo venía la mano y traté de
acomodar algunas calles de la zona de mi barrio que es algo que
conozco bien y así empezar a aprender cómo se usaba el software de
mapeo.

Hoy en Salta, después de recopilar bastante información con el GPS del
auto, volví a leer las guías de OSM y empecé a mapear con datos reales
que había notado que no estaban cargados en los mapas libres
[#]_. Después de un par de horas de dedicación al mapeo y la lectura,
diseñé una metodogía de trabajo que puede acelerar el mapeo a futuro.

#. Activar la opción de trazado en el GPS.

   * Utilidades -> Configuración -> Mapa -> Registro trayecto -> Mostrar

#. Siempre que salgamos en auto tener el GPS encendido

   * Para esto, agregué un cable extra que sale de la batería y se
     conecta directamente al cargador del GPS. De este modo, cada vez
     que pongo el auto en marcha el GPS se prende automáticamente.

   * Esto no es estrictamente necesario, pero en mi caso, uso el
     enchufe del encendedor del auto para otra cosa.

#. Marcar en los `Favoritos` del GPS *todos* los puntos que luego
   queramos agregar al mapa. Estos pueden ser Rutas, Calles, Puentes,
   Puntos de Interés (Estaciones de Servicio, Hoteles, Atracciones,
   etc)

.. TEASER_END: Seguir leyendo...

Siguiendo estos 3 pasos, luego será mucho más fácil cargar la
información que recopilamos utilizando JOSM.

Recomiendo leer estas guías oficiales para luego cargar la información
utilizando JOSM:

#. http://wiki.openstreetmap.org/wiki/JOSM/Guide

#. http://wiki.openstreetmap.org/wiki/JOSM/Basic_editing

#. http://learnosm.org/es/

Una vez que hayamos cargado todos los datos que consideremos que
hacían falta, lo último que nos queda es actualizar el GPS con esos
nuevos datos. Para eso yo utilizo un sitio web que genera un archivo
`gmapsupp.img` específico para Garmin.

.. sidebar:: Actualización 8 de Nov 2014

   Encontré estos mapas que están listos para usarse (solo hay que
   bajar y copiar el archivo al GPS) y muy pulidos para todo lo que es
   Argentina. Altamente recomendables ya que tienen un activo y
   continuo desarrollo:

   http://www.i-nis.com.ar/osm/garmin

#. Entramos a http://garmin.openstreetmap.nl/

#. Seleccionamos las opciones:

   * Choose your map type: Generic Routable

   * Include a TYP file (Optional): Mapnik

   * Perhaps you'd like to add some additional tiles?: Tildado

#. Seleccionamos el área en el mapa que queramos

   * Actualmente seleccioné solo el norte y centro de Argentina y los
     limítrofes (Salta, Jujuy, Bolivia, Paraguay, etc.)

   * Este mapa ocupa tan solo 53 Mb

#. Ingresamos nuestro email, hacemos click en *Build my map* y
   esperamos a que nos llegue el mail con el link para descargar el
   mapa recién generado y actualizado

#. Cuando nos avise que esté listo, descargamos el archivo
   *osm_generic_gmapsupp.zip* y lo descomprimimos en la SD que tenemos
   en el GPS dentro de la carpeta *Garmin*

¡Ya está! Toda la información que acabamos de subir sobre carreteras y
POIs ahora está disponible en nuestro GPS y en el de todos aquellos
que lo necesiten.

Una muestra de cómo se ven los OSM con la opción para incluir el archivo TYP:

.. figure:: osm.thumbnail.jpg
   :target: osm.jpg

   OpenStreetMaps funcionando en Garmin Nüvi 265w

.. figure:: mapear.thumbnail.jpg
   :target: mapear.jpg

   Proyecto Mapear funcionando en Garmin Nüvi 265w

Como se puede ver, las imagenes son similares en cuanto a su
estructura urbana, pero sin embargo la versión de OSM es mucho más
agradable a la vista () y encima tiene todos los senderos del parque
cargados. ¡Maravilloso! . Esto mismo pasa en muchísimos otros lugares,
dónde los senderos peatonales en parques y atractivos turísticos **sí
están marcados** en OSM.

.. epigraph::

   La información es poder.

   -- http://learnosm.org/es/

.. [#] ¡sí, son libres!
