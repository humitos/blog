.. title: Crear mosaico de fotos
.. slug: crear-mosaico-de-fotos
.. date: 2015-12-30 22:25:08 UTC-03:00
.. tags: foto, script, python, twitter, mosaico, perú, huacho
.. category: 
.. link: 
.. description: 
.. type: text

En estos días he estado preparando la charla de `Argentina en Python
<https://argentinaenpython.com/>`_ que voy a dar en `@PyCaribbean
<http://pycaribbean.com/>`_ en Febrero de 2016. En uno de los slides
quería agredecer el apoyo que hemos recibido de toda la comunidad y
para eso se me ocurrió poner una foto de un mosaico de todas las
fotitos de perfiles de los seguidores de la cuenta `@argenpython
<https://twitter.com/argenpython>`_ de Twitter.

Entonces, me puse a trabajar en eso.

.. sidebar:: Rockeala con fades!

   Para poder ejecutar ese comando lo recomendado siempre es crear un
   `virtualenv` y luego instalar la biblioteca `twitter` mediante
   pip. Sin embargo, te recomiendo que le pegues una mirada a `fades
   <https://github.com/PyAr/fades>`_ que te permite hacer todo eso sin
   que te des cuenta y en un solo comando:

   .. code:: bash

      fades -d twitter -x twitter-follow --oauth argenpython > "argenpython.followers.txt"

   :-d: le indico los paquetes que quiero instalar
   :-x: le digo que comando quiero ejecutar una vez instalado esos
        paquetes en el virtualenv automágicamente creado por fades

   Fácil, ¿no?

Primero, busqué un script que había venido utilizando cuando estaba
buscando herramientas para crear `YourReminder
<https://github.com/humitos/your-reminder>`_ (un programador de tuits
automáticos) para obtener todos los seguidores de una cuenta en
particular. Usé la biblioteca `twitter
<https://github.com/sixohsix/twitter>`_:

.. code:: bash

   twitter-follow --oauth argenpython > "argenpython.followers.txt"

Eso me dejó un archivo de la pinta::

  b'thehandro'
  b'raviol'
  b'AlvaroAnguix'
  b'rddebona'
  b'kragen'
  ...

Luego, quería buscar todas las fotos de perfil de los usuarios que
aparecen en ese txt. Para eso me hice este pequeño script en Python
que accede a todas las urls de esos usuarios e imprime el link a la
foto en la pantalla:

.. code:: python

   import re
   import sys
   import requests  # fades
   from bs4 import BeautifulSoup  # fades

   for user in open(sys.argv[1], 'r').readlines():
       url = 'http://twitter.com/{}'.format(user[2:-1])
       data = requests.get(url).content
       soup = BeautifulSoup(data)
       img = soup.find('img', {'class': 'ProfileAvatar-image'})
       print(img.get('src'))

Ejecutamos (obvio, con fades!):

.. code:: bash

   $ fades get_twitter_profile_pics.py argenpython.followers.txt

   https://pbs.twimg.com/profile_images/673314332340539393/lSKlxZ7r_400x400.jpg
   https://pbs.twimg.com/profile_images/378800000304367652/2fb693020239400ff0062b15034890e3_400x400.jpeg
   https://pbs.twimg.com/profile_images/676336395141672960/mB8x63HP_400x400.png
   ...

Ahora, teniendo todas las urls de las fotos de los perfiles, solo me
quedaba bajarlas y hacer el mosaico. Mientras hacía este script de
Python `ya había preguntado por Twitter como hacer el mosaico
<https://twitter.com/reydelhumo/status/681274719425966080>`_ y había
obtenido una respuesta muy acertada a la cual finalmente modifiqué un
poquito y fue lo que terminé usando.

Para bajar las fotos tenía dos caminos. Escribir algo en Python y
lidiar programando, o pasarle toda esta basura a quien más sabe del
tema: *wget*

.. code:: bash

   fades get_twitter_profile_pics.py argenpython.followers.txt | xargs wget -c

Mientras esperaba que se bajen todas las fotos, me puse a leer las
respuestas de Twitter y leer la documentación de `convert
<http://www.imagemagick.org/script/convert.php>`_ y `montage
<http://www.imagemagick.org/Usage/montage/>`_ para finalmente terminar
utilizando `montage` de esta forma:

.. code:: bash

   montage ./*.{jpg,JPG,jpeg,png,gif} -tile 35x -geometry 96x96+0+0 -quality 90 ahlapelotita.jpg

Eso, finalmente, me llevó al resultado que necesitaba:

.. figure:: ahlapelotita.thumbnail.jpg
   :target: ahlapelotita.jpg

   Mosaico de imágenes de perfiles de los seguidores de @argenpython


Y eso, ¡gracias a todos ustedes por el aguante!
