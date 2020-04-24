.. title: Navegar en internet en aeropuertos
.. slug: navegar-en-internet-en-aeropuertos
.. date: 2017-10-04 15:57:22 UTC-03:00
.. tags: linux, mac, network, aeropuerto, viaje
.. category: 
.. link: 
.. description: 
.. type: text

Una de las mejores cosas de saber cómo funcionan las cosas es que "a
veces" podés utilizar ese conocimiento para tomar atajos.

Hoy tengo un ejemplo concreto de esto. En mi viaje por sudamérica creé
un proyecto llamado `PyFi Spot`_ que básicamente es un portal cautivo
escrito en Python que ejecuta comandos de iptables para permitir o
denegar el acceso a internet de las personas que se conecta a una red
abierta.

¿No les suena familiar? Esos bares, restaurantes o aeropuertos que te
dicen que tenés 30 minutos gratis para navergar y luego se
termina. OK, algunos aeropuertos te permiten pagar (nunca entedí dónde
se compra ese usuario/contraseña que te pide al web) y podés seguir
navegando durante el tiempo que has pagado. Pero hay otros, que ni
siquiera tienen esa opción y entonces en una espera de 5 horas (como
la mia de hoy) solo tenés 30 minutos y te querés matar.

Acá entran en juego `macchanger`_ y `NetworkManager`_.

"Mmm... macchanger, eso me suena a algo", estarás pensando. Sí, la
posta de este tipo de servicios es que bloquean a los dispositivos
(teléfonos, laptops, etc) por el número de MAC de la placa de red de
ese dispositivo que es único en el mundo. Entonces, esta es la forma
que los portales tienen de saber quiénes están accediendo a su red y
filtran el acceso a internet por ese número (que va incrustado en los
paquetes de red).

Claro, ¿porqué sé esto? Porque me hice un programa que hace
exactamente eso y le dediqué un par de semanas a estudiar como
funcionaban estos bichos.

¿Entonces? ¿Cuál es la solución? Y claro, cada 29 minutos cambiar la
MAC de tu placa de red y volverte a conectar utilizando la nueva
MAC. El portal cautivo cree que sos una persona totalmente nueva
y... ¡ADELANTE!

¿Cómo hago para cambiar la MAC? Utilicé Network Manager que hace todo
esto sea muy fácil:

* Click derecho en el ícono del systray
* "Editar las conexiones..."
* Elegís la conexión que tiene el nombre de la red del aeropuerto
* Vas a la pestaña "Inalámbrica"
* Y donde dice "Dirección MAC clonada", le ponés "Aleatorio"
* Guardás todo, cerrás, volvés a conectar y listo!

.. admonition:: Cookies en juego

   Te recomiendo iniciar la sesión en el portal cautivo utilizando una
   pestaña privada, para así evitar que se guarden las cookies en tu
   máquina y que luego el sistema nos reconozca como que hemos vencido
   nuestro tiempo.

   Si ya "la has cagao", borrando las cookies del navegador solucionás
   este problema.
   
.. note::

   A "macchanger" no lo usé al final, ya que si bien funcionó, al
   volverme a conectar a la red mediante "network manager" este me volvía
   a poner la MAC de mi placa de red original.

.. _NetworkManager: https://wiki.archlinux.org/index.php/NetworkManager#Configuring_MAC_Address_Randomization
.. _macchanger: https://wiki.archlinux.org/index.php/MAC_address_spoofing#Method_2:_macchanger
.. _PyFi Spot: https://github.com/humitos/pyfispot
