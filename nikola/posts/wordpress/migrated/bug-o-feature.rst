.. link:
.. description:
.. tags: general
.. date: 2010/11/08 12:30:51
.. title: ¿Bug o feature?
.. slug: bug-o-feature

Eso! Entré en una discusión con mi PM del proyecto en el que estoy
trabajando y salió esta duda. El problema es este:

    De alguna forma necesitamos refrescar la página que está viendo el
    usuario porque otra persona hizo una actualización sobre la misma.

El caso que estamos barajando es bastante sencillo porque sólo hay dos
personas en juego no más y las posibilidades de actualizar la página es
por turno, osea que no la pueden actualizar al mismo tiempo los dos
usuarios.

Tiré la posibilidad de chequear con Ajax si el otro usuario había hecho
una modificación y si es así refrescar la página. Entonces mi PM me
dice: "La idea de Ajax en estos casos es refrescar sólo el pedacito de
página que cambió, pero si se complica mucho, lo dejamos así nomás sin
refrescar". Bueno, seguimos charlando y decidimos que no valía la pena,
era demasiado complicado para lo boludo que era (no era estrictamente
necesario).

Después de un rato le digo: "Che, y si verificamos con Ajax y de ser que
tenemos que refrescar... refrescamos toda la página y listo. Así es
mucho más fácil y sale en dos patadas :)". A lo que él contestó: "Eso es
eun Bug hecho Feature" y me mandó esta imágen:

|image0|

Y sí, posta:

    "Un Feature no es más que un Bug disfrazado"

.. |image0| image:: http://files.myopera.com/freejerk/files/bug-feature.jpg
   :target: http://files.myopera.com/freejerk/files/bug-feature.jpg
