.. title: Red Libre
.. slug: red-libre
.. date: 2015-09-16 13:34:56 UTC-03:00
.. tags: red libre, argentina en python, wifi, proyecto, software libre, bolivia, copacabana
.. category: 
.. link: 
.. description: 
.. type: text

Viajar te abre la cabeza. Constantemente uno está conociendo personas,
aprendiendo sobre otros estilos de vida y también entendiendo sus
*negocios* para conseguir dinero y así poder seguir adelante con sus
sueños.

También uno se encuentra con personas más estáticas, que trabajan
fuerte en un mismo lugar todos los días para implementar una idea en
particular en esa zona y así construir una red de contactos entre
personas, brindar un servicio o mejorar algo existente, promover la
cultura local y revolucionar todo lo que se pueda. Hay de todo. En
todo el mundo y hasta en los lugares menos pensados.

La motivación
-------------

Durante el último tiempo conocí el proyecto `mARTadero
<http://martadero.org/>`_ en Cochabamba, Bolivia en donde están
construyendo un `Barrio Hacker <http://barriohacker.net/>`_ y que
además aloja al `HackLab Cochabamba <http://hacklabcbba.org/>`_. En
este lugar aprendí muchísimas cosas, desde lo social hasta lo técnico
y también su combinación. Su uso adecuado e inteligente de la
tecnología. Todo esto, lo sume a mis ideas y empezó a gestarse algo...

Luego, llegamos a La Paz, Bolivia y conocimos a los chicos del
`r00thouse <http://hacklab.org.bo/>`_, un HackLab en el que
actualmente están construyendo una Red Mesh desde cero y con muy poco
conocimiento en el tema. Han estado estudiando muchísimo los últimos
meses y lograron montar dos nodos: conectaron la Universidad con su
propio HackLab. Con ellos hablamos sobre el impacto social que esto
podría tener y cómo hacer que los servicios actuales sean más
visibles. También les comenté todo lo que había aprendido en
Cochabamba con la experiencia del Barrio Hacker y el HackLab. Agregué
también un punto de vista más social y no tan técnico (que es lo que
nos gusta y más fácil nos sale) para acercar la tecnología a las
personas no-técnicas, facilitándoles su uso y su entendiemiento sobre
las mismas. Así, entendiendo como funciona y su porqué, podrán decidir
si les va a ser útil o no.

Hoy me levanté mirando el cerro *Calvario* en Copacabana, Bolivia y me
puse a leer un libro que me prestó `Facundo Batista
<http://taniquetil.com.ar/>`_ en mi visita al :doc:`asadogeek-2015`:
"Redes inalámbricas en los países en desarrollo". Luego de leer unas 4
o 5 páginas, me hizo un cortocircuito dentro de mi cabeza y me llegó a
mezclar todas estas experiencias que habíamos estado escuchando y
llegué a un nuevo proyecto de "Red Libre".


.. TEASER_END

La idea
-------

Consiste en armar una red WiFi en las ciudades que visitemos con
`Argentina en Python <https://argentinaenpython.com/>`_ y ofrecer
diferentes servicios además de dar a conocer el proyecto. Notamos que
la mayoría de los turistas que recorren la ciudad, en algún momento,
están en busca de WiFi para conectarse con sus amigos, buscar lugares
para comer, hoteles o turismo, conocer personas locales y demás. Eso
nos pareció un buen punto de partida para dar a conocer, *sin
esfuerzo*, lo que hacemos cotidianamente y así sumar más personas a
esta locura.

Pero claro, ofrecer *solo eso* me parece que era poco y que podríamos
sacarle mucho más provecho a una red WiFi. Es por eso que queremos, en
principio, tener estos servicios disponibles de forma gratuita para
quienes se conecten a esta red (en modo offline):

* Nuestros blogs (el blog de humitos, Química & Nómada) [#]_
* Sitio web de Argentina en Python
* CD-Pedia en su formato DVD
* Chat mediante IRC / Bonjour o similar
* Buscador de POIs mediante upoi.org
* Maps.me, OSMAnd y sus correspondientes mapas

Todo esto de forma offline y disponible para todos los que puedan
conectarse a la red. Una vez que los usuarios se conecten e ingresen
*google.com*, por ejemplo, en vez de mostrarse el sitio de Google se
les mostrará una página con una explicación detallada sobre el
proyecto de Red Libre y los servicios que están disponible.

De esta forma, podrían chatear entre los que estén conectados y
cercanos, conocerse entre ellos y juntarse a tomar una birra en el bar
de al lado. Coordinar para ir a hacer una excursión juntos o lo que se
les ocurra que cualquier comunicación pueda brindar. Leer sobre
nosotros y nuestros blogs en caso de estar aburridos y tener que hacer
tiempo a que salga su bus, leer diferentes artículos de Wikipedia
sobre el lugar en el que se encuentran, conocer nuestros proyectos y
sumarse a la causa, buscar un montón de información sobre lugares
interesantes en la ciudad mediante OpenStreetMap y también llevarse
esos datos en su celular para luego consultarlos en modo offline.

Suena interesante, ¿no?

¿Cómo montaríamos esto?
-----------------------

En todas las ciudades hay lugares que son muy transitados por turistas
que están buscando donde alojarse, qué comer o bien conocer cuáles son
las actividades de esa ciudad. Esos son lugares claves para montar
esta red WiFi Libre y dar a conocer nuestros proyectos y también
ofrecer un servicio gratuito y de utilidad (además, estaríamos dando a
conocer varios proyectos de Software Libre que no son fáciles de
acercar al público general). La idea es llegar a esos lugares en auto,
conectar nuestro router WiFi (Ubiquiti) a la batería del auto junto
con el servidor (RaspberryPi) y su disco externo con los datos. Esto
hace que sea totalmente transportable y que podamos alcanzar cualquier
lugar de la ciudad [#]_.

En el lugar que estacionemos el auto, podríamos poner la bandera de
`Argentina en Python <https://argentinaenpython.com/>`_, una mesa,
sombrilla y sillas para dar a conocer lo que hacemos, entregar
micro-tutoriales, difundir estas herramientas y ayudar a la gente a
configurar/instalar las apps en sus celulares. También, si tenemos un
evento pactado en esa ciudad, podríamos hacer difusión en este mismo
lugar.

Conclusión
----------

Creo que de esta forma estaríamos acercando un montón de servicios y
utilidades a muchas personas sin quizás tener interacción alguna en
primera instancia. Mostrando el Software Libre como alternativa a
muchas herramientas cotidianas que usamos sin tener conciencia alguna
sobre nuestros datos y llegar a charla más que interesantes.

Además de darnos una visibilidad más fuerte en la ciudad que nos
encontramos y así poder conseguir ayuda y contactos para seguir
adelante con nuestras locuras itinerantes :)

Al día de la fecha no tenemos el router WiFi Ubiquiti ni la
RaspberryPi que necesitamos. Podés ayudarnos a tomar una decisión
sobre qué modelo nos conviene comprar para obtener un mejor servicio,
como así también `económicamente para comprar estos dispositivos
<https://argentinaenpython.com/donaciones/>`_.

Nos encantaría leer/escuchar comentarios y sugerencias sobre qué otros
servicios podríamos brindar en esta Red Libre y así acercar más
información a usuarios pasajeros.

¡Muchas gracias!

.. [#] Podríamos tener muchos otros blog también aquí
.. [#] Incluso, en un futuro se podría disponer de una batería extra
       para no depender de llevar el auto a ese lugar
