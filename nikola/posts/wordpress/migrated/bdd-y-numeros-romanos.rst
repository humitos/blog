.. link:
.. description:
.. tags: numeros, python, romanos, software libre
.. date: 2008/04/29 11:33:07
.. title: BDD y Números Romanos
.. slug: bdd-y-numeros-romanos

En la primera y última, hasta el momento, charla del LugLi en la UTN de
Santa Fé Gastón mostró lo que es `BDD <http://behaviour-driven.org/>`__
(Behaviour Driven Development) aplicándolo en su lenguaje favorito (vaya
uno a saber porqué) con `RSpec <http://rspec.info/>`__. Lo que mostró y
como dió la charla fue **fantabuloso**, nos engañó a todos de una forma
increible, yo compraba.

Y finalmente... compré. Ayer me puse a buscar info sobre BDD en Google
pero aplicado a Python, no encontré mucho, al parecer toda esta
*metodología* es demasiado nueva y está muy verde. Finalmente caí en dos
links que salen de la sección implementación de la página oficial de
BDD. Uno se llama
`specipy <http://colus.cafe24.com/hgwebdir.cgi/specipy/>`__, que no
entendí para nada como se usa, ¡no hay doc!. Y el otro es un plugins
para nose, y... justamente **no sé** lo que es que se llama
`pinocchio <http://darcs.idyll.org/~t/projects/pinocchio/doc/>`__.

Seguí leyendo bastante, y preguntando qué me recomendaban hacer en la
lista de PyAr y en el canal. No conseguí ninguna respuesta, no sé si
nadie sabía, no lo utilizan o qué pasó. Después caí en el módulo doctest
de Python, que sirve para **probar comentarios** como si fueran
sentencias dentro del interprete. Está muy piola. Por ejemplo:

::

    def suma(x, y):
      """Esta función devuelve la suma de los
      argumentos x e y
      >>> suma(2,4)
      6
      >>> suma(24,1)
      25
      >>> suma([2],[4])
      [2, 4]
      >>> suma([3], 5)
      Traceback (most recent call last):
      ...
      TypeError: can only concatenate list (not "int") to list
      """

      return x + y

    if __name__ == '__main__':
      import doctest
      doctest.testmod()

Esto lo que hace es, cuando se ejecuta este módulo diréctamente se
**meten** en el intérprete todos los comentarios que empiecen con >>> y
se compara el resultado con lo que está inmediátamente abajo de esa
línea. Si esta coincide, el test es válido.

Ahora para jugar un poco con esto, ya que quería ver cómo se siente
tener que escribir cómo debe funcionar la aplicación y luego escribir el
código, me puse a jugar con un ejercicio interesante: "Convertir números
romandos a enteros, y viceversa". Abrí un archivo nuevo, lo guardé como
.py y empecé a delirar.

Es medio raro escribir algo de texto y ver que no avanzás mucho, pero
después cuando escribís la función ya estás seguro de que funciona :D ,
y no tenés que testearla manualmente, además en una me pasó que metí la
pata y pasé de tener 1 Test Fail a tener 14, lo cual hizo que me de
cuenta enseguida que había hecho cualquier cosa.

Todavía no me acostrumbro bien a hacer esto, a veces me desespero un
poco y empiezo a tirar código a medida que voy haciendo las pruebas, o
bien termino la prueba de una función y enseguida la escribo.

El módulo se puede `descargar de
acá <http://grulicueva.homelinux.net/~humitos/blog/bdd-y-numeros-romanos/roman.py>`__
y un ejemplo de su uso sería algo así.

::

    >>> from roman import Roman

    >>> Roman(2)

    Roman('II')

    >>> Roman('XI')

    Roman('XI')

    >>> Roman(2.5)

    Traceback (most recent call last):
        ...
    ValueError: float number is not support

    >>> Roman('II') + 5

    Roman('VII')

    >>> Roman('XXI') * 2

    Roman('XLII')

    >>> Roman('X') + Roman('XV')

    Roman('XXV')

    >>> Roman('X') - 25

    Traceback (most recent call last):
        ...
    ValueError: result zero or negative

    >>> Roman(25) + Roman(3995)

    Traceback (most recent call last):
        ...
    ValueError: result too long

Ahora bien, para qué carajo sirve sumar y restar números romanos no sé,
si alguien le encuentra alguna utilidad... Bienvenido sea :)
