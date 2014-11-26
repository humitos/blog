.. title: Soldando una placa icaro np06
.. slug: soldando-una-placa-icaro-np06
.. date: 2014/05/25 13:32:55
.. tags: argentina en python, córdoba, icaro, software libre, electrónica
.. link: 
.. description: 
.. type: text

.. admonition:: Nota

   Hay una :doc:`segunda versión <placa-icaro-terminada>` de este post
   donde se muestra la placa terminada y algunos consejos más sobre
   cómo hacerlo.


Ayer de mañana nos fuimos con el Guille a comprar todos los
`componentes necesarios <roboticaro.org/componentes/>`_ para armar la
placa ICARO np06 (la última del proyecto a la fecha) que me había
regalado Valentín durante mi estadía en su casa. Si bien yo tengo la
np05 que me la regaló Valentín en la PyCon 2013 de Rosario, esta placa
ya me vino lista para usar, no es que la armé y soldé los componentes
yo. Esta placa me sirvió para aprender todo lo que sé de electrónica
al día de la fecha, quitarme el miedo a romper las cosas (creo que
quemé 3 LEDs únicamente al día de hoy) y darme muchas ganas de seguir
leyendo tutoriales y videos en YouTube.

Como ayer durante la mañana nos colgamos hablando al pedo durante el
desayuno, se nos hizo tarde y no llegamos a todos los lugares que
queríamos ir a averiguar por todos los componentes necesario y tuvimos
la mala suerte de que en el lugar al que me recomendaron ir,
Electrocomponentes S.A., no tenían todos los componentes necesarios,
pero igualmente compramos todo lo que tenían como para empezar a armar
la placa:

.. image:: placa-icaro-np06.jpg

Tuve algunos problemas con algunos componentes y otras cositas que me
fui dando cuenta sobre la marcha, que detallo a continuación:

* Los colores y tamaños de las resistecias difieren con respecto a
  los que están en la página oficial. Yo tengo resistencias verdes y
  celestes y en la página oficial son marrones. Sin embargo, el valor
  que me daba el tester era de 470 ohms y 10K ohms, que son los
  valores correctos. Todavía no sé qué quiere decir que sean de
  diferentes colores.

* Seguí el `post que muestra la nueva placa
  <http://sistema-icaro.blogspot.com.ar/2013/09/nueva-placa-icaro.html>`_
  como ejemplo de dónde van los componentes, así cómo también la
  nomenclatura impresa en la placa con respecto a la `lista de
  componentes <http://roboticaro.org/componentes/>`_

* Los LEDs tiene una cara plana (en la base) que coincide con la
  impresión de la placa. Esto es útil para no errarle a la hora de
  buscar el positivo y el negativo de los leds.

* Me vendieron un capacitor electrolítico de 10 uF x 50V en vez de 10
  uF x 16V, con lo que no estaba seguro si me iba a servir, pero
  buscando en internet encontré `ésta imágen
  <http://2.bp.blogspot.com/-maSE_sXpDjU/UiULZmdG1fI/AAAAAAAAAN4/L_rhB-hGFjQ/s1600/2kdp.jpg>`_
  que dice que eso sería el máximo voltage que se aguanta, por lo que,
  como es mayor el del que me vendieron del necesario, supongo que va
  a estar todo bien.

* En ningún lugar está especificado cómo se hacen los puentes en la
  placa. Eso todavía no lo he hecho porque no estoy seguro dónde van
  (aunque parezca bastante obvio porque están cerquita los
  agujeros). Pero por ejemplo, en el mismo lugar del PIC18F4550 hay 4
  agujeros que no sabría cómo puentear (si es que va un puente
  ahí). Eso no está claro y tampoco se puede sacar la info de una
  imagen de la np06 ya armada porque está debajo del PIC y eso no se
  ve.

* El botón "Pushbutton para pcb" *sw2*, si bien tiene 4 pines y 4
  agujeros, necesita tener conectado únicamente dos pines, pero no
  estaba seguro cuáles 2 tenían que ser. Hay 4 posibilidades de
  colocación. Lo soldé sin saber cuál era la posición correcta,
  después les cuento.

* Los capacitores electrolíticos tienen polaridad. La pata negativa
  está indicada con una banda impresa con signo menos gordo sobre una
  de las caras del cilindro por encima de la pata negativa.

* En el lugar del L293D (*u3*) hay 4 agujeros como para hacer 2
  puentes, pero está muy próximos uno de los otros, así que no
  entiendo porqué eso no se hizo directamente como una pista en la
  placa, o sino no estoy entendiendo bien cómo deberían ir los
  puentes.

* Todavía no tengo el "Botón de encendido para pcb" *sw1*, pero
  supongo que voy a tener la misma interrogante que con el *sw2*.

* Entiendo que esta placa puede funcionar con uno de estos dos PICs:
  18f4550 o 18f2250. Me gustaría saber si se pueden soldar los dos
  sócalos y tener la posibilidad de intercambiar de PICs una vez que
  la placa esté completada.

* Para saber la polaridad del único diodo que tiene la placá, seguí la
  impresión que está en la placa y la marca en el diodo mismo.

* No pude encontrar en ningún lado cómo soldar el cristal, si tiene
  polaridad o si va de cualquier forma.

.. admonition:: ¿Cómo soldé los componentes?

   Para soldar todos los componentes lo que hice fue ir introduciendo
   de a varios por tandas (por ejemplo los 8 leds verdes de control),
   doblando sus patas para los costados como para que cuando de vuelta
   la placa no se muevan ni se caigan y, una vez que tenía el lápiz
   bien caliente, lo posicioné sobre la pata a soldar y la placa (como
   para que se vayan calentando ambas partes) y luego con la otra mano
   acercaba el estaño a la punta del lápiz para que dezlice por la
   punta hasta llegar a la pata y la placa. Un poquito menos de una
   gota fue suficiente.

Eso es todo lo que tengo por ahora. Si bien el proceso es sencillo,
hay unos cuántos interrogantes básico de una persona que es la primera
vez que lo hace. Estoy muy ansioso por terminar de soldar todos los
componentes y saber si esta cosa va a funcionar o si tiré la plata :P

Espero que esto sirva de feedback para Valentín sobre qué cosas se
pueden documentar un poco más, problemas típicos, qué decir en las
charlas introductorias, con qué tener cuidado o demás e incluso para
que me tire un poco de data de cómo resolver los problemas que tengo
;)

Personalmente, considero que el armado de la placa es muy intuitivo,
creo que hice casi todo bien con un conocimiento básico / nulo de cómo
se hacen estas cosas. Es muy bueno que tenga todo impreso en la placa
y que la lista de componentes mencione en qué lugar de la placa van.

Mañana voy a comprar lo que me falta y si puedo la termino.

¿Qué? ¿Cuánto tiempo me llevó armar hasta dónde tengo ahora? Ah, Unas
3 horas!
