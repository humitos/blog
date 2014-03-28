.. link:
.. description:
.. tags: juegos, pygame, python, software libre
.. date: 2007/11/12 19:31:17
.. title: Otro juego de damas
.. slug: otro-juego-de-damas


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/11/12/otro-juego-de-damas/


|image0|"Another Checkers Game" (Otro juego de damas) es el juego en el
cuál me sumé hace un par de semanas. Si bien la idea de hacer este juego
salió allá por las `2das Jornadas de Python en Santa
Fé <http://www.pythonsantafe.com.ar/>`__, de Hugo, Héctor y mía, yo
estuve bastante ausente en este proyecto por mucho tiempo.

Lo mejorcito de esto y lo que más ganas me daban de hacerlo era la
posibilidad de llevar un proyecto de forma remota, que el único medio de
comunicación sea internet. Aparte de trabajar en grupo, lo que conlleva
a discusiones sobre diversos temas y demás.

Por otro lado, un juego de damas implica, nada a bastante de
Inteligencia Artificial, depende qué es lo que se planee hacer. Por
ahora implica **nada**, ya que lo que primero queremos hacer es una
versión que sea jugable por dos humanos, y luego incorporarle todo lo
que es IA.

Cuando `fui a ver Soda
Stereo <http://humitos.wordpress.com/2007/11/05/soda-stereo-buenos-aires-argentina/>`__
a Buenos Aires, me alojé en lo Héctor. Me mostró lo que habían hecho
**la única** vez que se juntaron (bastante vagos de su parte también, no
viven tan lejos ¡che!). Pero igual me sorprendió mucho porque tenía unos
dibujos muy buenos e incluso ya andaba *algo.* Era prometedor al menos.

Al otro día vino Hugo y mostró unos dibujos que había hecho el primo de
unas piezas más infantiles y un tablero distinto, con aspecto a una
playa. Me comentaron que la idea es tener varios estilos de juegos,
varios temas, distintas piezas y tableros. Algunos para chicos. Muy
buena idea.

Aunque Hugo, a mi parecer se quedó con todas las ganas de empezar a
programar entre los tres ;) , yo desistí y les dije que no estaba como
para pensar ni siquiera 2+2. La noche anterior había sido el recital y
Hugo cayó a las **10am** (yo estaba *muerto*\ en vida).

Hablamos de todo un poco, tiramos cuales era las ideas que teníamos cada
uno, Hugo mostró la forma de poder arrastrar y soltar las fichas para
llevarlas de un casillero a otro, y demás.

Cuando volví, les dije que me agreguen `al proyecto de google
code <http://code.google.com/p/acheckersgame/>`__ para que pueda hacer
commits yo también. Me bajé el código y me lo puse a leer, ya que estaba
**en bolas** de cómo funcionaba. "Mejoré" algunas funciones en los días
subsiguientes a lo que me duró la *admiración* de **semejante** juego :)
. Después empecé a ver algo sobre las reglas del juego, movimientos
permitidos, si estoy obligado a comer, etc... Lo cuál no tuvo mucho
éxito en ese momento :(

Hoy al medio día, Hugo envía un mail anunciando que había hecho algunos
cambios en el código. Cuando vi lo que había hecho me dio bastantes
pilas para seguir con lo que estaba haciendo (reglas) y me puse
enseguida (después de terminar unas cositas en Java) con el Juego y sus
reglas.

Actualmente se puede intercambiar entre dos *estilos*. Uno es el clásico
y otro con onda a una playa. Lo bueno de esto es que podés jugar con el
clásico y a mitad de juego cambiarlo al otro, sin perder las posiciones
de las piezas.

Están validados los turnos de los jugadores (no puede mover dos veces el
mismo, y empiezan las blancas), se puede mover solamente a las dos
casillas adyacentes hacia adelante comprobando que esta no esté ocupada
por otra pieza.

No se puede comer una ficha, obligar a comer si es que se tiene la
posibilidad, y un largo etcétera que iremos mejorando con el tiempo.

Algunos screenshots... Y *arribaderchi*

|image1|\ |image2|

.. |image0| image:: http://img232.imageshack.us/img232/4416/p1normalbh1.png
.. |image1| image:: http://img138.imageshack.us/img138/1233/acgbeachrm0.th.png
   :target: http://img138.imageshack.us/img138/1233/acgbeachrm0.png
.. |image2| image:: http://img232.imageshack.us/img232/6420/acgclassicyw1.th.png
   :target: http://img232.imageshack.us/img232/6420/acgclassicyw1.png
