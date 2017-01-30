.. title: ¡No más Ads en Spotify!
.. slug: no-mas-ads-en-spotify
.. date: 2016-10-29 22:12:47 UTC-03:00
.. tags: ads, spotify, python
.. category: 
.. link: 
.. description: 
.. type: text

En Febrero probé Spotify en mi máquina por primera vez. No entré en
Premium ni nada, simplemente me creé un usuario como buen hijo de
vecino y empecé a ver qué era eso de lo que la gente tanto
hablaba. Busqué mis discos favoritos y empecé a utilizarlo de la misma
forma que lo hacía con mi música offline.

Un mes después: nada del otro mundo. Simplemente abría el cliente de
Linux, seleccionaba algún disco de los que tenía guardado y lo
reproducía de forma completa. Sin embargo, tenía una desventaja con
respecto a la música offline que yo tenía en mi computadora: ¡las
publicidades!. Cada 3 o 4 canciones del disco que estaba escuchando,
me aparecía una publicidad que *nada que ver* con lo que a mi me puede
gustar. Probapagandas de telefonías, recitales de reggaetón y demás
cosas que *teniendo mis gustos musicales* en su base de datos, no
tenían ningún sentido hacerme escuchar eso a mí.

Durante unos días pensé que podría pagar para quitar esos
anuncios. Investigué un poco y vi que pagando, además de quitar los
anuncios te dejaban tener música offline y también más opciones para
la aplicación del celular. Ninguna de las cosas *extras* me llamaron
la atención.

A la semana siguiente, me cansé de escuchar esa basura y sin pensarlo
me fui a comprar el servicio Premium. Intenté usar PayPal y tuve un
problema. Itenté de nuevo unas horas más tarde y lo mismo. Pensé un
rato... pero nada vino a mi mente.

Pasaron algunos días, y cada vez que salía una publicidad pensaba en
algo. Me tomaba esos 30 segundos de cada publicidad para encontrar una
solución...

    El 5 de Abril tuve una idea: quería *realmente* quitar los
    anuncios, pero ahora *sin pagar* ya que por ese camino no había
    tenido suerte y no iba a parar hasta lograrlo. Estaba decidido.

Hice un *brainstorming solo* y llegué a audiodiff_, una librería en
Python para comparar archivos de audio. La idea parecía ser simple al
principio: escuchar lo que viene de Spotify y cada vez que se detecte
un silencio (el que hay entre tema y tema -o tema y anuncio) comparar
a máxima velocidad lo que empieza a reproducirse con todos los
anuncios que previamente había guardado en disco. Ese día `le escribí
un tuit a fisa
<https://twitter.com/reydelhumo/status/717459145205612544>`_ porque
pensé que le podría interesar.

.. TEASER_END

Mucho tiempo después, a fines de Agosto, hice mis primeras pruebas con
esta librería. Si bien es extremadamente fácil de usar, es
increíblemente lenta. Además, solo trabaja sobre archivos y no
encontré la forma de pasarle un streaming directamente. Entonces,
pensé que podría crear un buffer de unos 45 segundos e ir trabajando
sobre eso, cortar los audios, analizarlos, ver qué tienen y decidir si
reproducirlo o no dependiendo de si es una publicidad. Tiré un par de
horas ahí y no llegué a nada útil.

Daba vueltas y pensaba opciones. Pensé en ver si yo podría ser capaz
de escribir algo más rápido que `audiodiff` utilizando numpy_ quizás,
y de paso era una buena excusa para aprenderlo...

En esos días *me dí cuenta* que cada vez que el cliente de Spotify de
Linux cambiaba de tema, utilizaba el nombre de esa canción/artista
como título de la ventana del programa, y que además también lo hacía
para los anuncios. *¡Voilá!, acá está la papa* -me dije.

    Voy a comprobar el título de la ventana cada segundo, analizarlo y
    compararlo contra los artistas que escucho normalmente y si no
    está dentro mi lista: ¡silencio!

La idea era excelentemente simple. Simple de verdad, no como la
primera. Me puse manos a la obra, y en menos de 30 minutos tenía el
primer prototipo y funcionaba para la mayoría de los casos. Durante
las primeras horas de prueba encontré algunos patrones en los nombres
de las publicidades y también de las canciones que escuchaba.

* muchas publicidades están TODAS EN MAYÚSCULAS
* otras tantas tienen una sola palabra
* la mayoría de las canciones se muestran como "Artista - Canción"

Implementé estas pequeñas reglas y retoqué un poco lo que había hecho
anteriormente y llegué a una versión muy estable y que funciona en el
95% de los casos. ¿Porqué en un 95%? Esto es debido a que hay discos
en vivo o de múltiples artistas donde la última regla de las
anteriores no se cumple. Por ejemplo, "Soda Stereo - Persiana
Americana - Gira Me Verás Volver".

A raíz de esto creé:

* una lista blanca con los artistas que *siempre* quiero escuchar
* una lista negra con algunos nombres de publicidades que no cumplen
  las reglas básicas

El resultado de esto es este pequeño programa escrito en Python
(`spotify-noads.py
<https://gist.github.com/humitos/bfc241857b1f87576ca6355ab7653ad0>`_)
que no hace ni más ni menos que eso que mencioné antes: si detecta una
publicidad, pone mute en tu sistema de audio, cuando termina la
publicidad y empieza una canción, lo quita.

Luego de las primeras horas de probarlo, lo quise dar a conocer y
escuchar algunas opiniones. Para eso, `publiqué este tuit
<https://twitter.com/reydelhumo/status/775374606400122883>`_ y recibí
diferentes opiniones. Algunos a favor, otros en contra, otros que
primero estaban a favor y luego se dieron cuenta que "le estamos
cagando el modelo de negocio a Spotify" y demás.

Personalmente, tengo opiniones encontradas. No estoy cien por ciento
seguro de estar de un lado o del otro. Algunos pensamientos:

* hemos descargado música utilizando torrent y p2p anteriormente
* hemos rippeado cd's de nuestros amigos
* si las publicidades tuvieran algo que ver conmigo...
* utilizamos bloqueadores de ads en las webs
* escuchar heavy metal y que salte un reggaeton, nah
* pagar por múltiples características cuando necesitás/querés solo una
* frente a un TV ponemos mute cuando viene la publicidad
* la publicidad para Spotify se sigue mostrando/escuchando
* de esta forma Spotify me sigue poniendo publicidades visuales en mi cliente [#]_

Además de dar a conocer este pequeño script, me gustaría que utilicen
los comentarios de este post para mostrar su postura (en contra o a
favor) sobre esta metodología y expliquen sus razones.
  
  
.. _audiodiff: http://audiodiff.readthedocs.org/
.. _numpy: http://www.numpy.org/

.. [#] el helado en palito que venden acá en Ecuador es buenísimo ;)
