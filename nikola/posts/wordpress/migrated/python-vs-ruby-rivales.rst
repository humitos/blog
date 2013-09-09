.. link:
.. description:
.. tags: charla, general, python, python, ruby, ruby, software libre
.. date: 2008/04/24 22:31:09
.. title: ...Python Vs. Ruby... ¿Rivales?
.. slug: python-vs-ruby-rivales

Desde la primer charla del LugLi en la UTN, hace un par de semanas, que
conozco Ruby. Esto quiere decir que ví algo de código, me mostraron
algunas de sus características y me dejó algo impactado.

Este lenguaje es **muy parecido**\ a Python en muchos aspectos. Sin
embargo `Gastón Ramos <http://gastonramos.wordpress.com/>`__ me mostró
algunas aspéctos que lo hacen que sea tan bueno como es, y me dejó
regulando en como hacerlo en Python.

Hay mucha gente que o está del lado de Ruby o de Python, y ni siquiera
quieren mirar al costado para compararlos, son cerrados y hasta incluso
rivales. Después de un tiempo le propuse hacer algunas comparaciones un
poco *más profundas* y no que quede solo de palabras, asique decidimos
escribir un par de post al respecto. `Este es el primero de
él <http://gastonramos.wordpress.com/2008/04/19/snakes-and-rubies/>`__,
la `respuesta de
Juanjo <http://www.juanjoconti.com.ar/2008/04/19/serpientes-y-rubies/>`__
y ahora tiro algunas diferencias entre ellos.

Python
------

#. Tiene strings inmutable
#. Lo métodos privados comienzan con __ (doble guión bajo)
#. Los bloques se delimitan con la identación y : (dos puntos)
#. Tiene __getattr__()
#. La sobrecarga de operadores se define como un método especial
   (comienza y termina con __). def __add__(self) para redefinir
   la suma.
#. No tiene constantes
#. InputRaw con r"C:\\Mis Documentos"
#. Insertar una variable en un texto al estilo C: "Mi variable es: %s" %
   (cadena.upper())
#. Necesita paréntesis para llamar a un método
#. True, False, None, elif, import
#. Acceso dirécto a las variables de una instancia mediante el operador
   . (punto)
#. if __name__ == '__main__': verifica si es el archivo
   principal
#. Tiene un guía excepcional para todo programador: import this
#. Docstring utilizados para brindar ayuda con help()
#. Las funciones son objetos y puedo crear una referencia a ellas

Ruby
----

#. Tiene strings mutables
#. Los métodos privados van después de private
#. Los bloques se delimitan con end's statements
#. Tiene method_missing
#. La sobrecarga de operadores es def +(), para redefinir la suma por
   ejemplo
#. Tiene constantes
#. InputRaw con 'C:\\Mis Documentos', (comillas simples)
#. Insertar una variable dentro de una cadena al estilo Template (de
   Django, por ejemplo): "Mi variable es #{variable.capitalize}
#. No necesita paréntesis para los métodos, los atributos comienzan
   luego del espacio
#. true, false, nil, elsif, require
#. Tengo que definir cuales variables son públicas una por una
#. if __FILE__ == $0 verifica si es el archivo principal
#. No tiene un guía built-in
#. Los docstring se utilizan cuando se llama al comando: rdoc
#. Hasta ahora, no pude guardar la referencia a una función en una
   variable

Éstas son algunas de las diferencias que encontré a simple vista en
Python y Ruby, pero lo que más me interesa mostrar es **cómo hacer**
algo en un lenguaje utilizando alguna particularidad del mismo, que
permita que sea super sencillo o que diréctamente en el otro no se pueda
realizar de "*ninguna forma*\ ".

Vamos a ver que sale de todo esto. ¿Seguiré con Python o me pasaré a
Ruby? **¡CHAN!**
