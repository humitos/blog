.. title: USB Hub y energía
.. slug: usb-hub-y-energia
.. date: 2015-06-04 13:58:08 UTC-03:00
.. tags: linux, kernel
.. category: 
.. link: 
.. description: 
.. type: text

Como mi máquina tiene solo 2 puertos USB 3.0, me compré un hub USB
marca Noganet (esos que de un puerto te sacan 4). Hasta ahí todo
bien. Sin embargo, luego ese hub como era muy trucho, ser rompió y me
compré otro: Belkin. Compré esa marca por ya había trabajado con
algunos routers wifi y me pareció que eran piola. Así que, aposté
también al hub USB.

Lamentablemente, nunca me funcionó bien. *Algunas* cosas que enchufaba
ahí no funcionaban correctamente y otras sí. Por ejemplo, el receptor
del mouse wireless anda sin problemas, pero un pendrive o un lector de
tarjetas SD no.

Investigué un poco y me encontré con que "no le alcanza la
energía". ¿Pero cómo? Si con el otro hub USB sí le alcanzaba si
enchufaba exactamente las mismas cosas.

.. code::

   usb 3-1.2: new high-speed USB device number 33 using xhci_hcd
   usb 3-1.2: New USB device found, idVendor=14cd, idProduct=125c
   usb 3-1.2: New USB device strings: Mfr=1, Product=3, SerialNumber=2
   usb 3-1.2: Product: Mass Storage Device
   usb 3-1.2: Manufacturer: Generic
   usb 3-1.2: SerialNumber: 125C20100726
   usb 3-1.2: rejected 1 configuration due to insufficient available bus power
   usb 3-1.2: no configuration chosen from 1 choice
   checking bus 3, device 33: "/sys/devices/pci0000:00/0000:00:14.0/usb3/3-1/3-1.2"
   mtp-probe: bus: 3, device: 33 was not an MTP device

Ahí dice claramente que no le alcanza la energía disponible en ese
bus. Esto aparece cuando enchufo un pendrive al hub.

Busqué un poco en internet y la solución que planteaban era aumentar
la cantidad de energía entregada en ese puerto y listo. La forma de
hacerlo es:

.. code::

   echo -n 1 >/sys/bus/usb/devices/3-1.2/bConfigurationValue

(el *1* ese `quiere decir
<https://ekuric.wordpress.com/2012/06/12/playing-with-usb-devicesremove-them-without-physical-access/>`_
que "conectado")

.. TEASER_END

Esto me sonaba raro, porque si hay un problema de energía y yo le
estoy diciendo: "No me importa nada. Dale toda la energía que esto
requiera y ya" puede ser que algo salga mal, que se **queme el
puerto** o salga *humito*. No sé. Mejor sigo investigando, me dije...

Hoy encontré `una respuesta
<http://www.mail-archive.com/linux-usb-devel@lists.sourceforge.net/msg43480.html>`_
un poco más interesante:

.. code::

   The idea is that the kernel now keeps track of USB power budgets.
   When a bus-powered device requires more current than its upstream
   hub is capable of providing, the kernel will not configure it.

   Computers' USB ports are capable of providing a full 500 mA, so
   devices plugged directly into the computer will work okay.  However
   unpowered hubs can provide only 100 mA to each port.  Some devices
   require (or claim they require) more current than that.  As a
   result, they don't get configured when plugged into an unpowered
   hub.

Entonces, esto quiere decir que *como máximo* el puerto de la pc
entrega 500mA y cada uno de los puertos del hub USB entrega
100mA. Entonces, por ahí venía el problema. Pareciera que los
pendrives y los lectores de tarjetas SD necesitan más que 100mA y por
eso el hub no lo está manejando correctamente.

En ese mismo email dice que podés consultar cuántos mA requiere un
dispositivo USB que tengas conectado con `lsusb -v`:

.. code::

   $ lsusb -v
   [...]
   MaxPower              248mA
   [...]

Así encontré que mi lector de tarjetas necesita 248mA y si le estoy
entregando solo 100mA es obvio que no va a funcionar. Esta entrega de
amperaje es manejada por el kernel, por eso poniendo ese "1" mágico en
ese archivo la puedo controlar manualmente.

Sin embargo, esto es peligroso porque: ¿qué pasa si pongo 2 pendrives
y 2 lectores de tarjetas en el hub USB? ¿se me quema el puerto?

Entonces, me gustaría ver si hay una forma de "medir cuántos mA
necesito para las cosas que tengo conectadas en el hub USB y si es
menor a 500mA (lo máximo que soporta el puerto) activarla, sino solo
informar por pantalla como hace ahora en /var/log/syslog"

La otra pregunta es: ¿qué pasaba con el Noganet? ¿porqué ese no tenía
esta limitación de energía? ¿era peligroso utilizarlo así?

¿Me das una mano?
