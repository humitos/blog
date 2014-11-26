.. link:
.. description:
.. tags: python, módulos
.. date: 2008/05/20 01:15:15
.. title: #2 Modulo: bisect
.. slug: modulo-bisect


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2008/05/20/modulo-bisect/


El módulo `bisect <http://docs.python.org/lib/module-bisect.html>`__
sirve para **mapear** números dentro de un rango con algo. Por ejemplo
si quiero indicar **qué tan grande**\ es un número con palabras, podría
hacer algo así::

  >>> from bisect import bisect
  >>> grado = ['muy chico', 'chico', 'mediano', 'grande', 'muy grande', 'gigante']
  >>> rango = [5, 20, 100, 1000, 10000]
  >>> def tamano(numero):
  ...   return grado[bisect(rango, numero)]
  ...
  >>> tamano(25)  'mediano'
  >>> tamano(-5)  'muy chico'
  >>> tamano(156)  'grande'
  >>> tamano(1056)  'muy grande'
  >>> tamano(26542)  'gigante'
  >>>

Lo que está haciendo es ver dónde cae el número que le paso, y
devolviéndome la posición de la lista (*grado*) en la que cae ese
número. Ésto puede ser muy útil para hacer comprobaciones de rango, en
vez de repetir muchas líneas con::

  if 5 <= numero < 20:
  ...    return 'chico'
  elif 20 <= numero < 100:
  ...    return 'mediano'

Fuente: la `documentación del
módulo <http://docs.python.org/lib/module-bisect.html>`__.
