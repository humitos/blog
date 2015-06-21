.. title: OSMTracker on the road
.. slug: osmtracker-on-the-road
.. date: 2015-06-21 02:23:45 UTC-03:00
.. tags: argentina en python, openstreetmap, osmtracker, viaje
.. category: 
.. link: 
.. description: 
.. type: text


Mapear mientras vas en el auto está completamente prohibido. Si bien
no hay ninguna ley que lo prohiba, es altamente peligroso. Pero claro,
cuando vas con un acompañante todo es mucho más fácil: esa persona
puede ir mapeando.

Hasta ahí, genial. Pero luego te das cuenta que está todo el tiempo
presionando el botón de "Grabar Voz" y menciona todo lo que pasa a
nuestro al rededor. También, cada tanto se equivoca, presiona otro
botón sin querer y así se pierde de mapear algunas cosas. Además, todo
el tiempo mira el celular y también lo acerca a la boca para
*hablarle* y así que la grabación salga mejor.

¡Eso ya es cosa del pasado!

.. TEASER_END

OSMTracker_ soporta crear nuestros propios layouts `haciendo un
pequeño archivo XML
<https://code.google.com/p/osmtracker-android/wiki/CustomButtonsLayouts>`_
muy sencillo. Así que, me puse manos a la obra y me hice un layout que
lo único que tiene es un botón que ocupa toda la pantalla y que es
super accible para presionar: no hay otra cosa. Entonces, es
simplemente *hacer tap* en la pantalla.

.. figure:: one-big-button.thumbnail.png
   :target: one-big-button.png
   :width: 50%

   Mi propio layout de un solo botón


.. listing:: osmtracker-on-the-road/driving.xml xml

Este archivo hay que copiarlo en la carpeta "layouts" (hay que
crearla) dentro del directorio de "osmtracker" en el celular. Luego,
hay que ir a las opciones de OSMTracker para activar este layout.

Además, si a eso le sumamos unos auriculares *manos libres* (esos que
tienen micrófono) ya te queda perfecto. No solo no tiene que mirar más
el celular, sino que tampoco lo tiene que acercar a la boca para
hablarle

.. _osmtracker: http://wiki.openstreetmap.org/wiki/OSMtracker_%28Android%29
