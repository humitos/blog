.. title: Skype sin/con sonido en Xubuntu 14.04
.. slug: skype-sincon-sonido-en-xubuntu-1404
.. date: 2014/05/22 15:55:40
.. tags: skype
.. link: 
.. description: 
.. type: text

Al actualizar mi Notebook a Xubuntu 14.04 LTS una de las cosas que
noté es que no me andaba bien el Skype y, como es algo que 'a veces'
necesito usar en el trabajo estuve renegando un poco hasta que... Les
dije que usemos hangout porque no me funcionaba.

Básicamente, el problema era que no tenía sonido. Ninguno. Ni al
iniciarlo, ni al conectarse un contacto, ni al hablar ni al recibir
una llamada... Nada.

Después de un tiempo, busqué de nuevo en Google y caí en la
solución. De hecho, mucho más fácil de lo que me pensaba.

.. code:: bash

   #!/bin/bash

   # From:
   # http://askubuntu.com/questions/453515/skype-14-04-no-sound-output-in-conversations

   # Skype is not working properly in Xubuntu 14.04 LTS (no sound at all). After
   # running Skype with this configuration the issue dissappears...

   env PULSE_LATENCY_MSEC=30 skype

A eso lo puse dentro de `~/bin/skype-fixed.sh` y listo, ejecuto Skype
llamando a este archivo.
