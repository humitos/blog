.. link:
.. description:
.. tags: google, python
.. date: 2011/03/12 19:00:34
.. title: Google no respeta el PEP8
.. slug: google-no-respeta-el-pep8


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2011/03/12/google-no-respeta-el-pep8/


Sí loco, estoy trabajando con el SDK de Python de Google App Engine y
veo que usan 2 espacios en vez de 4 para tabular. ¡Todo mal!

Además, le paso el pep8 a **dev_appserver.py** y recibo esto:

``  $ pep8 dev_appserver.py  dev_appserver.py:45:3: E111 indentation is not a multiple of four  dev_appserver.py:162:1: E303 too many blank lines (3)  dev_appserver.py:214:1: E302 expected 2 blank lines, found 1  dev_appserver.py:344:80: E501 line too long (80 characters)  dev_appserver.py:1334:15: E225 missing whitespace around operator  dev_appserver.py:1445:22: E202 whitespace before ']'  dev_appserver.py:2151:23: W602 deprecated form of raising exception  $ ``

Estoy... *INDIGNADO*!
