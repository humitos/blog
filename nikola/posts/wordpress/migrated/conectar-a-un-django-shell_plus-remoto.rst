.. link:
.. description:
.. tags: django, hosting, internet, python, ssh, trabajo
.. date: 2012/02/24 11:57:19
.. title: Conectar a un Django shell_plus remoto
.. slug: conectar-a-un-django-shell_plus-remoto


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2012/02/24/conectar-a-un-django-shell_plus-remoto/


¡Acabo de utilizar la cabeza para algo! Todavía estoy emocionado. Creo
que esto va a facilitarle las cosas a varios y a reducir ese tiempo
tedioso de conectarse al servidor "para probar algo" o "ver qué tiene la
db" o etc.

La cosa es así, ¿cuántas veces nos logueamos por ssh al servidor para
luego hacer Ctrl + R, empezar a tipear **shell_plus** y darle Enter (si
es que todavía quedó en el history y lo tipeamos con el path absoluto)
sino hacer \ *cd* hasta la carpeta dónde tenemos el proyecto de Django y
finalmente ejecutar *./manage.py shell_plus* con una previa activación
del virtualenv.

Wow! Suena tedioso hasta tener que explicarlo. Hoy traigo **la
solución**. "Waaaa, tengo miedo nene"

Es simple, seguimos utilizando SSH pero evitamos todos los pasos antes
dichos con sólo un comando:

    ssh user@remote-host.com -t -C "source
    ~/path/to/virtualenv/bin/activate && python
    ~/path/to/django/project/manage.py shell_plus"

La opción **-C** es para que comprima la entrada y la salida y la **-t**
es para que se vean bien los colores de la salida de *ipython* en mi
caso (ya que lo tengo instalado).

Me zarpé! :D
