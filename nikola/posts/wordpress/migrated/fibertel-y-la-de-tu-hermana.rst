.. link:
.. description:
.. tags: fibertel, internet
.. date: 2011/07/14 11:50:09
.. title: Fibertel y la ... de tu hermana
.. slug: fibertel-y-la-de-tu-hermana


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2011/07/14/fibertel-y-la-de-tu-hermana/


Si bien escribí que uno puede ser dueño de su conexión a Internet en un
`post
anterior <http://humitos.wordpress.com/2011/07/08/se-dueno-de-tu-conexion-fibertel/>`__,
antes de ayer me dí cuenta que uno no es dueño de nada, ni siquiera de
lo que paga, compra, o adquiere y se lo lleva hasta su propio hogar. Es
más, ni siquiera somos dueños de nuestra propia vida. Pero bueno, ese es
un tema aparte.

El Martes pasado me quise conectar a IRC con el programa que
habitualmente uso: Konversation. No hubo ningún problema alguno con la
conexión y el ingreso a los diferentes canales que entra de forma
automática. Una vez logueado y habiendo entrado a los diferentes
canales, noté que a lista de usuarios conectados en cada uno de los
canales *freakeaba*\ mal, y mostraba cualquier cosa. Veía gente que
estaba en varios canales cuando sólo estaba en uno de ellos.

Poco tiempo más tarde, empecé a notar que tenía muuucho lag. Algo así
como 150 segundos sin respuesta desde el servidor, y por lo tanto se me
desconectó después de un ratito más. Seguí intentando ver qué pasaba,
pero no había caso. El problema venía por otro lado.

Lo primero que hice fue probar con otro cliente de IRC, ahí lo llamé a
mi amigo personal "el" **irssi**. Un programa de consola muy completo.
Lo inicio, se conecta (aunque demora bastante), hago *join* a algunos
canales y no me muestra la lista de usuarios por un rato más que largo.
Pasado este tiempo (rato largo) aparecen los usuarios conectados al
canal y empiezo a chatear, pero nunca nadie me responde. Después de un
tiempo empiezo a ver que tengo lag con el irssi también, así que más que
descartado que el problema no era del cliente.

En este momento, pongo un mensaje en el Facebook diciendo que desde que
tengo Fibertel el IRC me anda como el orto. Ahí es dónde entra
**perrito666** y la parte interesante de esta movida. El loco me dice
que haga un *mtr* hacia freenode.net para ver dónde se están muriendo
los paquetes. Así que, eso hice:

|image0|\ mtr irc.freenode.net

|image1|\ mtr calvino.freenode.net

Bueno, para los que entienden algo... Esto es muy útil. Yo no me voy a
poner a explicar qué pasa y porqué ni todas esas cosas que seguro que
ustedes ya lo saben :P

La cosa es que el tipo inteligente este (apodado perrito666) que pruebe
conectándome mediante SSL y me pasó este
`link <http://freenode.net/faq.shtml#sslaccess>`__. Busqué en Google
como hacer para conectarme por SSL con el irssi y caí a `este
sitio <http://ubuntu-tutorials.com/2010/01/30/accessing-freenode-irc-network-via-ssl-secure-connection/>`__.
Que básicamente dice que use este comando:

    ``/connect -ssl_verify -ssl_capath /etc/ssl/certs chat.freenode.net 7000``

Intenté conectarme y luego unirme a varios canales y **voilá**, todo
empezó a funcionar correctamente y ya estaba chateando con toda la gente
que tanto me quiere en IRC ( :S ). Le comenté a la mente pensante esta y
me dijo que seguramente yo estaba detrás de un proxy transparente. ¿Lo
qué? Así que puse en Google, "Proxy Transparente Fibertel" y caí a `esta
nota <http://blog.smaldone.com.ar/2006/10/12/fibertel-y-su-proxy-transparente/>`__
muy interesante en dónde explican exactamente qué pasa con Fibertel y el
proxy transparente.

Después de todo, pude conectarme por IRC usando SSL. Está bien, Fibertel
no te dice nada de esto, lo tapan, y qué se yo cuantas otras cosas. La
verdad que eso es una cagada, pero bueno, por suerte hay una "solución".
Claro, sin darse de baja al servicio.

.. |image0| image:: http://humitos.files.wordpress.com/2011/07/mtr.jpeg
   :target: http://humitos.files.wordpress.com/2011/07/mtr.jpeg
.. |image1| image:: http://humitos.files.wordpress.com/2011/07/mtr1.jpeg
   :target: http://humitos.files.wordpress.com/2011/07/mtr1.jpeg
