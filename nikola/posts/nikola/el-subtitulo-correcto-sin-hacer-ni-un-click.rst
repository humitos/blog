.. title: El subtítulo correcto sin hacer ni un click
.. slug: el-subtitulo-correcto-sin-hacer-ni-un-click
.. date: 2016-01-13 01:29:11 UTC-03:00
.. tags: kodi, subtitulos, subliminal, python, fades
.. category: 
.. link: 
.. description: 
.. type: text

¡Me cansé! Siempre me hichó un poco las bolas tener que ir a `subdivx
<http://subdivx.com/>`_ para buscar el subtítulo correcto para el
video que quería ver, bajar ese `.rar` horrible, descomprimirlo y
probarlo para ver si estaba bien sincronizado. Eso, no solo que
llevaba un rato, sino que *encima* a veces estaban mal sincronizado y
puteaba.

Hoy, en primer lugar uso `Kodi <http://kodi.tv/>`_ para reproducir
videos en un TV y también en la notebook. Además, de ser re-cool, me
permite utilizar mi celular con `Yatse <http://yatse.tv>`_ como
control remoto y lo veo chocho tirado desde la cama. Además, en 2 o 3
swipes me permite bajar el subtítulo del video que estoy viendo desde
un par de sitios en la web.

Así y todo, todavía eso me parece engorroso. Por eso es que *encontré*
algo más fácil y mejor aún: `subliminal
<https://pypi.python.org/pypi/subliminal>`_. Así lo uso:


.. code:: bash

   fades -p python2 -d subliminal==1.1.1 -x subliminal download -v \
     -p addic7ed -p opensubtitles -p podnapisi -p thesubdb -p tvsubtitles \
     -l en -l spa <ejemplo.mp4>

:-v: para que me muestre el debug del subliminal y ver si algo falló
:-p: indica desde qué fuentes bajará los subtítulos
:-l: lenguaje del subtítulo

Le pongo en Español e Inglés porque muchas veces no encuentra ningún
subtítulo en Español y entonces, ante la necesidad, prefiero verlo con
subs en Inglés. De paso cañazo, aprendo algo nuevo.

Pero otra vez, para cada archivo del que quiero un sub tengo que
ejecutar este comando: ¡eso suena a script!

.. code:: bash

   #!/bin/bash
   
   # Download subtitles from all movies in a directory
   MOVIE_TYPES="*.mp4 *.avi *.mkv"
   FADES_BIN=/home/humitos/fades/bin/fades
   PATH_MOVIES_1=$1

   for MOVIE_TYPE in $MOVIE_TYPES; do {
     find "$PATH_MOVIES_1" -name $MOVIE_TYPE -type f -print | \
     xargs -I '{}' $FADES_BIN -p python2 -d subliminal==1.1.1 -x subliminal download -v \
      -p addic7ed -p opensubtitles -p podnapisi -p thesubdb -p tvsubtitles \
      -l en -l spa \
      '{}'
   }; done

Y lo utilizo así:

.. code:: bash

   download_subtitles.sh /media/Toshiba/series

Esto lo que hace es buscar en el PATH que le paso como primer
argumento todos los archivos `.mp4`, `.avi` y `.mkv` de forma
recursiva y para cada uno de los archivos ejecuta el comando que
descarga el subtítulo.

¿Cómo funciona? ¡Ni puta idea, pero rockea!
