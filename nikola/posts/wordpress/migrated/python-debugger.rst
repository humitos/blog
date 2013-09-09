.. link:
.. description:
.. tags: general, python
.. date: 2007/10/15 23:13:31
.. title: Python Debugger
.. slug: python-debugger

Hoy estuve haciendo un poco de todo. Configurando el canal de IRC que
mencioné en el post anterior, buscado plugins para el Kate, viendo
algunos programas, incorporándome en la comunidad Ubuntu, traduciendo
algunos paquetes, etc...

En un momento de la tarde me puse a revivir el Kpaper y a ver porqué no
andaba bien la parte de la interfaz gráfica hecha con PyGtk. Por lo que
me puse a investigar cuál era el problema, miré algunos logs que tenía
archivado en los bookmarks y pregunté en el canal de Ubuntu (#ubuntu-ar)
si alguien se sometía a ser mi beta tester.

Uno se copó (FreeDownload), se bajó el código y le hice hacer algunas
pruebas en su máquina, ya que yo tengo Kubuntu y quería estar seguro que
en Ubuntu andaba. Bue, cómo era de esperar no le funcionó y le pedí que
me pase por favor lo impreso en consola. Me puse a estudiar cuál era el
problema. No lo pude descifrar y no dude en mandarlo a la lista de
`PyAr <http://www.python.com.ar>`__.

No estando seguro de cuál era el problema, mandé el mail. Esto es jodido
porque si no sé qué es lo que pasa es complicado transmitir por email la
pregunta. Lo que yo quería explicar no era nada concreto y no sabía
como, ni por dónde empezar. Pero esto no viene al caso...

Redacté el mail, y envié. Al rato me contestaron con una explicación (no
muy distinta a lo que yo pensaba) pero me sugirieron hecharle un vistazo
al módulo **pdb** que es *Python Debugger*. Asique fuí directo a la
documentación `oficial <http://docs.python.org/lib/module-pdb.html>`__.
Y me encontré con que es para ir parando el programa dónde uno desea. Ni
más ni menos que... "Un debugger!" :) . Buenísimo.

Hice un par de `pruebas <http://www.paste-it.net/3957>`__, *simples*,
sobre el archivo `hello.py <http://www.paste-it.net/3958>`__, para ver
como funciona y si realmente es útil. Después de jugar un rato, encontré
cosas interesantes, cómo por ejemplo, ver en qué parte del código de mi
programa estoy y poder ejecutar código Python ahí mismo.

Con la función "*pdb.set_trace()*\ " le indico al intérprete que debe
frenar en esa línea, y dejarme hacer lo que yo quiera en la consola del
debugger. Yo en el ejemplo que hice puse cuatro puntos en los que quería
que parara, e hice algunas consultas. Utilicé los comandos:

-  **list:** me muestra la porción del código indicando dónde estoy
   posicionado actualmente en el código.
-  **!:** me deja introducir código Python, por lo que yo usé la función
   *print* para mostrar el contenido de las variables que me
   interesaban.
-  **continue:**\ ejecuta el código hasta el próximo *pdb.set_trace()*
   (break point).
-  **next:** continúa la ejecución hasta la próxima línea de la función
   actual.
-  **help:** nos muestra la ayuda de los comandos que podemos utilizar.
-  **where:** indica en qué parte del código estamos parados y muestra a
   línea correspondiente.
-  **whatis:** muestra el tipo de dato de la variable pasado como
   argumento.
-  **args:** indica cuales son los parámetros de la función en la que
   actualmente estamos ejecutando el código.
-  **return:** ejecuta el código hasta que la función actual retorne.

Se puede ir haciendo un seguimiento del código que escribí y de las
pruebas que realicé. Por ahora son muy sencillas, es la primer vez que
veo este módulo y seguro que más adelante le sacaré más provecho.
