.. link:
.. description:
.. tags: internet, software libre
.. date: 2009/02/02 15:13:22
.. title: 'Flashear' router Linksys WRT54G V8.0
.. slug: flashear-router-linksys-wrt54g-v80


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2009/02/02/flashear-router-linksys-wrt54g-v80/


Han pasado tantas cosas desde la última vez que escribí algo en mi blog,
que no me voy a poner a contar todas, sino que simplemente voy a
comentar una de las últimas cosas que he hecho (y que por suerte
funcionó :) ).

Hace una semana me compré un router Linksys WiFi  porque le estoy
*instalando* la red a mi mamá en su casa de Paraná. El tema es que
contrató el servicio de Arnet y necesita conectar dos PC's a internet.
Una se encuentra en la entrada de la casa y otra al fondo, dónde para
llegar a esta hay que pasar varias paredes internas y externas (más
gruesas y con cámara de aire) y además hay, de camino, un teléfono
inalámbrico y un horno microondas (los que son considerados como
*obstáculos*).

En fin, la cuestión es que como no quería cablear todo, debido a que mi
vieja es quisquillosa con *la estética* de la casa, sugerí probar
poniendo WiFi y ver si llegaba hasta el fondo de la casa. Lo propuse
como **dudándolo** porque la verdad que no tengo ni idea cuánto se banca
una conexión de WiFi en cuanto a la distancia.

El router lo compré hace una o dos semanas, y antes de llevarlo a la
casa de mi mamá quería probarlo, asique lo saqué de la caja, enchufé el
cable de red que trae al modem adsl y el transformador como corresponde.
Prendió. Agarré la notebook (cosa que comentaré algún día en otro post)
y **yastá** tenía WiFi funcionando joya, no tuve que hacer nada de nada.

Pasaron unos días y recordé que existía un **Firmware libre** que se les
podía poner a los Linksys y que estaba bueno, o al menos tenía esos
comentarios de este firmware, por lo que me puse manos a la obra.
Leyendo por internet caí en el firmware
`dd-wrt <http://dd-wrt.com/dd-wrtv3/index.php>`__, que al parecer es uno
de los más conocidos (cuando fui a San Luis había un loco que tenía este
firmware puesto en un NanoStation). Me fijé si era compatible con el
router que me había comprado yo (`Linksys
WRT54Gv8 <http://en.wikipedia.org/wiki/Linksys_WRT54G_series>`__) y
efectivamente decía que funcionaba.

Seguí las instrucciones del wiki de la `página oficial del
firmware <http://dd-wrt.com/wiki/index.php/How_To_Flash_the_WRT54Gv8>`__
y la verdad que salió *todo bien* hasta cierto punto :S . Lo primero que
hice fue llevar el router al trabajo ya que ahí hay UPS y quería
asegurarme de que no se me corte la luz mientras estoy haciendo la
transferencia del firmware, asique ni bien pude llevarlo me puse manos a
la obra.

Cuando llegué, le comenté a Cristian (uno de los que labura conmigo) y
de paso le pregunté si me daba una mano y apoyo *emocional* para llevar
adelante semejante **riesgo** (el router me salió $212 y los podía
perder en menos de 2 minutos :) ). Enchufamos todo en la UPS, rezamos 3
padres nuestros y nos pusimos manos a la obra. Luego de enchufar todo
como corresponde, configuré la IP en mi máquina y agregué el *Default
Gateway* como bien decían las instrucciones. Hice ping, andaba. Luego
resetié el router y cuando volví a entrar con el Firefox a 192.168.1.1
me apareció un mensaje de actualización del firmware, que si mal no
tengo entendido este es de Linksys todavía.

En este momento se le sube el *workskiller* que, para mí, lo que hace es
eliminar el firmware original e instala un servidor FTP para poder luego
pasarle el binario del firmware. A este programita hay que dejarlo
trabajar por lo menos 2 minutos, aunque cuanto más tiempo se deja
trabajar parece que es mejor.

Una vez que pasó este tiempo, me empecé a poner bastante nervioso, no sé
porqué... Pero ya estaba entrando en estado de *trance.*\ Una vez que
pasé este estado, intenté seguir leyendo las instrucciones y llevar
adelante el **flasheo** del router. Por lo que primero me fijé si seguía
*vivo* haciéndole un ping común y corriente a 192.168.1.1 y... Por
suerte me contestaba. ¡Iupi!

Ahora venía el paso de copiar el binario por **tftp** (Trivial FTP) que
es lo que *me instaló* el workskiller que corrí antes. El comando figura
en la wiki del firmware, pero al correrlo me entero que no tengo ese
programa, asique los nervios aumentan. Desconecto el cable UTP, enchufo
el otro (del laburo, para poder tener internet), bajo el programa y por
las dudas también el **atftp** que es otro cliente que recomienda la
wiki para utilizar en caso de que el anterior falle.

Una vez descargado esto, desconecto los cables y conecto nuevamente,
reconfiguro la red indicando cual es mi nuevo IP y toda la historieta
esa que tuve que hacer en el primer paso del flasheo del router.
Entonces, veo que sigo teniendo ping contra el router. Me pongo contento
por un rato y vuelvo a probar ejecutar ese comando y... Me entero que no
está soportado el método *octet* o no sé qué problema tenía con ese
parámetro (la verdad en este momento no recuerdo, pero estaba recontra
caliente/nervioso). Asique, pruebo el otro comando (atftp), y me da que
no se puede conectar al host. ¿Qué hice? Me mandé a *hacerlo a pata*,
osea, nada del otro mundo: en vez de poner todo el comando en una sóla
línea, entré por tftp al router y los fui poniendo de a uno, pero el
**comando del modo** no me lo tomaba, me daba un error. Asique me mandé
a transferirlo igual haciendo "*put* bla bla" y... Lo transfirió.

Sigo leyendo el wiki, ahora ya un poco más tranquilo, y veo que dice que
en el próximo minuto o minuto y medio debe reiniciar el router y bootear
el nuevo firmware. ¿Ya está? ¿Así de fácil era? ¿Tanta preparación para
esto? Y si, bueno... Esto por supuesto que no pasó, con la leche que
tengo yo, era **muy obvio que no iba a pasar esto**, siempre dije que me
tendría que haber dedicado a otra cosa. Bue, dejando estos comentarios
de lado, me puse muy nervioso y Cristian que me hacía dos o tres
comentarios sobre como seguir me hacían poner más nervioso, por suerte
no lo demostraba e intentaba mantenerme tranquilo por fuera.

Hablando un *toque* más tranquilo con Cristian llegamos a la conclusión
que quizás sea una buena idea quitarle la energía y que se reinicie,
entonces podía llegar a levantar el nuevo firmware de forma correcta.
¡Qué iluso por Dios! Por supuesto que lo que pasó no fue esto ¿No? Sino
que empezó a hacer luces muy extrañas, parpadeando muy muy rápido la luz
en dónde tenía enchufado el UTP (puerto 1). Para este momento ya me
importaba un corno el router, había sufrido lo suficiente como para
ponerme mal y mi activo ya se había ido a la mierda (en este momento
recordé que me había gastado más de $300 en el tapizado de un sillón, ya
me importaba todo un pepino).

Volví a conectar todos los cables como corresponde para poder tener
internet y seguí leyendo el wiki, busqué la página en la que hablaba de
`cómo recuperar el
router <http://dd-wrt.com/wiki/index.php/Recover_from_a_Bad_Flash>`__ de
una ***Bad Flash*** :D . Era justo lo que necesitaba. Habla de un **Hard
Reset** y luego de esto sobre un juego de luces interesantes, que
indican el problema que puede llegar a tener el router de acuerdo a como
parpadeaban las luces. La cuestión es que hice todo esto y estaba en el
caso 1: *la luz del puerto 1 parpadeaba por más de 2 minutos sin parar y
nunca se prendían las otras luces y que si podía hacerle ping tendría
que intentar mandarle por TFTP nuevamente y sino hacer un cable que se
llama JTAG* (ni idea esto). Como ping no podía hacerle, osea, hacerle
si, pero el muy guacho no me contestaba. Empecé a leer que bosta era eso
del JTAG, no cazé una y me dí por vencido al menos por ese día.

Pasaron algunos días y yo seguía leyendo como hacer para recuperarme de
la paliza que me había dado el Linksys. Al final caí en el foro de
dd-wrt y `encontré que un loquito tenía un problema muy similar al
mío <http://www.dd-wrt.com/phpBB2/viewtopic.php?t=20095>`__. El vago es
**matt0401**, había hecho los pasos y **manteca**. No pasó nada.
Siguiendo el hilo veo que comenta que encontró la solución y que no la
sabe, pero que tampoco le importa saberla, que no le interesa nada pero
que estaba re contento que lo había recuperado.

Dicho y hecho, hice lo que decía él: *copiar por tftp dos veces más el
binario porque a la tercera le funcionó.* Enseguida el router empezó a
funcionar, se prendieron las luces correspondiente y estaba entrando con
el Firefox al HOME del dd-wrt. **¡Done!** Canté victoria como loco. De
acá en adelante: todo joya. El driver se zarpa, tiene varias cosas que
no tiene el original. Lamentablemente, como Linksys amarretea la RAM de
este dispositivo tuvieron que sacar algunas cosas los muchachos, por eso
esta es la versión **micro** del driver. Por ejemplo, no tengo SSH, pero
sí TELNET.

Asique bueno, tengo un par de tardes para probar configuraciones medias
locas antes de entregarle el router a mi pobre madre que casi se muere
cuando le dije que estaba roto cuando se lo llevé. No entendía nada, me
dijo que parecía que era nuevo, que qué le pasaba que estaba roto :D
