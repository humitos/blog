.. title: Compartir videos con tu co-equiper
.. slug: compartir-videos-con-tu-co-equiper
.. date: 2015-08-12 16:22:44 UTC-03:00
.. tags: script, shell, youtube, video, audio
.. category: 
.. link: 
.. description: 
.. type: text

Viajamos mucho y muchas veces tenemos poca conectividad a
internet. Entonces, necesitamos una forma de poder descargar la mayor
cantidad de datos de internet cuando *sí tenemos* internet.

Para eso, hemos implementado varias ideas pequeñas que nos permiten
trabajan Offline y sincronizarnos cuando estamos Online. Por ejemplo,
muchas veces queremos bajar videos para ver cuando no tenemos
internet.

Acá viene la cuestión. Siempre pasa que nos decimos: "¿Bajaste el
video que te pedí?" y siempre tiene la misma respuesta: "¡Uh! Me re
colgué". Finalmente, nunca tenemos nada para ver.

¡Basta! ¡Me cansé! Necesito *hacer un programa* que me ayude. Para eso
combiné: `Dropbox <http://dropbox.com/>`_ + `youtube-dl
<https://rg3.github.io/youtube-dl/>`_ + bash magic. Primero, creamos
un archivo llamado `urls-videos.txt` y lo compartimos con Dropbox
entre los dos. Cada uno agrega, cuando quiere/puede, un link al video
que quiere bajar (uno por línea). Luego, en mi máquina me hice un
one-line-bash-script que lo que hace es:

#. Tomar la primera línea
#. Bajar el video
#. Borrar la primera línea (si tuvo éxito la descarga)
#. Volver al primer paso

El script:

.. code:: bash

   URLS=urls-videos.txt
   youtube-dl --restrict-filenames --retries 50 --continue \
              --write-sub --sub-lang "en,es" --batch-file $URLS \
              --exec "tail -n +2 $URLS > /tmp/urls.txt ; mv /tmp/urls.txt $URLS ; ls"

La descripción:

:--restrict-filenames: restringe el nombre de los archivos a algo más compatible (sin caracteres raros)
:--retries 50: intenta un máximo de 50 veces
:--continue: resume la descarga en caso de haberse cancelado por cualquier motivo
:--write-subs: escribe los subtítulos en un archivo
:--sub-lang: selecciona solo los subtítulos de los lenguajes "English" y "Español"
:--batch-file: utiliza un archivo como entrada de urls a descargar
:--exec: (acá está *la magia*) mediante `tail -n +2` elimino la
         primera línea del archivo de urls y lo guardo en un archivo
         temporal. Luego, muevo ese archivo temporal al archivo
         original de urls (`urls-videos.txt`). Finalmente, pongo un
         `ls` porque youtube-dl concatena el nombre del archivo recién
         descargado, y como yo no quiero hacer nada con ese archivo,
         simplemente lo muestro en pantalla.

Así, cuando tengo internet se actualiza (con toda la magia de Dropbox)
el archivo `urls-videos.txt` que yo modifiqué en mi máquina y también
el que modificó Johanna. Después yo corro ese simple script y comienza
el proceso.

¡Tenemos videos para ver! (sobre todo charlas TEDx)
