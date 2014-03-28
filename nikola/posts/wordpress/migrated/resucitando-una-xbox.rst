.. link:
.. description:
.. tags: general
.. date: 2012/04/06 22:30:53
.. title: Resucitando una XBOX
.. slug: resucitando-una-xbox


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2012/04/06/resucitando-una-xbox/


La `XBOX <http://es.wikipedia.org/wiki/Xbox>`__ es una consola de video
juegos de Microsoft. La que compite con la PlayStation 2. Esta consola,
a mi entender, no fue muy famosa, al menos en Argentina, ya que no la he
escuchado nombrar mucho y de hecho yo la conozco \ *solamente *\ porque
la tenía mi primo, nada más. Nunca la había escuchando antes, ni tampoco
después.

La cuestión es que mi primo la compró hace unos años (usada) con una
inmensa cantidad de juegos. No sé, 300 quizás. Es más, me parece que en
estos años ni siquiera ha probado todos los juegos que le trajo.

Al pasar el tiempo, él se compró otra consola: la PlayStation 3 y la
XBOX pasó a quedar guardada en su caja original arriba del placard con
todos sus juegos. Un buen día; digamos, la semana pasada, voy a Rosario
y hablando al pedo de la vida me la mencionó, me dijo que la tenía ahí
tirada y que andaba; aunque el lector de DVD no estaba en sus mejores
condiciones, pero para jugar servía aunque a veces se colgaba la
consola. "Igualmente, fijate. Porque tiene un Disco Rígido adentro y
además tiene RED; así que capaz que podés jugar los juegos por la red o
copiarlos al disco, no sé. Llevatela si querés". Me la traje, algo iba a
inventar.

|image0|

Cuando llego, conecto todo como corresponde. Pongo un juego cualquiera y
la pruebo. Funcionó. Arrancó el juego sin ningún problema pero después
de un rato, cuando quiso cargar un video se tildó. Probé un DVD de
música y medio que de a ratos saltaba. Entonces, me propuse ver cómo era
eso de que tenía un Disco Rígido y ver también cómo era la lectora. Así
que la desarmé y me encontré con esto:

|image1|

Ahí se ve el Disco Rígido (IDE) a la izquierda de la consola, y abajo al
medio está la lectora de DVD, también IDE, pero con una simpática
diferencia: **el conector de la energía es de 12 pines**. Entonces, me
pregunté: "¿qué información enviará además de la energía por esos
pines?". El día anterior había ido a una casa de computación que venden
insumos de Consolas y demás y el loco me había dicho que nunca había
visto un conector como ese.

No podía ser, cambiar el lector de DVD de una consola de juegos debía
ser algo no trivial, pero sencillo. Digamos, el lector ES la consola,
sin eso no funciona, no sirve y además los lectores de DVD se gastan. Es
lógico. Tienen una vida útil y a este se le había terminado.

Por suerte, Googleando, `entontré esta
guía <http://www.euskalnet.net/dlosada/Sustituir_lector_XBOX.html>`__
(que encima es GPL!) que me guío mucho en cómo se hace el cambio. Me
puse manos a la obra con mucha fe. Busqué una fuente vieja para sacar el
conector de la energía (ya que la lectora de dvd nueva necesita el
conector estándar), corté el cable de alimentación que va al disco
rígido y adjunté el nuevo conector. Ahora tenía dos conectores de
energía: uno para el disco rígido y otro para la nueva lectora.

Mi intención en el primer prototipo era simplemente que funcione, sin
soldar nada y sin integrar nada. Entonces, una vez que tenía eso ya
adjuntado quité el cable IDE de la vieja lectora y lo conecté en la
nueva dejando el cable de alimentación en la lectora vieja porque quería
que la "otra información" que mandaba por ese cable la siga leyendo de
la lectora vieja.

Eso funcionó sin problemas. Prendí la XBOX, puse un DVD, reinicié y
salió andando. Probé un juego y también un DVD de Video. ¡GENIAL! Andaba
de lujo. Ahora que me quedaba puentiar el conector de energía "loco" ese
para decirle: 1) está cerrada la bandeja y 2) estoy listo para leer el
DVD. Aunque eso sea mentira :)

Todavía me falta hacer que el botón Open de la XBOX abra la lectora de
DVD nueva que le puse; pero para esto necesito soldar un par de cosas y
como la lectora que estoy usando de prueba no es mía, no lo he hecho
aún. Supongo que el lunes me compro una lectora IDE por unos $200
aproximadamente y lo hago. Después de eso me queda hacer que encaje
dentro de la XBOX así la puedo cerrar y ahí quedaría JOYA. Por el
momento lo que tengo es esto:

|image2|

.. |image0| image:: http://humitos.files.wordpress.com/2012/04/dsc_1765.jpg
   :target: http://humitos.files.wordpress.com/2012/04/dsc_1765.jpg
.. |image1| image:: http://humitos.files.wordpress.com/2012/04/dsc_1864.jpg
   :target: http://humitos.files.wordpress.com/2012/04/dsc_1864.jpg
.. |image2| image:: http://humitos.files.wordpress.com/2012/04/dsc_1880.jpg
   :target: http://humitos.files.wordpress.com/2012/04/dsc_1880.jpg
