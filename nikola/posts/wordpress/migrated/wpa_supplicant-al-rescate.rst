.. link:
.. description:
.. tags: internet, software libre
.. date: 2012/04/09 17:08:47
.. title: wpa_supplicant al rescate
.. slug: wpa_supplicant-al-rescate

¿Cuántas miles de veces puteaste porque no te levantaron las X por el
motivo que sea y tuviste que recurrir a conectarte a la red por la
consola? ¿Con cuánto tiempo contabas en ese momento para estudiarte los
manuales de *ifconfig, iwconfig, iwlist, wpa_supplicant* y demás?
Incluso, ¿sabías que ellos existían antes de haberte quedado sin X?

Si te preocupa llegar a ese momento y no saber qué hacer. Si estás
agradecido a que las X siempre levantaron en los momentos que más lo
necesitabas. Si no querés que esto te pase, ésta es la guía que te
aconsejo leer: *wpa_supplicant al rescate.*

Básicamente la idea es esa: conectarse a una red ABIERTA, WEP o con WPA2
como si lo hiciéramos desde la interfaz gráfica. Sólo basta con aprender
algunos comandos útiles, sin siquiera explorarlos a fondo (ya que hay
miles de variantes) para cubrir los casos más habituales.

Entonces, ¡vamos manos a la obra! Lo primero que hay que hacer es
fijarse si la interfaz que queremos utilizar para conectarnos a la red
está habilitada. Para eso ejecutamos:

    ::

        sudo ifconfig

Este comando nos lista las interfaces que actualmente tenemos
habilitadas. De no encontrar nuestra interfaz en esa lista, debemos
comprobar que ésta ha sido detectada por el kernel y que la podemos ver
como deshabilitada:

    ::

        sudo ifconfig -a

Si la interfaz aparece en esta lista y no en la anterior, eso es
justamente lo que ha pasado: el kernel la detectó pero aún no la ha
habilitado. Entonces, antes que nada debemos habilitarla para poder
empezar a usarla. Para eso:

    ::

        sudo ifconfig wlan2 up

En mi caso, la interfaz se llama **wlan2**, pero puede que tu kernel la
nombre distinto.

Ahora lo que resta es listar las redes disponibles (las que están a
nuestro alcance), asociarse a una de ellas y luego preguntar por una
dirección de IP. Entonces, primero listamos las redes disponibles:

    ::

        sudo iwlis wlan2 scan

Ahí vamos a ver una serie de datos, quizás irrelevantes para algunos,
quizás no. Pero lo que más nos interesa de ese listado son los campos
**Encryption key**\ y **ESSID**. Esos campos nos dicen qué tipo de
encriptación tiene (qué tipo de password debemos poner o ninguno) y el
siguiente nos dice el nombre de la red.

Si vemos que el valor del campo *Encryptation key* es **off** quiere
decir que la red está \ **ABIERTA** y debemos usar este comando para
asociarnos:

    ::

        sudo iwconfig wlan2 essid "humitos"

En cambio, si el valor de *Encryptation key* es **on** quiere decir que
la red está encriptada con **WEP**, para lo que el comando adecuado es:

    ::

        sudo iwconfig wlan2 essid "humitos" s:password

*Notar que la contraseña se escribe inmediatamente después de **s:***

Además, si encontramos que *Encryptation key* es **on**\ y vemos también
que hay un campo similar a **IEEE 802.11i/WPA2 Version 1**, nos está
indicando que la encriptación está hecha mediante WPA2 y para eso
debemos hacer algún truquito extra.

Primero debemos crear un archivo de configuración (que luego será pasado
como argumento a **wpa_supplicant**) con el nombre de la red, la
password y algunas cositas más:

    ::

        ctrl_interface=/var/run/wpa_supplicant

        ctrl_interface_group=20

        update_config=1

        network={
            ssid="humitos"
            psk="password"
            proto=WPA2
            key_mgmt=WPA-PSK
            pairwise=CCMP
        }

Una vez creado este archivo, yo comúnmente lo pongo en
*/etc/wpa_supplicant/<nombredelared>.conf*, tenemos que asociarnos a la
red como si estuviera abierta y luego llamar a **wpa_supplicant** para
que nos rescate:

    ::

        sudo iwconfig wlan2 essid "humitos"

        sudo wpa_supplicant -Dwext -iwlan2 -c/etc/wpa_supplicant/humitos.conf

Si llegamos a este punto, cualquiera sea el camino (abierta, wep o wpa)
quiere decir que estamos conectados con el Router, pero que estemos
conectados no quiere decir que podamos navegar por la red. Aún
necesitamos una dirección IP y para eso lo que debemos hacer es
preguntársela al router con **dhclient** (si el router usa servidor
DHCP) o sino ponerla manualmente.

Para usar DHCP, debemos utilizar este comando:

    ::

        sudo dhclient wlan2

Si en cambio, el router no nos entrega una dirección de IP por DHCP;
necesitamos poner la dirección manualmente. Además, si es un router que
nos permite tener acceso afuera de la red, también necesitamos asignar
un default gateway y un servidor de DNS:

    ::

        sudo ifconfig wlan2 192.168.1.105

        sudo route add default gw 192.168.1.1

        sudo echo "nameserver 192.168.1.1" > /etc/resolv.conf

Con estos comandos tenemos cubierto la mayor cantidad de casos de redes
wifi convencionales. Hay muchos casos más que quizás iré agregando con
el tiempo; pero no quería dejar de publicar esto ya que me ha resultado
bastante útil en muchas oportunidades.
