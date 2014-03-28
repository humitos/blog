.. link:
.. description:
.. tags: django, facebook, internet, trabajo
.. date: 2010/09/18 18:51:56
.. title: Facebook App
.. slug: facebook-app


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2010/09/18/facebook-app/


Si bien Facebook no me gusta mucho, más que nada **por el uso que la
gente le da**, y no porque sea una aplicación que no me gusta; de hecho,
me parece que es muy groso y fue revolucionario.

Fue tan revolucionario que la gente quiere hacer aplicaciones para que
se vean dentro de Facebook y además que sus sitios estén conectados con
Facebook de alguna manera: login mediante tu usuario de Facebook, que se
publique en tu muro la actividad que estás llevando a cabo en otro
sitio, y cosas similares. Digamos, todo el mundo quiere integrar
Facebook a su sitio.

Bueno, para este tipo de integración se requiere registrar una
**aplicación en Facebook** mediante un nombre, un desarrollador,
información de contacto, url de la aplicación y demás. Por otro lado, se
puede hacer que la aplicación que el desarrollador registra funcione
"dentro" de Facebook o que sólo sean una redirección al sitio de la
aplicación.

Hace un tiempo atrás trabajé para un sitio que se llama
`Listuc <http://www.listuc.com>`__ (es sobre boliches de Barcelona,
España) y necesitábamos que el usuario se pueda loguear en Listuc con su
cuenta de Facebook, dándole permisos a Listuc para poder recibir mails
de este y publicar cosas en su muro.

Para eso tuvimos que registrar una aplicación **que no funcionaba dentro
de Facebook**\ pero que sí necesitaba usar a Facebook para obtener
determinados datos del usuario y como no necesitábamos mostrar algo
dentro del sitio de la app (dentro de Facebook) le indicamos que haga
una redirección hacia el *home* hacia el sitio de Listuc. Luego
utilizamos la API que Facebook brinda para hacer todo el manejo desde
nuestro sitio.

Hoy en día, unos meses más tarde de esto, estoy trabajando en una
aplicación de Facebook que necesitamos que se vea dentro de Facebook.
Por lo tanto hay que registrar una aplicación Facebook e indicarle esto.
La forma de "funcionar dentro de Facebook" es así:

|image0|

En la parte de la pantalla que se ve blanca en el screenshot anterior es
dónde Facebook *te deja* meter tu aplicación web. Pero claro, otra vez:
"para obtener datos del usuario y demás cosas relacionadas con Facebook
debemos registrar la aplicación". Entonces, fui a la `sección de
desarrolladores <http://developers.facebook.com/?ref=pf>`__ que tiene
Facebook e intenté registrar una nueva aplicación para empezar a
programarla pero me encontré con este mensaje:

    Tu cuenta deber ser verificada antes de que puedas realizar esta
    acción. Por favor, verifica tu cuenta añadiendo tu teléfono móvil o
    tu tarjeta de crédito.

Anteriormente, cuando registré la aplicación que necesitábamos en
Listuc, no me apareció este cartel sino que fue más directo y no tuve
que hacer mucho más que lo que comenté para registrarla.

Bueno, fui al link que me mostró ahí para verificar mediante el teléfono
móvil, puse mi teléfono y le pedí que me mande el código de confirmación
(esto fue el Jueves). Esperé un rato que me llegue el código y no pasaba
nada. Hablé con el PM del proyecto, dimos un par de vueltas, probamos
varios celulares (todos de Personal) y no tuvimos chance, pasaba siempre
lo mismo: "a nadie le llegaba el código".

Ese mismo día llamé al \*111 de Personal para comentarle el problema y
para que me digan si sabían algo o si este servicio había dejado de
funcionar para Personal y en la página de Facebook aún no estaba
actualizado o algo por el estilo. Me dijeron que no era problema de
ellos, que el servicio está habilitado y que por las dudas pruebe con
otros números del centro de mensajes. Me dió unos cuantos números para
probar, pero no anduvo con por lo menos 3 de ellos.

Hoy me puse a navegar y a pensar algunas cosas del trabajo y terminé de
nuevo en esa página, así que me propuse probar de nuevo y v\ *oilá:*\ me
llegó el código de confirmación. Por lo tanto pensé que iba a poder
registrar la aplicación que quería pero...

... luego de configurar todo lo que me pedía del celular e incluso
probar mandando un SMS para actualizar mi estado (y que funcione) voy la
`URL que es para registrar una nueva
app <http://developers.facebook.com/setup/>`__ y me dice:

    Tu cuenta deber ser verificada antes de que puedas realizar esta
    acción. Por favor, verifica tu cuenta añadiendo tu teléfono móvil o
    tu tarjeta de crédito.

¡Lo mismo que antes! Entonces, ¿en qué quedamos? ¿para qué registré mi
teléfono y gasté dos mensajes mandando códigos y letras a Facebook?

¿Alguien ha registrado una app de Facebook actualmente? ¿Cómo lo han
hecho?

.. |image0| image:: http://humitos.files.wordpress.com/2010/09/facebook-app.jpeg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/facebook-app.jpeg
