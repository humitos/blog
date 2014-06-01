.. title: Placa ICARO terminada
.. slug: placa-icaro-terminada
.. date: 2014/05/30 12:55:39
.. tags: icaro, software libre, electronica, cordoba, argentina en python
.. link: 
.. description: 
.. type: text

.. admonition:: Nota

   Hay una :doc:`versión previa <soldando-una-placa-icaro-np06>`
   a este post donde se explica la primera parte de esta
   aventura

¡Terminé la placa icaro!

.. image:: placa-icaro-terminada-front.jpg

Como no podía ser de otra forma, cuando le enchufé el clabe USB no
prendía. Ouch! Pasé un rato pensando en qué podía estar mal y me di
cuenta de que no le había puesto ninguno de los jumpers que llevaba,
lo cual es una condición necesaria para que la placa prenda. Al
menos, poner uno de los jumpers: el que indica de dónde viene la
energía (de la batería externa o del USB)

Luego de poner el jumper correcto, conectar al USB y presionar el
botón de encendido se ve una luz roja encenderce: whoa! una
locura. ¿Te imaginás mi cara no?

Para llegar a completar la placa, me basé en la ayuda de muchas
personas y en particular de un mail que envió Kiara Navarro a la lista
de correo de Icaro durante esta semana, después de leer mi post sobre
los inconvenientes que tuve al soldar los componentes y las dudas que
fueron surgiendo:

.. code::

   Felicidades por el post. Estuvo interesante.

   Algunos datos que quisiera compartir en base a tus dudas.

   El color de fondo de las resistencias realmente depende es el
   material con que estan hechas. Realmente no tiene mucha importancia
   en este tipo de aplicaciones. Nunca había utilizado resistencia de
   fondo verde, pero las de fondo azul es porque están hechas a base
   de película de metal. Las clásicas que son las de color marrón es
   porque están hechas a base de carbón. Realmente lo importante aquí
   es el valor que ellas tengan y la potencia que éstas puedan
   disipar.

   En cuanto a la parte de los capacitores electrolíticos el dato del
   voltaje te indica cuánto voltaje puede soportar. En tu caso está
   bien ya que necesitabas un capacitor que soportará al menos 16 V,
   como el que compraste soporta 50 V, entonces está bien. En otras
   aplicaciones esto quizás no pueda ser buena idea, pero para este
   caso con solo seleccionar un capacitor con un voltaje superior o
   igual, está bien.

   En cuanto a los puentes. Valentín me facilitó una placa con los
   puentes ya puestos. Puedo compartir una foto contigo para que te
   guies de allí. Si puedes, verifica que el PCB, ya que allí de
   seguro debe estar. Como yo ya tenía los puentes allí no lo revisé.

   En cuanto a los push button, en efecto sólo se conectan dos
   pines. Un esquema general de ese tipo de push button es el que está
   en esta imagen:

   http://www.arduino-hacks.com/wp-content/uploads/2014/01/4-pin-pushbutton1.png

   En este caso no es necesario que tengas cuatro combinaciones,
   podrías probar colocando dos de los pines a un circuito que
   encienda un led. Cuando aprietas el botón, si se enciende el led
   entonces ese es tu par de pines. Nada más tendrías que asegurarte
   seleccionar el par de pines que se ajuste a la posición de la
   placa. Si ves en la misma placa, los pines deben pasar por una
   línea paralela y no perpendicular.

   En cuanto a la parte de los puentes del L293D. Los puentes no están
   próximos. Es inverso. Es decir, tienes un puente distinto en la
   cercacía de cada agujero. Si te fijas en la plaquita, en medio de
   los dos agujeros de arriba y los dos agujeros de abajo hay pistas
   de conexión. Necesitas tirar un puente de arriba a abajo para que
   no intervenga con esas pistas.

   Con el otro push button de seis patitas, es lo mismo. Nada más debe
   elegir un par y fijándote en la posición de conexión en la
   plaquita. Para ese caso, el par debe estar uno al lado del otro en
   la misma línea paralela.

   Con respecto a los microcontroladores sí lo puedes hacer. Pero no
   con los sockets convencionales. Echa un vistazo a los sockets.

   http://aliatron.pt/e-biz/images/40.jpg

   Lo que podrías hacer es cortar la parte que une cada columna y
   soldarlos.

   O comprarte los sockets sil. Acorde con las patitas del micro.

   De todas maneras yo recomiendo que solo uses uno porque quitar el
   pic después de introducirlo es algo delicado. Primero antes de
   colocarlo en la placa, lo debes tener quemado. Porque es díficil
   retirarlo. Esa es mi opinión. También, estar cambiando y colocando
   en la placa puede hacer que las patitas se doblen. Es por eso que
   muchos circuitos utilizan ISCP, para en vez de retirar los PICs de
   los circuitos, se queman desde esos pines ISCP. Pero como la
   plaquita Icaro una vez que le micro esté quemado, el se encarga de
   bajar el compilado con la misma plataforma.

   En cuanto al cristal, ellos no tienen polaridad. Así que lo pueden
   colocar como quieras. Eso no importa.

   Espero haberte ayudado.

   Saludos,


La verdad que la información que tiró es *altamente valiosa*. Cubrió
todas mis dudas y me dio mucha buenas vibras para seguir metiendo
estaño sobre la placa sin miedo a romper nada y con la fuerza y el
entusiasmo a arreglar cualquier cosa que se me pueda llegar a romper
en el medio.

Ahora, algunos otros consejos de mi parte, que me encontré mientras
continuaba el proceso de soldado y algunos tips que me dijo Valentín
cuando fui a mostrarle la plaquita terminada:

* Los 8 LEDs verdes que indican el estado de las salidas del PIC están
  al revés. La impresión sobre la placa marca que el lado plano va
  hacia afuera y eso es incorrecto.

* Es recomendable primero soldar los puentes (esos cablecitos que van
  por encima de la placa) ya que son muy chiquitos y una vez que tenés
  todos los componentes puestos se complica un poco.

  Para saber dónde y cómo van los puentes, me basé en el archivo de
  KiCAD que se encuentra en el sitio web de ICARO. Aparecen en rojo en
  la visualización.

* Para saber de qué forma va el botón de switch, usé un tester y medí
  la continuidad entre sus patas con el botón pulsado y con el botón
  suelto. Teniendo esa info, miré las pistas de la placa y soldé como
  me parecía. Igualmente, hay dos formas nomás de ponerlo, lo que
  haría que la placa esté prendida cuando el botón esté pulsado o que
  esté prendida cuando el botón esté suelto. No hay mucha más ciencia
  ahí.

* Las tiras de pines hembra que se usan en las salidas del PIC las
  intenté cortar con un cutter y no pude. Probé con una pinza y se me
  rompían los pines. También probé con una tijera y tuve el mismo
  problema.

  Después Valentín me dijo que los podía pedir ya cortadas en la casa
  de electrónica o sino que siempre iba a tener que sacrificar uno de
  los pines. Y posta, en vez de medir de a 8 medía de a 9 y ese noveno
  moría. Después lijaba un poquito el extremo por dónde había cortado
  para que quede prolijo y listo.

* Una vez soldado el conector USB, es recomendable llenarle de estaño
  los dos orificios que tiene la placa en dónde entran sus patas que
  irían apretadas con una pinza. Esto es para que haga buena fuerza y
  no se mueva al momento de conectar el cable.

* Como tenía todos los LEDs ya soldados y Valentín me dijo que estaban
  al revés, tenía que desoldarlos, darlos vuelta y volverlos a
  soldar. Para eso, me compré un lapiz desoldador que, una vez que se
  derrite el estaño con el lapiz soldador, este otro lapiz desoldador
  se lo chupa y lo retira de la placa. Eso nos permite retirar el LED
  y darlo vuelta.

  Acá hay que tener mucho cuidado y tratar de usar el lapiz desoldador
  la menor cantidad de veces por cada pin porque se corre el riesgo de
  que se levante la pista de cobre que está pegada en la placa PCB;
  cosa que me pasó en el pin de la masa (por lo que ningún led
  prendía) y tuve que meter un pedazo de cable a lo artesano para
  *reconstruir* esa pista.

Una vez que terminé de armar mi placa, me encontré con Valentín y me
cargó el bootloader (firmware) en el PIC con su programador de PICs
(que yo todavía no tengo -llega el Lunes) y nos pusimos a probar la
placa.

.. image:: placa-icaro-terminada-back.jpg

Ahora sí, la placa está terminanda y funcionando, ya le puse algunos
programitas para que vaya corriendo y ver si funciona por más de 10
minutos :D . Lo que me queda ahora es empezar a jugar con los relés y
algunas lámparas de 220v.

Después escribo como me fue si es que no morí en el intento :P
