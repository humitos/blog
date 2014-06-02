.. link:
.. description:
.. tags: fibertel, internet, telecom
.. date: 2011/07/08 22:32:33
.. title: Sé dueño de tu conexión Fibertel
.. slug: se-dueno-de-tu-conexion-fibertel


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2011/07/08/se-dueno-de-tu-conexion-fibertel/


Antes de ayer pedí (bah, **me hincharon tanto las pelotas** que terminé
aceptando) el servicio de Fibertel 3Mb + Cablevisión Digital. Hacía
mucho que veníamos a las vueltas con mi vieja, que sí, que no y qué se
yo. Pero Arnet siempre tenía algo.

Una cosa que me preocupaba era el tema de abrir puertos con Fibertel, ya
que yo necesito poder ingresar a mi PC desde afuera (SSH, Apache,
Django, Pylons, JDownloader y demás). Digamos, quiero hacer lo que se me
canta el culo con mi conexión, es mía y pago por eso. Bueno, acá el tema
es que Arnet **siempre me dijo que esto no se podía hacer**. Sin
embargo, investigando en internet encontré varias cosas para hacer,
desde el password del router hasta como flashearlo. Y bueno, esto
finalmente lo pude hacer con Arnet sin problemas.

Siendo que esto me preocupaba, decidí que la próxima vez que me llamen
para ofrecerme este servicio lo iba a matar a preguntas al pibe y que de
última me diga que no sabía o que sí o lo que sea. Pero yo quería dejar
en claro las cosas que quería hacer con el servicio que estaba
contratando, siendo que con Arnet lo podía hacer y si ellos no me
ofrecían lo mismo o mejor no me iba a cambiar.

Finalmente, decidimos decir que sí, por lo menos se iban a dejar de
romper las bolas. El tipo que me llamó preguntó las 1000 y 1 preguntas
que le hice a su supervisor y muchas me dijo que "sí sí" como a los
locos y otras me las supo explicar un poco más, pero que igualmente,
hable con los pibes que me iban a hacer la instalación para estar 100%
seguro :) (lavate las manos)

Hoy por la mañana vinieron los pibes y **lavate las manos**\ de nuevo.
Me dijeron que yo podía hacer todo lo que Fibertel me había ofrecido,
que ellos no sabían nada de eso: "*Nosotros sólo hacemos la instalación,
tiramos los cables digamos. Si yo te digo que la instalación va sin
cargo y ellos después te la cobran, me vas a putear a mí. Yo no sé eso,
si te dijeron A es A.*\ "

"*Ok, vos instalalo y yo después me arreglo con ellos. De última, lo doy
de baja*\ "

Se pasaron por lo menos 2 horas los pibes acá haciendo la instalación y
hablando al pedo conmigo. Uno era medio pistero y fan del 147, y como yo
la tengo re clara de autos :P , hablamos un montón.

Listo! Ya tenía Fibertel 3Mb... Uhhh, como anda! :P Seee, se nota un
poco que anda más rápido, pero no es la gran cosa. Los pibes me dijeron:
"*Esta es la clave del Wifi y el nombre de la red es Fibertel WiFi.
Cualquier cambio que quieras hacer entrá a la Sucursal Virtual*\ ".

Se fueron los pibes y lo primero que probé fue entrar a
http://192.168.0.1 y nada. Busqué en Google y encontré en Taringa! que
la dirección era http://24.232.0.118/ y había que usar el **número de
serie del modem / router Motorola** como **usuario** y el **número de
cliente** como **contraseña.**\ Al final no era el número de serie, no
sé qué es el número, pero me había quedado grabado en el Firefox por
suerte. La contraseña sí es el número de cliente.

Estaba re contento pero lamentablemente desde ahí no se puede hacer
nada. Así que, de vuelta a Google y a Taringa! como loco. Busqué, busqué
y ¿viste que el busca siempre encuentra?:
`encontré <http://www.taringa.net/posts/info/5251453/Solucion-Fibertel-Wifi_-Conecta-mas-pc_s_-notebooks_-etc.html>`__!

Siguiendo ese post de Taringa terminé haciendo estos pasos:

#. Desenchufar todos los cables del Modem / Router
#. Mantener presionado  el botón de **reset** (que es muy chiquitito y
   no dice nada al respecto) que se encuentra en la parte de atrás cerca
   de la alimentación. Esto lo hice con la herramienta mágica: un clip
#. Conectar el cable de alimentación
#. Esperar que las luces hagan su gracia (parpadean todas juntas después
   de unos 10-15 segundos)
#. Conectar una PC por el cable de Red que trae
#. Ingresar a http://192.168.0.1
#. Poner los datos de usuario: **admin** y contraseña: **motorola**
#. |image0|

Ir a **Advanced -> Options** y luego **des-tildar**\ la
   opción **WAN Blocking**
#. |image1|

Luego ir a **Advanced -> Forwarding** y habilitar
   *tooooodos*\ los puertos que se te canten. Yo acá puse la dirección
   de IP (que después de la asigno de forma estática mediante el Modem /
   Router de Fiberter - Motorola) del router Linkys al cual conecto el
   RJ45 (cable de red del Motorola) en la interface de WAN
#. |image2|

En **Basic -> DHCP** le asigno la dirección de IP de forma
   estática al router Linksys poniendo su MAC y la dirección de IP que
   le quiero asignar. En este caso 192.168.0.2
#. |image3|

Por último le cambié el SSID (nombre de la red WiFi) en
   **Wireless -> Primary Network**
#. |image4|

Me desloguié con **Logout** y luego le quité el cable de
   energía nuevamente al Modem / Router de Fibertel
#. Ubiqué todo como quería quede finalmente (*ojo, una vez que le
   colocás el cable de Internet -el coaxil- no podés entrar más a este
   panel de administración. Por lo tanto te recomiendo que hagas todo
   bien de la primera, sino hay que hacer todo de nuevo. También te
   podés guardar un Backup de la configuración de tu Modem / Router en
   la sección **Basic -> Backup***) y coloqué el cable coaxil
#. Demoró *bastante*\ en iniciar y finalmente tengo todo configurado
   como corresponde

Por las dudas, mi **Modem / Router es el Motorola SBG901**:

|image5|

*Bueno, nada más. Espero que se entienda y que sea de utilidad para
todos los que **ahora** tenemos Fibertel! Culeados, viva Piñón Fijo
carajo!*

**EDITADO 14 de Julio de 2011:** por si te interesa investigar un poco
más, acá tenés el `manual del
router <https://docs.google.com/viewer?a=v&pid=explorer&chrome=true&srcid=0B2rKoqZVq0cPNzI5MzI0ZGUtNjM2Mi00NTBlLThiMzEtZjYwNDk0ZDE3NDRk&hl=en_US>`__.
Si encontrás algo copado, por favor dejá un comentario acá, así nos
enteramos todos. Gracias!

**EDITADO 21 de Julio de 2011:** hablando con un amigo (Nicolás "Casi
Ingeniero" Mascardi) me dijo que me fije si el Router lo podía
configurar con DMZ y así evitar muchos de los pasos anteriormente
mencionados. Hoy le dediqué un tiempo para ver qué es esto y, además de
descubrir que se puede, llegué a la conclusión que es exactamente lo que
necesito: *básicamente forwardea todos los puertos de la WAN a una IP
fija de la LAN que vos le digas*. Joya, acá está la información tomada
del manual de cómo hacer esto (recordar que hay que quitar el coaxil,
resetear el router y luego entrar en el admin del Motorola). Bueno,
basícamente configuré el IP de mi router Linksys para que mande todo
hacia ahí y ahora la administración de los puertos la hago desde el
Linksys ;)

|image6|

*"si hubiese terminado la carrera, sabría hacer esto"*

.. |image0| image:: http://humitos.files.wordpress.com/2011/07/pantallazo.png
   :target: http://humitos.files.wordpress.com/2011/07/pantallazo.png
.. |image1| image:: http://humitos.files.wordpress.com/2011/07/pantallazo-2.png
   :target: http://humitos.files.wordpress.com/2011/07/pantallazo-2.png
.. |image2| image:: http://humitos.files.wordpress.com/2011/07/pantallazo-3.png
   :target: http://humitos.files.wordpress.com/2011/07/pantallazo-3.png
.. |image3| image:: http://humitos.files.wordpress.com/2011/07/pantallazo-5.png
   :target: http://humitos.files.wordpress.com/2011/07/pantallazo-5.png
.. |image4| image:: http://humitos.files.wordpress.com/2011/07/pantallazo-7.png
   :target: http://humitos.files.wordpress.com/2011/07/pantallazo-7.png
.. |image5| image:: http://www.generalmanual.com/img/0907/motorola-sbg901-wireless-cable-modem-gateway.jpg
.. |image6| image:: http://humitos.files.wordpress.com/2011/07/dmz-router-motorola.png
   :target: http://humitos.files.wordpress.com/2011/07/dmz-router-motorola.png
