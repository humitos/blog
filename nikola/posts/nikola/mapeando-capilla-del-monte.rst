.. title: Mapeando Capilla del Monte
.. slug: mapeando-capilla-del-monte
.. date: 2014-11-07 15:23:53 UTC-03:00
.. tags: argentina en python, capilla del monte, córdoba, openstreetmap, software libre, viaje
.. link: 
.. description: 
.. type: text

.. sidebar:: ¿Cuál de los dos elegir?

   El que *hay que usar* es Field Papers (ya que es nuevo y mejor)
   pero luego de hacer varias pruebas en el sitio web, me di cuenta de
   que actualmente no está funcionando correctamente ya que el mapa
   generado contiene algunos cuadrados en negro.

   Reporté el bug acá:
   https://github.com/stamen/fieldpapers/issues/221

   Espero que solucionen este problema rápido.

El Miércoles estuve leyendo un poco sobre `Field Papers
<http://fieldpapers.org/>`_ y `Walking papers
<http://walking-papers.org/>`_ (`guía en Español
<http://learnosm.org/es/beginner/walking-papers/>`_) para entender
cómo funcionaban, salir a ponerlo en práctica y luego poder hablar con
conocimiento en la causa; entender qué se puede hacer y compartirlo
con quienes corresponda en el momento adecuado.

En primer lugar, lo que tuve que aprender fue sobre cuál es la
diferencia de cada uno de ellos. Ambos parecen cumplir la misma
función, los dos tienen un sitio web para generar los mapas y también
un plugin para luego usarlos en JOSM. La diferencia es simplemente que
Field Papers es una *evolución* de Walking Papers y... Nada más,
digamos.

Sí, ok, ¿pero de qué va todo esto? Bueno, la idea principal es:

#. Imprimir una porción del mapa del lugar que querés mapear

   .. figure:: walking-paper-77cph8f8.thumbnail.jpg
      :target: walking-paper-77cph8f8.jpg

      Mapa impreso con Walking Papers

.. TEASER_END

#. Salir a caminar por esa zona marcando la información que falta en
   el mapa:

   * Nombre de calles
   * Numeración de calles
   * Puntos de interés (Escuelas, Comercios, Estaciones de Servicios, etc)
   * Senderos peatonales
   * Nuevas calles
   * ... y todo lo que falte en el mapa impreso

#. Sacarle una foto / Escanearlo

   .. figure:: walking-capilla-3.thumbnail.jpg
      :target: walking-capilla-3.jpg
   
      Mapa marcado luego de la caminata
   

#. `Subir esta nueva versión
   <http://walking-papers.org/scan.php?id=tx869br8>`_ al sitio web
   (Field Papers / Walking Papers)

Una vez subida la imagen se puede tomar uno de dos caminos:

#. Indicar que nosotros NO vamos a cargar esa información en el mapa
   de OSM: de esta forma, la imagen queda pública para que otros
   mapeadores agreguen esa información luego.

#. Utilizar JOSM para cargar esta información. Entonces, ¿cuál es el
   beneficio de hacer esto si voy a usar JOSM igualmente? Lo bueno de
   esto es que JOSM utiliza el código QR que se imprimió en la hoja
   que contiene el mapa original para mostrarlo como una capa de
   imagen alineada al lugar específico que corresponde esa porción de
   mapa. De esta forma con JOSM podemos simplemente ir dibujando sobre
   nuestro mapa escrito y que quede perfectamente alineado.

   .. figure:: osm-walking-papers.thumbnail.jpg
      :target: osm-walking-papers.jpg
   
      Utilizando mi mapa escrito como fondo de JOSM
   
El resultado de todo esto se puede ver en un mapa comparativo de
Capilla del Monte mostrado en Google Maps y OSM:

.. figure:: mapa-comparativo.thumbnail.jpg
   :target: mapa-comparativo.jpg

   Arriba: Google Maps - Abajo: OSM

Incluso si van a `OSM y ven el mapa más de cerca
<http://www.openstreetmap.org/#map=18/-30.85753/-64.52391>`_, se
pueden apreciar la numeración de algunas calles que pude cargar
también.

Este método de mapeo creo que baja mucho la línea del conocimiento
técnico y ayuda a que gente que conoce de temas como Geografía y/o
Cartografía se anime a salir a recorrer sus calles y a colaborar con
un proyecto *tecnológico* con poco o ningún conocimiento en la parte
técnica :)
