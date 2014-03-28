.. link:
.. description:
.. tags: juegos, software libre
.. date: 2008/06/14 19:17:12
.. title: OpenArena
.. slug: openarena


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2008/06/14/openarena/


Ayer me dieron ganas de jugar un rato a los videos juegos para matar el
tiempo y para *aprovechar* la placa 3D que tengo. La verdad que hacía
una cantidad que no jugaba absolutamente a ninguno y me sorprendí cuando
ví que mantengo el nivel ... :)

Me puse a buscar juegos para Linux y como desde hace tiempo estoy
suscrito por RSS a `LinuxJuegos.com <http://www.linuxjuegos.com>`__,
empecé por fue buscar ahí. Ahí están todas las novedades de las cosas
relacionadas con los Juegos para Linux, desde drivers hasta Pyweek's. Y
mucho más.

Encontré el OpenArena que parecía que tenía unos gráficos piola y es el
clon del Quake 3 Arena que ya lo conocía. Lo busqué con **apt-cache
search openarena** y estaba, asique lo instalé desde ahí. Pesa unos
280Mb.

Jugué un ratito para probarlo y me mandé a jugar en internet. Pero no me
fue muy bien, tenía mucho PING (algo así como ~250) y se notaba
bastante: cuando yo disparaba el otro tipo ya se había corrido de donde
estaba, entonces se hacía bastante difícil. Igualmente el nivel que
manejan los flacos que están ahí es otro totalmente distinto al mío.

Como me cansé de perder y perder, no sé si debido al PING o porque soy
malo a comparación con ellos, me puse un servidor en mi casa para este
juego, para que juguemos entre amigos o los que estemos cerca de Santa
Fé (la mayoría de los servidores están afuera del país y tienen mucho
PING).

Lo probé con algunos amigos y tiene entre 20-50 de PING que es bastante
razonable para jugar. Además lo bueno de este juego es que no necesita
mucha PC, los requerimientos son extremadamente mínimos: ni siquiera
placa 3D (que era lo que yo quería usar :( ).

Aunque yo lo instalé desde los repositorios, es **recomendable**
descargarlo desde el `sitio oficial, <http://www.openarena.ws/>`__
porque después hay que aplicarle un parche y se complica bastante sino.
De esta forma para aplicar el parche hay que descomprimirlo
sobreescribiendo todos los archivos, y listo.

Para jugar en mi servidor hay que entrar en modo **multiplayer** y
elegir **specific**. Luego como host: **humitos.homelinux.net**\ y como
puerto **27960**.

Como no podía ser de otra manera, `me hice un script en
Python <http://grulicueva.homelinux.net/~humitos/blog/openarena/nuevo-server.py>`__
para saber quienes están conectados al servidor cada X cantidad de
minutos :) . Este se conecta con un sitio el cual informa los servidores
activos y quienes están jugando. Parsea este resultado y utiliza
**aosd_cat** para mostrarlo en pantalla. ¿Que tul?. (la idea de usar
aosd_cat se la robé a Gastón :P )

    *... escucho sugerencias...*
