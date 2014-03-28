.. link:
.. description:
.. tags: modulos, modulos, python, python
.. date: 2008/04/29 17:46:18
.. title: #1 Modulo: commands
.. slug: modulo-commands


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2008/04/29/modulo-commands/


Para capturar la salida de un comando generalmente utilizaba el módulo
`subprocess <http://docs.python.org/lib/module-subprocess.html>`__\ de
Python de esta forma:

``>>> from subprocess import Popen, PIPE  >>> Popen(['date'], stdout=PIPE).stdout.read()  'mar abr 29 17:08:17 ART 2008\n'  >>> ``

Hoy viendo el código fuente de un programa
(`pydf <http://sourceforge.net/projects/pydf/>`__) encontré que
utilizaba el módulo
`commands <http://docs.python.org/lib/module-commands.html>`__ y como no
lo conocía me fijé de qué se trataba. Sirve para hacer lo mismo de una
manera más sencilla y legible:

``>>> import commands  >>> commands.getoutput('date')  'mar abr 29 17:04:22 ART 2008'   >>> ``

PD: funciona sólamente en Unix
