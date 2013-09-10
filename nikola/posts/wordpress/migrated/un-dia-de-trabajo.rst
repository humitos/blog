.. link:
.. description:
.. tags: arte, dibujos, proyectos, software libre
.. date: 2012/07/19 22:20:24
.. title: Un día de trabajo...
.. slug: un-dia-de-trabajo

El mes pasado empecé un curso de edición de contenido audiovisual que se
dicta semanalmente: "`Odisea en el
Taller <https://analisisdigital.com.ar/noticias.php?ed=1&di=0&no=164362>`__\ ".
La idea de este curso es experimentar en todo lo que se pueda; en clases
y fuera también. Está bueno porque es bastante informal, está dictado
por gente jóven y pila y además en cada encuentro circula mucha
información por los aires. Aparecen muchas puntas y estimula los
sentidos.

La clase pasada vimos los inicios del cine, las primeras filmaciones,
las características que éstas tenían, los primeros efectos especiales
(artesanales, recortando y pegando cintas, etc). Nos tiraron unas puntas
como `The Lumiere Brothers' - First films
(1895) <http://www.youtube.com/watch?v=4nj0vEO4Q6s>`__ y la idea para la
clase de hoy era hacer algo "similar": a cámara fija y documentando la
realidad, en pocas palabras.

Como no tuve tiempo durante toda la semana, recién hoy cerca del medio
día me pude poner a ver algo y salió ésto:

.. media:: http://www.youtube.com/watch?v=2H0KY-Xd0T4

Como no tengo cámara para filmar, improvisé algo con la cámara
fotográfica y **gphoto2**, algo que aprendí a usar en el
`PyCamp <http://humitos.wordpress.com/2012/07/15/pycamp-2012/>`__
gracias a Joac y a perrito666. Entonces, ubiqué el trípode, conecté la
cámara por USB a la computadora y le dije que saque una foto cada 2
segundos con éste comando:

.. code:: bash

    gphoto2 --capture-image-and-download --interval 2

Eso estuvo sacando fotos durante un buen rato. Capaz que un poco más de
una hora. Una vez que había reunido todas esas fotos busqué una forma de
hacer un video con ellas. Probé varias cosas, cantidad de fotogramas por
segundos y demás. Terminé usando **mencoder** para hacerlo:

.. code:: bash

    mencoder "mf://*.JPG" -mf fps=8 -o output.avi -ovc lavc \
             -lavcopts vcodec=msmpeg4v2:vbitrate=1800

Luego, busqué alguna forma de meterle una "tapa frontal" y una "tapa
trasera". Agarré el **gimp**, me "diseñé" algo y multipliqué ese archivo
por 16 con nombres consecutivos, así me los agarraba el *mencoder* y
listo! Ya tenía el video terminado, o casi: le faltaba el audio. Para
eso, me puse a pensar algunas cosas: "una música que no diga nada".
Pensé un rato, agarré la guitarra, toqué por unos momentos, enchufé
todo, puse a grabar en el \ **audacity** y le dí click en **Play** al
video: "qué salga lo que tenga que salir". Después junté el audio y el
video con éste comando:

.. code:: bash

    ffmpeg -i input.avi -i new_audio.ogg -vcodec copy -acodec copy \
           -acodec copy final.avi

¡Tengo mi primer *obra* audiovisual Libre, hecha con Software Libre!
