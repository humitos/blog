.. link:
.. description:
.. tags: software libre
.. date: 2009/02/11 22:32:16
.. title: Configurar una placa wifi Airlive wmm3000pci en Debian
.. slug: configurar-una-placa-wifi-airlive-wmm3000pci-en-debian


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2009/02/11/configurar-una-placa-wifi-airlive-wmm3000pci-en-debian/


Resulta que siempre que me hablan de placas wifi y GNU/Linux se me pone
la piel de gallina. Existen muchas placas wifi en el mercado que
actualmente no están soportadas por GNU/Linux, como por ejemplo la
plaquita USB que intenté configurar hace un tiempo atrás y lo comenté en
`otro
post. <http://humitos.wordpress.com/2008/09/21/encore-enuwi-g2-rtl8187b-en-debian/>`__

Hace tiempo que vengo diciéndole a mi jefe que quiero probar las cosas
de Airlive ya que el habla muy bien todo el tiempo de esta marca.
Primero le pedí un router wifi para el proyecto "Santa Fe libre" (que
lamentablemente está bastante muerto) y cada tanto le iba pidiendo
diversas cosas. Lo primero que conseguí fue una remera que entra en la
palma de la mano y *crece* con agua. ¡Sí! Una cosa muy extraña que nunca
antes había visto. Aún no la he agrandado porque lo quiero hacer bien y
de ser posible hacer un videito :)

Bueno, volviendo al tema de la placa wifi. Como comenté en el `post
anterior <http://humitos.wordpress.com/2009/02/02/flashear-router-linksys-wrt54g-v80/>`__
a este, en la casa de mi mamá están haciendo una red wifi. Como la
computadora de mi hermano no tiene placa wifi y la placa USB que probé
en la pc de él no alcanzaba a ver la red, decidí pedirle una placa
Airlive a mi jefe para probar estos productos. Según él están muy bien
vistas en entornos linux y tienen soporte nativo y demás. Asique allá
vamos.

Hoy, cuando llegué a casa después de inglés, me decidí a poner la placa
wifi en la pc de escritorio, tirarme en la cama con la notebook y
configurarla a través de SSH mientras descanzaba un poco ya que estaba
bastante destruído. Bueno, prendí la pc, me puse cómodo, abrí una
consola y... A ver qué sale.

Primero busqué con **lspci** el modelo de la placa ( RaLink RT2600
802.11 MIMO), lo puse en Google y leí algunas referencias sobre la
plaquita. Después pensé: "¿Porqué no estoy haciendo un **ifconfig** o un
**dmesg** para ver cómo me la detectó si es que me la detectó?". Una vez
hecho el **ifconfig** veo que me aparece como *wlan1*. ¡Wow! ¡Buenísimo!

Segundo paso: levantarla y hacer un scan. Cuando levanto la interfaz me
da un error que debido a mi ignorancia no entendía. Asique me puse a
buscar en los paquetes de Debian todo lo que diga "wifi" y encontré uno
que se llamaba **firmware-ralink** asique si no era este le pegaba en el
palo. Lo que podía pasar es que no contenga el firmware exacto para la
versión de chipset que yo tenía pero: "Oh, sorpresa". Cuando levanto la
interfaz y hago un **iwlist scan** me aparece la red wifi de mi casa
(humitos) y una que no sé de quién es (Casa) pero que con todas las
otras placas wifi que he probado en mi casa NUNCA la había visto y
encima con re buena señal, creo que tiene un 50% o le pega en el palo.

Lamentablemente, este paquete parece no ser libre. Aún no he investigado
porqué, qué tiene que no lo hace libre, pero don **vrms** (Virtual
Richard M. Stallman) dice que este paquete NO es libre :( .

Otra cosa que me sorprendio cuando lo probé es que **soporta el modo
monitor** y... *sin chistar*. Funcionó de una, no dijo nada, no se quejó
y estoy empezando a romper las bolas con aircrack. ¡Qué lindo, qué
lindo! ¿Y ahora quién me para? Si se pueden inyectar paquetes me voy a
cagar de la risa....

Ahora a probar cosas raras para gente normal que me quedan pocos días de
prueba en linux; el fin de semana se harán estas cosas (o similares) en
Windows para ver como viene la mano.
