.. link:
.. description:
.. tags: hosting, internet, proyectos, pygame, python, software libre, ssh
.. date: 2007/11/19 02:12:17
.. title: Hosting nuevo - Vida nueva
.. slug: hosting-nuevo-vida-nueva


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/11/19/hosting-nuevo-vida-nueva/


¡Mission acomplished! Hace un rato que termino de mudarme. No está demás
decir que en `PyAr <http://www.python.com.ar>`__\ (Python Argentina) hay
gente que tiene muy buena onda con la respuesta de los mails que uno
manda a la lista. Pero además, tienen buena onda en otros sentido
también.

A través del canal de irc de pyar (#pyar en freenode.net) conocí a
`StyXman <http://grulicueva.homelinux.net/~mdione/glob/>`__ (o
StucKman); que quitando el problema de doble personalidad que tiene, es
uno a los que hago referencia arriba.

Muy sutilmente, hace un par de días (dos exactamente :P ) me ofreció
hosting en su servidor *casero*. Le dije que lo iba a pensar y que era
mejor que lo charlemos por mails, ya que yo tenía **demasiadas dudas**
al respecto. ¿Cómo era el servicio? ¿Qué tengo que hacer? ¿Cuanto tengo
de subida? ¿Cuanto de bajada? Que sé yo, una cantidad de preguntas que
creo que cualquier persona que va a un hosting algo bastante distinto a
lo que es Google, tiene en su cabeza.

Bueno, después de un par de mails de idas y vuelvas, nos pusimos de
acuerdo. Arreglamos para empezar a hacer las cosas hoy (ya ayer) por la
tarde. Enseguida me creó una cuenta para poder acceder por **ssh**, si
bien yo tengo conocimiento sobre esto, tuve que recurrir a mis
`artículos
anteriores <http://humitos.wordpress.com/2007/10/01/conexion-remota-por-ssh/>`__
sobre este comando, para refrescar algunos conceptos.

Bajé todos los repositorios de Google, como comenté en mi `post
anterior <http://humitos.wordpress.com/2007/11/18/mudarse-de-google-code/>`__.
Pero al final tuve que modificar algunas cosas en esta mudanza. Cuando
bajé los repositorios de google lo hice con el comando:

::

    $ svk mirror //local http://<proyecto>.googlecode.com/svn/

Lo cual me dí cuenta que está **mal**. Porque esto te crea una carpeta
*local* en el repositorio y dentro de ella te manda todas las otras
(trunk, branches, tags). Entonces a la hora de hacer el **svnadmin
load** me quedaban carpetas *indeseadas*. Asique busqué un rato, y me dí
cuenta que el error era el *//local* pero en casi todos los ejemplos que
ví en internet estaba así y no explicaba mucho el porqué. Por lo que yo
lo dejaba así cayadito.

Lo que hice en un principio fue bajar todos los repositorios de google a
mi máquina, para luego subirlos por ssh al servidor. Después me avivé y
me dije: *¿Porqué no ejecutar mi script de Python que me baja todos los
proyectos en el servidor?* Ya sabía que tenía Python en el servidor
asique iba a funcionar, lo único es que me faltaba el comando **svk**,
pero enviando un sólo mensaje al administrador del servidor en pocos
minutos tenía lo que necesitaba instalado.

Bueno la cuestión es que después de un par de horas tenía todo andando
en el servidor mal llamado *mio*. En cuanto al llamado por StyXman hacia
mi persona como *"iluso"*, no tiene idea de lo que está diciendo. En el
mismísimo momento en el que se fue a dormir, busqué todas las pass del
sistema y empecé a cambiar todo tipo de configuraciones de la máquina
adaptándola a mis necesidades. Ja! En realidad todavía no sé ni como
cambiar la clave que me dió por defecto de mi cuenta de usuario :( . Ya
veremos, todo se aprende... tampoco busqué.

"Asique bueno", diria alguna persona que conozco. En cuanto tenga todo
bien configurado se los comunico a mis amigos **co-desarrolladores** de
algunos proyectos para empezar a meterles pilas a este repositorio.

Me gustan varias cosas de esto. Para empezar sé como están funcionando
algunas cosas ahí, y soy mi propio administrador de los repositorios,
osea, no dependo de google si quiero borrar el repositorio a la mierda
cuando quiero (hace un par de semanas hice un "Delete proyect" en google
y todavía está ahí :( ), hacer mis backups, subir cosas, bajar cosas...
que sé yo. Por lo menos hasta que me reten, me echen o pase algo. Por
algo dicen que no todo es color de rosas, pero esto pinta bastante bien.

Vamos a ver cómo se va desarrollando con el tiempo esto, espero no tener
ningún problema y no complicarle la vida a StyXman, o a su alma gemela
StucKman, haciendo cagadas...
