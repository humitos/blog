.. link:
.. description:
.. tags: internet, software libre
.. date: 2009/02/16 23:01:54
.. title: ¡Mirá mamá, sin manos!
.. slug: mira-mama-sin-manos

Frase que escucho al menos una vez a la semana de la boca del *Flamante
Ingeniero* ( :) ) César, con quién tengo el gusto de trabajar todos los
días en la misma oficina cara a cara. Bueno, esta vez me tocó usarla a
mí, y ni más ni menos que para "no levantarme y usar las manos para
prender una computadora que se encuentra en la otra pieza"

Hoy nos juntamos con Nico, después de algunas discusiones, a "estudiar".
La discusión venía porque siempre que nos juntamos a *estudiar cosas
diferentes* ninguno de los dos termina estudiando **eso** y nos colgamos
hablando y debatiendo sobre distintos conceptos y softwares que andan
dando vueltas por ahí.

Como no podía ser de otra forma, ese *momento* existió, y nos pusimos a
ver como era el tema de ***WakeOnLan***: "Encender mediante la red" o me
perdí esa clase de inglés, pero la idea está. La posta es que querés
prender una computadora que no está al alcance de las manos, ni del pié
ni tampoco llegás con el escobillón; lo cual resulta ser un garrón si
estás acostado en la cama un día de invierno tapado hasta la nariz
dejando un espacio para que salgan los ojos y poder ver la pantalla del
monitor (sí, sí... **bien nerd**)

Esta es una propiedad de la BIOS y de la placa de red, por ende hay que
habilitarla en... y si, la BIOS :) . El lugar dónde se encuentra esto
depende de la placa madre, por lo que no voy a indicar en qué menú se
encuentra, pero sí dónde está la respuesta: **RTFM** o más conocido como
*Read The Fucking Manual*.

Una vez que tenemos esto habilitado, resta instalar un programa que
genera un paquete *mágico* para que la máquina que queremos encender se
prenda como por arte de mágia. El paquete en cuestión es **ethwake** y
está en los repositorios de Debian, por lo que se instala mediante
apt-get.

Echo este, habilitada la opción WakeOnLan en la pc que queremos
encender, resta ejecutar este programa indicando cuál es la interfaz por
la que llegamos a esa pc y cuál es la MAC de la misma. Vamos a un
ejemplo:

    # etherwake -i wlan0 00:61:13:dd:ff:c2

Le estoy indicando que vaya por la interfaz **wifi** y que la mac de la
pc que quiero prender es **00:61:13:dd:ff:c2** (esta es una MAC
inventada por mí). Si estamos dentro de una LAN esto funciona
perfectirijillo, pero... ¿Qué pasa si lo queremos hacer **OnWan**?

Existe otro paquete llamado **wakeonlan** que permite indicarle el IP de
la máquina de destino además de la MAC, entonces, si estoy conectado a
internet, me conozco la MAC de mi pc y además sé cuál es el ip que tengo
le puedo mandar un SMS :P diciendo que quiero que se prenda:

    # wakeonlan -i humitos.homelinux.net 00:61:13:dd:ff:c2

Y... tarán... puedo ver por el espejo de mi casa como se está prendiendo
la pc y entrar a mis datos compartidos que tengo con Apache, usar ssh y
hacer lo que se me canta ahora que la pc está prendida. El único
problema que tengo es que con Arnet tengo IP dinámica, osea, si se me
corta la luz, la máquina queda apagada y el router se reinicia, pierdo
el *humitos.homelinux.net* para acceder con un nombre, ya que el router
no soporta dyndns ni nungún otro, esto lo hago mediante **ddclient**\ y
para que esto funcione la pc tiene que estar prendida, pero ¡Oh
casualidad! es justo lo que quiero hacer :P

Como nota, puedo decir que tuve que habilitar una cosa más. No sé
porqué, si es mi máquina o en todas pasa lo mismo, pero como que al
habilitar esta opción de la BIOS se habilita "por la mitad", si algo que
suena raro para quien ignora totalmente como funciona esto, osea: yo. El
punto es que tuve que instalar otro paquete para hacerlo funcionar, este
es: **ethtool**. El cual entre otras cosas sirve para *terminar*\ de
habilitar esta opción.

    # ethtool eth0 Settings for eth0: [...] Transceiver: external
    Auto-negotiation: on **Supports Wake-on: g Wake-on: d** Link
    detected: yes [...]

Las líneas que están en negrita son las más importantes. La primera
indica que la placa que tengo lo soporta y la segunda, que está
desactivado. Entonces lo que tuve que hacer fue ejecutar:

    # ethtool -s eth0 wol g

De esta forma activo esta opción. Luego cuando apague la máquina la voy
a poder prender desde la red, pero por esas casualidades de la vida,
esta configuración se pierde: ni idea porqué... Ignorancia pura! Pero la
solución chancha y que me caracteriza, fue poner una directiva "up" cada
vez que se levanta la eth0... ¡Chupate esa mandarina! :P
