.. link:
.. description:
.. tags: facultad, java, python
.. date: 2007/11/09 18:17:09
.. title: Python más rápido que Java
.. slug: python-mas-rapido-que-java


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/11/09/python-mas-rapido-que-java/


|image0|

Con un título de post robado de la charla de `Facundo
Batista <http://www.taniquetil.com.ar/plog/>`__ y Lucio Torre ("`Python
más rápido que
C <http://www.cafeconf.org/2007/slides/facundo_batista_python_mas_rapido_que_C.tar.gz>`__\ ")
empiezo un post para comentar los resultados que fui obteniendo a lo
largo de la implementación de un árbol de búsqueda trie, para el
desarrollo de un trabajo práctico de la facultad.

Una parte del trabajo consiste en crear una función de autocompletado,
esto es, a medida que el usuario vaya tipeando letras en un editor de
texto, se despliegue una lista con todas las sugerencias que coinciden
con la cadena de teclas tipeadas. Por ejemplo, si el usuario va tipeando
"automovi", el programa sugiere las palabras ["automovilístico",
"automovilismo", "automovilista"] (la lista de todas las palabras son
previamente cargadas desde un archivo de texto plano).

Con mi equipo intuíamos que esto se hacía con un árbol, ni idea porqué,
pero pensábamos que era mejor que hacer una lista con todas las
ocurrencias y filtrar por "startswith()" (empieza con), ya que de esta
forma estamos recorriendo **toda** la lista, y el proceso se alentecería
bastante. Asique opción descartada definitivamente... Aunque... ¡Aunque
nada, y listo

Luego seguimos leyendo el trabajo, y decía: *"La cantidad de palabras en
los diccionarios puede ser grande, por lo cual se recomienda que la
selección de la palabra actual se realice mediante una referencia a una
estructura arbórea, y que no se cree una lista con todas las palabras
posibles, ya que la ineficiencia de esta opción puede notarse en una
aplicación interactiva como la que se pretende desarrollar"*. Por lo que
no descubrimos nada con lo que intuíamos, pero por lo menos nos dimos
cuenta que no estábamos equivocados...

El primer día que nos juntamos con
`Guille <http://gheize.wordpress.com>`__, mi compañero de grupo junto a
Iván, aunque éste último se encontraba ausente debido a que estaba en su
ciudad (¿natal?), nos pusimos las pilas pensando cómo iba a ser la
estructura de datos que queríamos crear y cómo podíamos luego buscar las
coincidencias con respecto a lo que tipeaba el usuario.

Sin ningún tipo de estupefaciente encima, ni siquiera cerca, empezamos a
delirar varias ideas, árboles, listas, diccionarios, pilas, colas, mates
y música volaban por todos lados. Pero ninguna de todas las ideas nos
convencía.

A todo esto estábamos en la tarde del Miércoles de esta semana en la
pileta de mi casa pensando estas cuestiones con un infiltrado en el
grupo (Nico). Aunque ya habíamos trabajado a la mañana corrigiendo
algunas cosas del trabajo anterior, que pensábamos que podían llegar a
estar mal. La idea que fue más acertada por los tres, fue la de tener en
cada nodo una lista con todos sus hijos, además de un caracter (que
componía una de las letras de la palabra), y una marca indicando si en
ese nodo terminaba una palabra o no.

Según algunos comentarios de Nico en su computadora la carga del
*diccionario.txt* de unos 800Kb aproximadamente en una estructura le
llevaba algo así como **5min**, ¡Una guasada! Lo que en gran parte fue
el comienzo de esta investigación.

Hicimos algunas cosas más (perdimos un poco de tiempo), y nos pusimos a
codificar algo con el Guille. No llegamos a nada concreto, ni siquiera
pudimos terminar de pulir la idea que teníamos. Él se fue y yo me quedé
con la espina en el ojo de que cómo no podíamos implementar un árbol, si
ya lo había hecho en ocasiones anteriores... Bueno, pasó y me fui a
dormir.

Al otro día cuando me levanto, me voy derecho al canal IRC de
`PyAr <http://www.python.com.ar>`__, sabiendo de ante mano que tienen
muy buena onda y que seguro alguno me iba a tirar alguna pista de cómo
implementar un árbol de este tipo, por lo menos en Python. Lo que más
necesitaba era saber si la idea que teníamos estaba más o menos
acertada, sobre todo para no empezarme a pelear con Java sin saber si lo
que estoy haciendo va a funcionar o no.

Me tiraron varias ideas teóricas, conceptos, material para investigar
(*que busque en google*;)\ *)* y demás, hasta que Facundo mandó `una
implementación <http://www.paste-it.net/4450>`__ de esa estructura
arbórea que yo necesitaba en Python. Él implementó algo muy parecido a
lo que teníamos **pensado** pero cambiando algunas cosas, por ejemplo,
en vez de listas utilizó diccionarios y algunas otras cuestiones que
permite Python. La cuestión es que me hizo entender **muy bien** el
funcionamiento de éstos árboles y lo rápido, fácil y útil que es Python
para crear prototipos de cualquier cosa.

Lo primero que probé fue cargar todo este archivo con la implementación
que hizo Facu (en el link anterior ya tiene las modificaciones que le
hice yo). Lo cargó enseguida, demoró 5.12 segundo, que comparado con los
5 minutos de los que veníamos manejando con Nico, no era nada. Hice una
búsqueda y funcionó. Pero pasaron algunas cosas, por ejemplo el programa
en memoria estaba ocupando 185Mb de ram y 100Mb de memoria virtual, lo
que es **¡Una locura!**. Igualmente no molesté más a la gente de PyAr
hasta que implemente mi versión en Java y podamos comparar tiempos de
ejecución, de carga, de búsqueda y demás porque quizás esto era
*¿aceptable?.*

Luego de hacerlo en Java después de algunas peleas con los tipos de
datos, partiendo de que no encontraba cuál era la clase de diccionarios
ya que está *Dictionary*, pero esta es abstracta, por lo tanto no puedo
tener instancias de estas. Así seguí bajando por el árbol de herencia
hasta llegar a la clase *Properties*. Ni idea si esto es un diccionario
o no, pero lo hice con esta clase y funcionó por lo menos...

Terminé de codificarlo todo, el código resultante quedó
`así <http://www.paste-it.net/4453>`__ (la implementación en Java) y los
tiempos para "cargar las palabras del diccionario al árbol" y "cargar el
árbol y realizar una búsqueda" son
`estos <http://www.paste-it.net/4445/>`__. El comando **time** está
ejecutado tres veces por cada operación. Una vez que el programa carga
todo el árbol en memoria, este ocupa 108Mb de memoria ram física y al
rededor de 180Mb de memoria de intercambio algo *similar* a lo que
ocupaba el programa hecho en Python. Asique estaba conforme con ambas
implemenetaciones hasta el momento.

*"La primera versión que había hecho del programa en Java ocupaba sólo
20Mb en memoria, lo cual me sorprendió mucho cuando ví. Pero que luego
de unas correcciones pasó a parecerse a la implementación hecha en
Python"* ;)

En este momento dejé un comentario en el foro de la materia explicando
esta situación, comentando de que habíamos creado esta estructura y que
seguro que el programa iba a ser muy lento a la hora de mostrar las
sugerencias en la lista de posibilidades. Pero hasta el día de hoy no he
tenido ninguna respuesta :( .

Comenté en el canal de PyAr que me parecía raro que el programa ocupara
tanto en memoria en comparación con la incorrecta implementación del mío
:D (que en este momento desconocía) y Facundo mejoró su código agregando
`__slots__ <http://www.python.org/doc/current/ref/slots.html>`__
para que la clase sepa cuanta memoria reservar de ante-mano. Y el
programa pasó a ocupar como 80Mb menos en memoria, lo cual es bastante
menos.\ **Interesante**.

*Hoy, tres días después de haber pensado que era una locura meter todas
las palabras y hacer startswith, me puse a implementar esta forma de
encarar el problema, para luego llevarme una sorpresa **gigante.***

El programa para la carga y búsqueda lo hice en Python, ya que quería
ver resultados rápidos, y Python para esto viene al pelo. Ni bien
terminé de hacerlo corrí la aplicación cargando el árbol y nada más, en
dónde veo que esta carga estaba demorando solamente 0.13 segundos **como
mucho**, lo que no se compara con la carga del árbol que era 5.12
segundos con el algoritmo de Facundo también hecho en Python y 2.6
segundo que demoraba el mío hecho en Java. Entonces ¿es mejor utilizar
listas que árboles para esto? El programa en Python con una lista en vez
de un árbol es `este <http://www.paste-it.net/4455>`__.

Por ahora estoy bastante mareado con todos los resultados que obtuve. En
el canal de PyAr me dijeron que quizás no importe tanto el tiempo que
demore en cargar el diccionario ya que esto se hace una sola vez, lo que
más importa es el tiempo de búsqueda de concordancias... Pero el
resultado promedio que obtuve con esta implementación buscando 100
palabras aleatoreas:

::

    [manuel] [~/blog/python-mas-rapido-que-java]$ python lista.py

    En cargar: 0.07 seg

    Cantidad de palabras a buscar: 100

    Busq x palabra: 41.96 mseg

    [manuel] [~/blog/python-mas-rapido-que-java]$

Cuanto tenga menos dudas o esté seguro al menos de cómo lo voy a
desarrollar y qué estructura de datos voy a usar para hacer esto escribo
cómo y qué hice :P

.. |image0| image:: http://img62.imageshack.us/img62/1199/imagendelpostru1.png
