.. link:
.. description:
.. tags: internet, kde, proyectos, python
.. date: 2007/11/27 23:59:31
.. title: KeDElicioso
.. slug: kedelicioso

Aunque le falta un poco de azúcar todavía, puedo decir que hice un
*plug-out* para el Konqueror y los marcadores de
`del.icio.us <http://del.icio.us>`__. Es un *plug-out* porque todavía no
lo pude **meter adentro** del navegador. Para esto se necesita tener
acceso a la barra lateral que se llama KonqSideBar y está bastante verde
todavía en PyKDE, de hecho creo que no está :) .

Estoy convencido que quiero seguir usando el Konqueror, y no tener estos
marcadores que sí tenía en Firefox, me impidan seguir usándolo. Además
tenía ganas de empezar a ver un poco de HTTP-Auth y demás cosas en
Python, de las cuales no tenía idea.

Asique me puse a investigar un par de días. Bajé el
`plugin <http://www.kde-apps.org/content/show.php?content=18909>`__ que
yo ya conocía y me puse a ver cómo funcionaba. Descubrí varias cosas
ahí: el plugin para el Konqueror no era más que un archivo externo y que
no tenía nada que ver con este. Estaba hecho Perl y se comunicaba con el
navegador por medio de `DCOP <http://en.wikipedia.org/wiki/Dcop>`__ (una
de las tantas grandes cosas que tiene KDE). **DCOP**, rápidamente, es
una forma de comunicarse con los programas que están en ejecución, por
ejemplo al Konqueror le puedo preguntar que url tiene abierta, cerrar
una sesión de Kopete, etc...

Por otro lado, también descubrí que había una API de del.icio.us que
explicaba cómo se debía manejar el servicio, cómo eran las consultas y
como eran las respuestas. Qué te convenía hacer y demás. Estaba muy bien
explicado, la idea es abrir distintas urls con algunos parámetros que se
les pasan y esta te devuelve un XML con los Post, Tags y demás que se
necesita.

Lo primero que hice fue ver cómo manejaba esto el plugin de Perl, pero
lo hacía bastante feo, o por lo menos yo no lo entendía (todavía no
sabía que existía esta API). Después conseguí un programita en Python
que hacía algo similar a lo que yo quería pero no funcionaba :P . Miré
el código y ahí recién descubrí que había una API.

El código no funcionaba porque tenía las direcciones de las páginas en
cualquiera y le pasaba cualquier cosa a estas direcciones también.
Después leí que la API puede cambiar sin ningún tipo de aviso, sin
respetar las versiones anteriores y de la forma que se le dé la gana. En
este momento me pregunté: ¿Cuánto tiempo puede durar mi programa
funcionando? :D

Me puse a jugar un rato con la API, fue un rato bastante corto, ya que
te limitan las consultas a la misma para no sobrecargar el servidor,
hice 3 boludeces y se me terminó la joda. Una cagada bah! Asique seguía
haciendo cosas por otro lado, y cuando pasaba cierto tiempo volvía a
intentar y probar las funciones que había escrito y *suponía* que
funcionarían.

Me *filtraron* dos veces más y me cansé, me dí cuenta que esto así no
podía ser porque si abrías dos veces el navegador y este bajaba los
marcadores a la segunda vez no los ibas a poder ver porque estabas
*filtrado*. Además de tener que bajar **todos** los marcadores cada vez
que entrabas al navegador con su correspondiente consumo de ancho de
banda.

Me puse a buscar la forma de mejorar esto y me bajé el archivo XML a
disco y lo trabajaba desde ahí. Aunque esto era un poco feo, tenía que
hacer consultas como: ¿Cuáles son todos los marcadores que tienen tal
etiqueta?, ¿Qué marcadores tienen la palabra "linux"?, etc... Asique lo
pensé **dos segundos** y me hice una base de datos con SQLObject que
algo sabía de cuando estudié TurboGears y era una boludés.

El problema era que si agregabas un marcador desde otra computadora,
este actualizaba los marcadores de la página, pero no la base de datos.
Investigué un poco más y encontré la función *update* en la API de
del.icio.us, que indica cuándo fue la última vez que el usuario hizo una
modificación. Asique comparando esta con la última fecha de modificación
de mi base de datos queda *chanta*. Pero... ¿cómo saber la última
modificación de la base de datos? Aja! Te la encargo. Yo hice una tabla
en la que mantengo esa fecha por el momento. Una negrada bah!

Por último empecé a hacer la GUI con PyKDE, primero por el diálogo de
Agregar un Marcador, ya que supuestamente lo otro lo iba a meter en el
Konqueror (que todavía no he podido :( ), probé esto y funcionaba
perfecto. Asique seguí con la parte del filtrado de marcadores,
etiquetas y las consultas a la base de datos para estas.

Terminó saliendo algo bastante bueno, por lo menos para mi gusto, y si
lo puedo integrar completamente con el Konqueror me va a ser algo muy
útil.

Al principio dije que le falta un poco de azúcar todavía porque el
sistema de DCOP le asigna un nombre a cada uno de los programas que
están en ejecución y soportan este sistema. Pero si se puede tener más
de una aplicación del mismo programa, al nombre de esta le suma un
número, que este es su PID. Al no estar integrado con Konqueror este
número no lo puedo saber ya que la forma sería haciendo un
**os.getpid()** pero como lo estoy corriendo fuera del navegador me
devuelve otro número. Asique por el momento esto hay que ponerlo a mano.

Además no hice alguna forma de ingresar el nombre de usuario y la
contraseña todavía, porque no he tenido ganas. Hice un archivo
*config.py* en el cuál se pueden poner estos datos. Total, como nadie lo
va a usar no me calenté mucho, y si alguién lo quiere probar y no puede
me pregunta y le doy una mano :)

El código está lo que se dice **horrible**, tengo pensado cambiarlo todo
para estructurarlo de alguna forma mejor, como no pensaba hacer nada de
lo que hice fue saliendo así de feo :D

Hice una página para este programa en la que explico algunas cosas más,
hay screenshots, se puede descargar el código, etc:

http://grulicueva.homelinux.net/~humitos/KeDElicioso/
