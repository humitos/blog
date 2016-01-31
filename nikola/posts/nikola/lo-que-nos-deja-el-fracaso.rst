.. title: Lo que nos deja el fracaso
.. slug: lo-que-nos-deja-el-fracaso
.. date: 2015-11-03 18:45:50 UTC-03:00
.. tags: red libre, pyfispot, proyecto, python, viaje, perú, mollendo
.. category: 
.. link: 
.. description: 
.. type: text

Aunque crean que mi vida es un éxito por la cantidad de proyectos,
empresas, fundaciones y organizaciones que he fundado y las diferentes
cuentas de banco que no dejan de aumentar diariamente sus activos (?);
tengo que decirles algo:

  Soy un fracasado

Estuve 4 días (de reloj -diría mi abuela) trabajando en configurar
correctamente PAC, WPAD, Polipo/Squid dentro de la Red Libre y Portal
Cautivo de `PyFi Spot <posts/nikola/lo-que-nos-deja-el-fracaso.rst>`_
y, no lo logré.

Probé varias configuraciones diferentes y aquí dejo algunos
comentarios para en un futuro no caer de nuevo en las mismas ideas:

#. Polipo `no soporta
   <http://www.pps.univ-paris-diderot.fr/~jch/software/polipo/faq.html#interception>`_
   funcionar como proxy transparente

#. Las **únicas** funciones soportadas dentro del archivo `wpad.dat`
   son las que figuran en su `documentación
   <http://findproxyforurl.com/pac-functions/>`_. No se puede utilizar
   otras funciones que sí están implementadas en los Browsers cuando
   uno abre la consola de desarrollo. Por ejemplo, yo traté de
   utilizar `XMLHttpRequest` y no está disponible.

#. Una buena forma de debuggear nuestro archivo PAC es utilizar estas
   herramientas:

   * `pacparser <https://github.com/pacparser/pacparser>`_

   * En Google Chrome, ingresando a `chrome://net-internals/` y luego
     a la sección de Proxy y Events. Dentro de Events uno puede ver
     qué archivo `wpad.dat` está bajando y si da algún error al
     ejecutarlo.

#. Para que WPAD funcione a la perfección por DNS debemos configurar
   las siguientes cosas; teniendo en cuenta que nuestro dominio es
   "redlibre":

   * Nuestro DNS debe resolver `wpad.redlibre` a la PC que tiene ese
     archivo.

   * Nuestro Web Server debe entregar ese archivo.

   * Mediante http://wpad.redlibre/wpad.dat debo poder descargar el
     archivo `wpad.dat`. Esto es lo que busca Firefox (lo dice la práctica).

   * Mediante http://wpad/wpad.dat también debo poder descargar el
     archivo. Esto es lo que hace Google Chrome (lo dice la práctica)

#. Tinyproxy no tiene función de caché.

#. La única forma que encontré de hacer un proxy transparente es con
   Squid y esta regla de iptables. Además, me sigue redirigiendo al
   Portal para loguearme::

     $IPTABLES -i $IFACE_HOSTAPD -t nat -A PREROUTING -m mark ! \
         --mark 99 -p tcp --dport 3128 -j REDIRECT --to-ports 80 

   Esto quiere decir, básicamente, que todo lo que entra por
   `$IFACE_HOSTAPD` y *no* está marcado como 99 y *es* TCP y *va* al
   puerto 3128 -> lo redirigimos al puerto 80 de la misma máquina.

#. **Nadie** sabe en qué momento los navegadores hacen un GET del
   archivo `wpad.dat`. Sin embargo, *por lo general* lo hacen al
   abrirse o al forzar su recarga desde algún lugar oscuro de la
   interfaz. Aunque, por otro lado, Google Chrome lo pide
   periódicamente cada un cierto tiempo desconocido.

#. Cualquier cabecera HTTP que tenga que ver con Caché no es respetada
   por Firefox ni Chrome. Implementé una versión de `wpad.dat` que era
   generada con Flask + Jinja2 dependiendo del IP que la solicitaba y
   no logré hacer que no cachee su contenido utilizando *Pragma* y
   *Cache-Control* de varias formas y combinaciones.

#. Google Chrome en Linux no "auto descubre" el proxy. Viene con esa
   configuración deshabilitada (al menos en Xubuntu 14.04). Entonces, para
   que auto descubra el proxy hay que llamarlo así::

     google-chrome --proxy-auto-detect

   Por lo que, tener una "auto configuración" de proxy en una red que
   muchos van a tener Linux y usar Google Chrome, es una
   estupidez. Firefox, por default, viene **bien configurado**.

#. La función `myIpAddress()` dentro del archivo PAC devuelve algo muy
   diferente en Firefox (mi verdadero IP dentro de la red en la que
   estoy) y Google Chrome (127.0.1.1). Por lo tanto, no es confiable y
   *no debería* usarse.

#. *Parece* que si instalás un paquete en Linux, Google Chrome
   comienza a obtener correctamente el IP utilizando la función
   anterior::

     sudo apt-get install libnss-myhostname

#. Hay una función `myIpAddressEx()` (notar el *Ex* en el nombre) que
   no alcancé a probar porque ya estaba muy hinchado los huevos; pero
   que `supuestamente funciona
   <https://code.google.com/p/chromium/issues/detail?id=386221>`_.

#. .. epigraph::

     Ah! agregale otro tema al myIPAddress(): los MS Windows 8 te
     devuelve la dirección de IPV6!!!

     -- César Ballardini

#. El `Content-Type` del archivo PAC debe ser
   `application/x-ns-proxy-autoconfig` porque sino puede ser que
   *algunos* browsers no lo utilicen.

#. `alert()` y `console.log()` dentro del archivo PAC no tienen ningún
   efecto. "No insista".


César me estuvo ayudando muchísimo, sobre todo con las ideas de cómo
implementarlo y qué probar para poder llegar a buen puerto. Sin
embargo, creo que ambos nos cansamos de dedicarle tiempo y esfuerzo a
algo que está demasiado mal implementado y se rompe por todos
lados. Sinceramente, creo que *no hay un standard* bien creado.

.. epigraph::

   PAC y WPAD anda si lo ponés en una maceta y no dejás más que una
   plantita a la cual cuidas con mucho esmero, y cuando crece la
   arrancás para que no sea diferente.

   -- César Ballardini


Y yo me despedí de él así:

.. epigraph::

   Te lo digo así: PAC, WPAD, Google Chrome, Firefox e Internet
   Explorer se pueden ir bien a la mierda. No puedo creer que esta
   gente haya inventado una tecnología tan pero tan mala para
   auto-configurar un proxy de mierda. Que no respete estándares y que
   sea tan difícil de debuggear.

   Acordate bien de esto: ¡estos tipos son unos hijos de puta!

   -- Manuel Kaufmann

Entonces, borré todo lo que hice, desinstalé Polipo, Tinyproxy y
Squid. Además, borré el archivo wpad.dat y mandé todo al carajo. No
tiene sentido implementar algo que es tan inestable. Para lo único que
simple todo esto es para tener algo demasiado-muy sencillo, esa
plantita a la que hace referencia César.

Espero que la siguiente persona que quiera configurar PAC y WPAD
llegue a este artículo *antes* de aventurarse en esto y terminar
siendo un fracasado más.
