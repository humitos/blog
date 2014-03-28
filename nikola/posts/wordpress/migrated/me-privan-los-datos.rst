.. link:
.. description:
.. tags: facultad
.. date: 2008/06/05 00:03:44
.. title: Me privan los datos
.. slug: me-privan-los-datos


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2008/06/05/me-privan-los-datos/


Es lamentable. Hoy después de hablar lo que publiqué en el post anterior
con la profesora, un amigo le preguntó que forma tenía de exportar la
base de datos para poder trabajar en su casa (estamos haciendo 2 guías
de 20 ejercicios cada una de sentencias SQL). Antes me había preguntado
a mí y no tenía ni idea ya que estaban usando Oracle.

    A: Le preguntaba si no hay una forma de exportar la base de datos o
    algo para poder llevármela a mi casa y poder trabajar ahí.

    P: No porque el profesor no la puso disponible a la base de datos.

    A: Ah, ¿No está disponible?, yo le decía porque no llegamos a hacer
    todos los ejercicios.

    P: Mmm... No, la única opción que tienen es venir a trabajar acá al
    laboratorio

También está en OGG, y es patético. Asique bueno, mi amigo se puso a
hacer **SELECT \* FROM tabla;**\ de las 8 tablas que había y copiaba eso
a un ".txt" para que yo me lleve a mi casa y luego haga un script que
levante eso y lo vuelque en una base de datos.

`Recién lo
termino <http://grulicueva.homelinux.net/~humitos/blog/me-privan-los-datos/cargar_bd.py>`__,
aunque no está muy bien hecho, ya que algunos atributos estaban
separados por 2 espacios y otros por N, quedó más o menos... A veces
tuve que agregarle campos vacíos (le puse \*\* para identificar cuales
eran).

Igualmente, no entiendo muy bien todavía, y no tengo ganas de ponerme a
ver cómo son tampoco, son las claves foráneas y las claves primarias.
Aunque tengo el diagrama, este se entiende bastante poco.

*... dentro de poco no voy a poder compartir con nadie lo que aprendo en
la facultad, espero realmente que esto cambie ...*
