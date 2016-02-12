.. title: Crear GIFs de comandos en terminal
.. slug: crear-gifs-de-comandos-en-terminal
.. date: 2016-02-11 22:33:55 UTC-03:00
.. tags: gif, video, terminal, perú, las lomas
.. category: 
.. link: 
.. description: 
.. type: text


Hace un tiempo que tengo curiosidad por saber cómo crean esos
"screencast" de los comandos que van tipeando en una terminal y los
meten en un blog en formato `gif`.

Hoy encontré ttygif_ que te deja crear un GIF a partir de lo grabado
con ttyrec_ -que basicamente permite grabar los comandos que vas
tipeando en la consola y luego reproducirlo con el comando `ttyplay`.

Bueno ttygif_ mientras lo va reproduciendo va grabando una pequeña
imagen de lo que se va mostrando junto con un tiempo en
milisegundos. Luego, ejecutando su comando `concat.sh` te permite
guardar eso en un gif.

Para instalarlo:
	   
.. code:: bash

   sudo apt-get install imagemagick ttyrec gcc
   git clone https://github.com/icholy/ttygif
   cd ttygif
   make

Para usarlo:
   
.. code:: bash

   ttyrec fades-django
   ./ttygif fades-django
   ./concat.sh fades-django.gif

¡Listo!


Aquí en el resultado, muestro fades_ con Django_:

.. image:: fades-django.gif
   :align: center

.. include:: links.rst
			
