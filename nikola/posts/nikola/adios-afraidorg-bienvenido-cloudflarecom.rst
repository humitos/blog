.. title: Adios afraid.org, bienvenido cloudflare.com
.. slug: adios-afraidorg-bienvenido-cloudflarecom
.. date: 2015-01-02 22:32:18 UTC-03:00
.. tags: avast, blog, dns, windows, hosting, antivirus, cloudflare, afraid
.. link: 
.. description: 
.. type: text

El problema
-----------

Durante más de un año tuve mi blog bloqueado por Avast! y no lo
supe. Luego, cuando varios usuarios me comentaron que al entrar a mi
blog el Avast! les decía que tenía virus, revisé si tenía algún
javascript que podía estar molestando o algo similar (supongo que no
es necesario aclarar que mi blog no tiene virus) y no encontré nada.

Un tiempo después, hice varios reclamos por email a Avast!
comentándoles qué estaba pasando y no recibí ninguna respuesta, así
que mi investigación terminó ahí ya que no supe qué hacer.

Cuando empecé a viajar con `Argentina en Python <https://argentinaenpython.com/>`_ y pasaba la
dirección de mi blog, la mayoría de la gente que intentaba entrar
desde los hostels desconfiaba de lo que yo le decía y le creía más a
su antivirus. Por eso, decidía no entrar al sitio.

Eso me preocupó un poco y :doc:`busqué una solución <bloqueo-avast>`,
pero era necesario la interacción del usuario y un pequeño
conocimiento de cómo se usa el Avast! y, de hecho, si el usuario tenía
ese conocimiento además tenía que confiar más en mi palabra que en la
del Avast! (que es un problema que va para un post aparte).

Igualmente, esa solución era temporal y yo quería que, al menos los
que confiaban en mi, no tengan que hacer ese laburo cada vez. Así que,
gracias a mi hermano, llegué a :doc:`esta otra solución
<solucion-al-bloqueo-de-avast>` mientras yo seguía mandando emails a la
gente de Avast!.

Afortunadamente, luego de insistir bastante por su formulario de
contacto y pedirle a varias personas que reporten un falso positivo en
mi blog, ellos me contestaron. ¿Qué me dijeron?. Básicamente que mi
blog había sufrido `DNS Hijacking
<https://en.wikipedia.org/wiki/DNS_hijacking>`_. Así que, luego de
investigar de qué se trataba eso, les volví a mandar un mail y les
pregunté qué podía hacer yo para revertir la situación y que quiten mi
dominio de su lista negra.

La respuesta
------------

::

   Any domain hosted on afraid.org can be used by other persons for
   dns hosting without your control.

   It happened for your domain, it was misused for malicious
   purposes - in that case, when nobody has control on subdomains of
   domain (DNS hijacking), we block the whole domain in order to
   protect our users.

   For you, the solution is most probably only changing the dns
   hosting and letting us know later.

Esto quiere decir que me tenía que mudar de *afraid.org*, y como yo no
estaba contento con eso ya que el servicio que ofrece afraid.org me
gustaba y me parecía cómodo para mudarse de servidor fácilmente, les
dije que no me quería mudar y que me expliquen un poco más el porqué
de la cuestión.

Me dijeron que por la forma en la que funciona afraid.org el problema
de DNS hijacking no tiene solución. Esto es básicamente por la forma
en la que `funciona afraid.org <http://freedns.afraid.org/faq/#3>`_:

#. Creás un dominio en afraid.org
#. Cualquier usuario puede crear un sub-dominio en tu dominio sin
   autorización (por más que el dominio sea "Private")

Eso, a la gente de Avast! no le gusta nada ya que dicen que vos no
tenés control sobre tus dominios. Lo cual, tiene un poco de sentido
aunque no debería estar reportado como un virus y sin brindarle nada
de info al usuario ni siquiera una forma de visualizarlo de cualquier
forma.

La solución
-----------

Me mudé a `Cloudflare <http://cloudflare.com>`_ que si bien es un CDN,
también se puede usar únicamente como servicio de DNS. Que es como lo
estoy usando yo ya que CDN no quiero / necesito por el momento.

Cloudflare me resultó sencillo de entender, de configurar y también
puedo decir que por el momento no he tenido ningún problema.
