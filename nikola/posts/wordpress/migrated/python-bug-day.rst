.. link:
.. description:
.. tags: python, software libre
.. date: 2008/02/24 20:53:48
.. title: Python Bug Day
.. slug: python-bug-day


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2008/02/24/python-bug-day/


El sábado pasado hubo un `Python Bug
day <http://wiki.python.org/moin/PythonBugDay>`__, en el cuál se
"juntan" en el canal de IRC python-dev de freenode.net y entre todos
cooperan para solucionar todos los Bugs, errores de documentación, y
demás problemas que tiene Python, porque, que sea el mejor lenguaje que
exista actualmente no lo hace que esté libre de Bugs ;) .

El viernes por la tarde estuve hablando con los chicos de PyAr, bah,
hinchando como siempre. Les pregunté qué es lo que tenía que saber,
probar y hacer para poder participar. Facundo me recomendó que lea unos
`slices <http://www.cs.ubc.ca/~drifty/pycon/sprint_tutorial.pdf>`__ que
hablaban sobre el tema de forma muy reducida, pero que explicaba los
puntos claves.

Bueno, me leí esto, bajé el código, compilé y probé... ¡Funcionaba!, con
la única diferencia, que de hecho no sé a qué se debe, en el python que
me compilé no andan las flechitas del teclado para desplazarte por la
línea actual.

Después de esto consulté la
`página <http://www.taniquetil.com.ar/cgi-bin/pytickets.py>`__\ de
Facundo, que muestra todos los Tickets que están abiertos todavía, y
además permite hacer algunos filtrados. Busqué los que tenían de llave
"Easy" (Fácil), para ver si podía resolver alguno.

El `primero <http://bugs.python.org/issue1746071>`__\ que agarré, era
sobre el módulo ConfigParser, que sirve para trabajar con archivos de
configuración, estilo .ini. El problema era que al agregar una sección
con el nombre "DEFAULT" y luego agregarle a esta sección un valor, se
duplicaba. Osea, quedaban dos secciones "DEFAUL" lo cuál está mal...
Perdón, 'estaba' mal :) .

El ejemplo que mostraba el autor de la apertura del Ticket es este:
``>>> import sys, ConfigParser  >>> c = ConfigParser.ConfigParser()  >>> c.add_section('DEFAULT')  >>> c.write(sys.stdout)  [DEFAULT]  >>> c.set('DEFAULT', 'color', 'yellow')  >>> c.write(sys.stdout)  [DEFAULT]  color = yellow  [DEFAULT] ``

Me puse a ver bien cuál era el problema, preguntando en PyAr si me
podían ayudar, investigué un poco, leía todos los comentarios, intentaba
traducirlos. La verdad es que estaba bastante en bolas. Después de un
tiempo buscando algo (pero no sabía qué) encontré que ya había un parche
hecho, incluso documentado y demás. Lo descargué y lo probé. Funcionaba
perfecto. Sólo que le faltaba agregar algunas cositas, como testeos y
modificar el archivo NEWS, que es donde se ponen todos los cambios entre
las versiones.

Asique subí la versión completa del parche y comenté que lo había
probado, funcionaba bien y estaba todo OK. Le avisé a Facundo y él cerró
el ticket ese. Gracias Facu!

Me hice unos mates, dí un par de vueltas en casa (toqué el bongó y la
guitarra un rato) y volví a buscar algún ticket que pueda llegar a
solucionar. Encontré `este <http://bugs.python.org/issue1746071>`__. Y
ví que el tipo pedía un agregado de una funcionabilidad, pero esta ya
existía. Asique pregunté en python-dev algo así como: "Why this ticket
http://bugs.python.org/issue2130 is open yet?" (estuve 15 minutos
formulando esta pregunta) o lo que enseguida Facundo me contestó "Thanks
humitos!" y lo cerró.

Ya le había agarrado el gustito a esto y estaba bastante embalado. Está
bueno, poder ayudar aunque sea en lo más mínimo a un lenguaje que me dió
tantas satisfacciones y me enseñó muchas cosas. Ademas de darme unos
pesitos también. Asique busqué otro y encontré
`uno <http://bugs.python.org/issue1746071>`__\ que venía como anillo al
dedo con lo que había rendido yo (Sistemas Operativos), era sobre el
módulo mutex de python y decía que esta función no hacía nada
automáticamente. Osea, permitía que dos procesos se ejecuten
simultáneamente estando en su región crítica.

Me costó bastante entender bien algunas cosas. Porque decían que esta
clase no se tenía que utilizar para multithreading, pero justamente es
para eso que están hechos los mutex. Asique bueno, después de unas
discusiones ¿filosóficas? sobre si este módulo lo utilizaba alguien o
no, y si debía seguir estando en Python, llegamos a un acuerdo en lo que
pensábamos entre todos. Facundo envió un mail a python-dev preguntado
estas cosas y por lo que tengo entendido este módulo va a desaparecer en
Python 3 o al menos lo van a ocultar.

Resumiendo, en una mañana y una parte de la siesta, con los chicos de
PyAr cerramos 3 tickets, lo que me parece para ser la primera vez que
intento ayudar acá está bien.
