.. link: 
.. description: 
.. tags: python, software libre, charla, argentina en python, documentación
.. date: 2013/09/17 00:18:06
.. title: Características de Python 2.7-3.3 que no conocía
.. slug: caracteristicas-de-python-27-33-que-no-conocia

Python 2.7 es la última *major release* de la serie 2.x y esto es porque los
desarrolladores de Python están avocados a las versiones de Python 3 más que a
Python 2. Entonces, la idea es poner todo el esfuerzo en Python 3 y mantener
una versión **estable** de Python 2, que esa sería la versión 2.7. Esta versión
tuvo sus *bug-fix releases* hasta el 2012.

.. sidebar:: ¡Muchos más cambios!

    Por supuesto que hay muchísimos cambios más desde la versión 2.7 a la 3.3
    de Python, pero estoy mostrando únicamente las que representan un cambio en
    las herramientas que *usamos* (o uso -al menos) frecuentemente. Hay muchos
    cambios de optimizacion y de cosas más sutiles también, pero creo que en
    esos casos es mejor chequear la documentación oficial directamente.

    Todos los cambios de todas las versiones de Python (en inglés), se pueden
    encontrar en éste link:

    * http://docs.python.org/release/3.3.1/whatsnew/index.html

A continuación voy a mostrar las características nuevas más importantes (de uso
común) desde Python 2.7 y hasta Python 3.3 que no conocía o no estoy habituado
a usar. Además de las que muestre yo, han habido muchas más, incluso en 
cuestiones de *performance*.

.. note::

    En los casos en los que sea necesario, voy a hacer una diferencia marcada
    en los intérpretes de Python 2.7 y 3.3 si es que estos generan una salida
    diferente.

Python 2.7
----------

* Sintaxis para crear un `set` utilizando llaves (`{}`):
  
  .. code:: python

    # Python 2.7
    >>> {1,2,3}
    set([1, 2, 3])
    >>>

  .. code:: python

    # Python 3.3
    >>> {1,2,3}
    {1, 2, 3}
    >>> type({1,2,3})
    <class 'set'>
    >>>

* Diccionarios y comprensión de listas:

  .. code:: python

    >>> {i: i*2 for i in range(3)}
    {0: 0, 1: 2, 2: 4}
    >>>

* Multiples contextos en un solo *with* (with llama a __enter__() y __exit__()
  respectivamente):

  .. code:: python

    with A() as a, B() as b:
        suite

* Diccionario ordenado:

  .. code:: python

    >>> from collections import OrderedDict
    >>> d = OrderedDict([('first', 1),
    ...                  ('second', 2),
    ...                  ('third', 3)])
    >>> d.items()
    [('first', 1), ('second', 2), ('third', 3)]

* Marcador de miles, mediante ",", para números dentro de cadenas de
  caracteres:

  .. code:: python

    >>> '{:20,.2f}'.format(18446744073709551616.0)
    '18,446,744,073,709,551,616.00'

* Nuevo módulo `argparse`_ que reemplaza a `optparse`_ debido a sus
  limitaciones. `argoparse` tiene mejores validaciones que `optparse` ya que
  permite, por ejemplo, espeficar el número de argumentos con un entero, 0 o
  más argumentos utilizando `'*'`, 1 o más argumentos con `'+'` o un argumento
  opcional usando `'?'`. Además, se puede definir un tipo de argumento como
  FileType, el cual se va a abrir automáticamente.

* Vistas de diccionarios. Los métodos de diccionario `keys()`, `values()` y
  `items()`, en Python 3.x devuelven un objeto llamado *view* en vez de una
  lista. Esta *view* es una representación de los valores del diccionario, por
  lo tanto si los valores del diccionario cambian, los valores de la view
  también (en Python 2.7, a esos nombres de métodos hay que anteponerle la
  palabra `view`:

  .. code:: python

    # Python 2.7
    >>> d = dict(a=1, b=2, c=3)
    >>> d
    {'b': 2, 'c': 3, 'a': 1}
    >>> view_keys = d.viewkeys()  # en Python 3 es solo keys()
    >>> view_keys
    dict_keys(['b', 'c', 'a'])
    >>> d['d'] = 4
    >>> view_keys
    dict_keys(['d', 'b', 'c', 'a'])
    >>> 

* El método `str.format()` soporta numeración automática del remplazo de
  campos. Hace que el uso de `str.format()` sea más parecido al uso del
  formateo con %s:
  
  .. code:: python

    >>> 'One: {}, Two: {}, Three: {}'.format(1, 2, 3)
    'One: 1, Two: 2, Three: 3'
    >>> 'One: {}, Two: {}, Three: {three}'.format(1, 2, three=3)
    'One: 1, Two: 2, Three: 3'

* Nueva clase: `collections.Counter`. Es útil para el conteo de datos:
  
  .. code:: python

    >>> from collections import Counter
    >>> c = Counter()
    >>> for letter in 'here is a sample of english text':
    ...   c[letter] += 1
    ...
    >>> c
    Counter({' ': 6, 'e': 5, 's': 3, 'a': 2, 'i': 2, 'h': 2,
    'l': 2, 't': 2, 'g': 1, 'f': 1, 'm': 1, 'o': 1, 'n': 1,
    'p': 1, 'r': 1, 'x': 1})
    >>> c['e']
    5
    >>> c['z']
    0

* Algunas optimizaciones_ que hacen el funcionamiento de Python más rápido.

.. _optimizaciones: http://docs.python.org/release/3.3.1/whatsnew/2.7.html#optimizations
.. _argparse: http://docs.python.org/release/3.3.1/library/argparse.html
.. _optparse: http://docs.python.org/release/3.3.1/library/optparse.html

Python 3.0
----------

* `print` es una función:

  .. code::

    >>> print('The answer is', 2*2)
    The answer is 4
    >>>

* División de punto flotante por omisión:

  .. code:: python

    >>> 3 / 2
    1.5
    >>> 3 // 2
    1
    >>>

* `Texto Vs. Datos`_

* Desempaquetar iterables de forma variable:

  .. code:: python

    >>> (a, *rest, b) = range(5)
    >>> a
    0
    >>> rest
    [1, 2, 3]
    >>> b
    4
    >>>

* Uso obligatorio de `()` en comprensión de listas:
  
  .. code:: python

    # Python 2.6
    >>> [x for x in 1, 2, 3]
    [1, 2, 3]
    >>>

  .. code:: python

    # Python 3.3.1
    >>> [x for x in 1, 2, 3]
    File "<stdin>", line 1
    [x for x in 1, 2, 3]
                 ^
    SyntaxError: invalid syntax

    # Esta es la nueva forma
    >>> [x for x in (1, 2, 3)]
    [1, 2, 3]
    >>>

* Tuplas como parámetros, eliminadas:

  .. code:: python

    >>> def foo(a, (b, c)):
      File "<stdin>", line 1
        def foo(a, (b, c)):
                   ^
    SyntaxError: invalid syntax
    >>>

  .. code:: python

    # Esta es la nueva forma
    >>> def foo(a, b_c):
    ...   b, c = b_c
    ...   print(b, c)
    ... 
    >>> foo(1, (2, 3))
    2 3
    >>>

* `raw_input()` se renombró a `input()`:

  .. code:: python

    >>> raw_input()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'raw_input' is not defined
    >>>

    >>> input()
    Hello, beautiful day!
    'Hello, beautiful day!'
    >>>

.. _Texto Vs. Datos: http://docs.python.org/release/3.3.1/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit

Python 3.2
----------

* Nuevo módulo: `concurrent.futures`. La idea es poder ejecutar varios hilos de
  manera concurrente sin tener que setear un entorno muy grande:

  .. code:: python

    import concurrent.futures, shutil
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:
        e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
        e.submit(shutil.copy, 'src2.txt', 'dest2.txt')
        e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
        e.submit(shutil.copy, 'src3.txt', 'dest4.txt')

* Los objetos `range` ahora soportan `index()`, `count()`, slicing y slicing
  negativo:

  .. code:: python

    >>> range(0, 100, 2).count(10)
    1
    >>> range(0, 100, 2).index(10)
    5
    >>> range(0, 100, 2)[5]
    10
    >>> range(0, 100, 2)[0:5]
    range(0, 10, 2)

Python 3.3
----------

* Entornos virtuales dentro de la librería estándar a través del módulo `venv`_

  .. code:: bash

    humitos@michifus:~$ python3 -m venv myvenv
    humitos@michifus:~$ ls myvenv/
    bin  include  lib  pyvenv.cfg
    humitos@michifus:~$ source myvenv/bin/activate 
    (myvenv) humitos@michifus:~$ deactivate 
    humitos@michifus:~$

.. note::

    Si sabés de alguna característica importante que me olvidé de mencionar,
    avisame a través de los comentarios así la agrego.

*Seguramente de acá salga alguna que otra charlita.*

.. _venv: http://docs.python.org/release/3.3.1/library/venv.html
