.. link:
.. description:
.. tags: software libre, ubuntu
.. date: 2008/09/21 14:46:39
.. title: Encore ENUWI-G2 (RTL8187b) en Debian
.. slug: encore-enuwi-g2-rtl8187b-en-debian

/me pone música porque se viene para largo...

En el transcurso del fin de semana estuve **peleando** con la placa de
red USB Encore ENUWI-G2, pero al final conseguí hacerla funcionar y de
la forma que pretendía hacerlo.

Hace algunos meses que tenía ganas de comprarme una placa de red wifi
para estudiar algunos conceptos y ver la forma de analizar paquetes con
encriptación. Algunas de estas cosas las vimos muy por arriba en la facu
y me quedó picando el bichito de ver como es esto de las redes wifi.

En aquél momento averigué por todos lados sobre placas PCI, que suponía
que eran más barata y que además me daba la impresión de que tenían más
alcance al tener una antenita por afuera. Después de esta recorrida no
decidí comprarme nada porque estaban un poco caras, algo así como $100 o
más. No quería gastar esa plata para algo que **no necesitaba** ya que
era sólo por investigación.

Pasó cierto tiempo, empecé a trabajar, me pelié con muchas placas wifi
en el trabajo y mi ignorancia me mataba frente a este tipo de redes. Me
dí muchas veces la cabeza contra la pared cuando quería conectarme a un
AccessPoint: me mataba depender de un entorno gráfico para poder
conectarme (estaba usando el KWifiManager), asique me decidí a aprender
todo este tipo de cosas.

El viernes por la tarde, me fui a *promocionar* la **3ra Jornada de
Python en Santa Fe** con un amigo al centro en busca de sponsors y de
paso aprovechaba para preguntar sobre una placa wifi en algunos lugares
que quedaban por el centro. Me fui de casa con la idea de comprar una
TP-Link que estoy seguro que funciona ya que es la que pudimos
configurar en el trabajo: mediante **ndiswrapper**.

Los precios que manejaban las casa de computación eran al rededor de los
$80 para arriba y todas eran placas que no conocía, asique no me gustaba
para nada. Igualmente le preguntaba si sabían que estas funcionen en
linux para luego ir a averiguar si en alguna me decían que si. La
mayoría no tenía ni idea, asique seguía mi camino.

Por último fui a un lugar que venden DVD's, CD's y un montón de
accesorios pero... Por las dudas fui igual. Me encontré con la placa del
título de este post a un precio de $60, anoté el modelo porque era
interesante este precio y le dije que iba a averiguar si funcionaba en
Linux y que si era así volvía a comprarla. Antes de irme le pregunté si
sabía si funcionaba y me dijo: "Anda!", nada más.

|Encore ENUWI-G2|

Cuando me estoy yendo mi amigo me dice: "¿Y porqué no la llevás si sabés
que anda?", a lo cual le contesto delante de los vendedores: "Me quiero
asegurar". Salimos de ahí y nos estábamos volviendo para casa, para
supuestamente volver al día siguiente (Sábado) a comprarla luego de
buscar en internet. Se me ocurrió ir a un cyber para verificar esto y
comprarla ese mismo día.

Lo primero que encontré es que muchos la habían hecho funcionar con
**ndiswrapper**, tal y como yo sabía que funcionaba la TP-Link, asique
ya estaba dicho: "La tenía que comprar". Salí del cyber y la compré.

Cuando llegué a mi casa seguí buscando información sobre cómo instalarla
y por todos lados estaba la misma descripción del que `había encontrado
en el
cyber <http://delajusco.wordpress.com/2007/10/10/como-instalar-un-adaptador-wifi-encore-enuwi-g2-en-ubuntu-610-edgy-eft/>`__
asique me puse a hacerlo de esta forma. Esto era instalar ndiswrapper,
cargar el driver de Windows XP y levantar el módulo del kernel de
ndiswrapper, pero... Oh! sorpresa me encuentro que el módulo del kernel
no levanta. Buscando en Google encontré que tenía que compilar el módulo
para la versión específica de mi kernel (**2.6.24-amd64**) ya que no
venía precompilado.

Manos a la obra entonces. Instalé los paquetes necesarios y compilé el
paquete:

::

     apt-get install module-assistant ndiswrapper-source
     m-a a-i ndiswrapper

Una vez que tenía esto andando, pude hacer *modprobe ndiswrapper* y que
carge correctamente este módulo, aunque en los logs (*/var/log/message*)
me estaba indicando que tenía un driver para 32bit y que yo tenía un
kernel de 64bit. ¡Qué mala suerte!. Busqué por todo el CD los drivers
para XP64bit y no los encontré, asique los bajé la `página oficial de
encore <http://encore-usa.com>`__ y estos sí funcionaron.

Luego investigué como hacer para conectarme a mi AccessPoint, busqué por
internet e hice muchas pruebas antes de lograrlo. Lo primero que me fijé
en realidad era el comando **iwlist** (del paquete wireless-tools) que
entre otras cosas sirve para escanear las redes y ver los *essid's* que
exportan los AccessPoint. Por suerte veía el mío, y la calidad de la
señal era de 60 más o menos estando a 1,5 metros de distancia. Esto no
me sorprendío porque calidad de la señal que teníamos en el trabajo con
las otras placas era más o menos igual.

En poco tiempo logré configurar la conexión sin encriptación y funciona
sin problemas. Luego probé hacerlo con WEP y también funcionaba. Asique
quise pasar al siguiente paso: **sniffear** la red utilizando la placa
en el modo *Monitor*. Cuando intento cambiar el modo de la interfaz, el
mismísimo driver me dice que la placa esta no soporta este modo, nah!.
Me fui a la página oficial y efectivamente dice que sólo funciona en
*Ad-Hoc* (punto a punto) y en modo *Managed* (contra un AccessPoint).

Seguí buscando por todos lados, no me podía dar por vencido. Encontré
por todos lados un `proyecto de
drivers <http://linuxwireless.org/en/users/Drivers/rtl8187>`__ libres
para el modelo rtl8187, que aunque esa página no está muy completa,
tiene unos links que resultaron interantes. Y como siempre sucede, uno
nunca lee la página completa, lee un poquito y se va directamente a
ejecutar los comando :) , luego me encontré con que el **chipset
rtl8187b no estaba soportado** por ese driver :(

También encontré una modificación a este driver que *parece funcionar*
con este modelo de chipset. Mmm... vamos a probar. Me pelié mucho para
compilarlo, hice un poco de magia negra y salió andando. Me lo detectaba
y todo lindo, pero cada 2 o 3 minutos recibía un hermoso **Kernel
Panic**, lo cual me llevó a hacer algunas pruebas más y descartarlo por
completo si quería que mi sitema siga funcionando :) .

Ya eran las 2 de la mañana de anoche y yo seguía dando vueltas con mi
placa de red wifi, no encontraba la solución que buscaba. Sí tenía la
placa funcionando con ndiswrapper, pero no la podía sniffear ni tampoco
me gustaba que los drivers no sean libres (lo único que tengo no-libre
son los de NVIDIA porque no encontré solución aún :( ). Me fui directo
al `código fuente <http://www.kernel.org>`__ del kernel y me puse a leer
los ChangeLogs, `vi que se estaba
trabajando <http://git.kernel.org/?p=linux%2Fkernel%2Fgit%2Fstable%2Flinux-2.6.26.y.git&a=search&h=HEAD&st=commit&s=rtl8187>`__
para el chipset rtl8187 y me volvieron las esperanzas nuevamente.
También vi que Linus Torvalds hizo un commit el 23 de Diciembre de 2007:
¡Que capo!

A todo esto me dijo: "¿Y porqué no?, ya estoy en el baile. Me compilo el
kernel y lo saco andando". Me bajé el kernel
(`2.6.27-rc6 <http://www.kernel.org/pub/linux/kernel/v2.6/testing/linux-2.6.27-rc6.tar.gz>`__)
de la página oficial y `seguí una guía muy
buena <http://www.howtoforge.com/kernel_compilation_debian>`__ que
explica como hacerlo a la manera Debian, esto sería creando un paquete
**.deb** y luego instalándolo.

Por supuesto que lo primero que hice cuando hay que configurar las
opciones fue verificar que estaba tildada la opción de mi placa de red
wireless :) . Además tuve que cambiar unas cositas en esa guía, primero,
el comando **fakeroot** por **fakeroot-sysv** porque el primero comando
me decía que no lo tengo. Segundo, me saltié el paso de crear un ramdisk
(el paso 8) de la guía. Al terminar la instalación completa me daba este
error al intentar bootear con el nuevo kernel:

::

    Kernel panic - not syncing VFS: Unable to mount root fs on unknown - block (0,0)

Esto tengo entendido que es por ese paso que me saltié, pero no lo hice
porque no me gustaba nada tener que bajar un paquete que no conocía de
un lugar que no fueran los repositorios de debian, además era una
versión del kernel muy vieja y decía que era algo novedoso la forma en
que se trataba el RamFS. Quizás una maña mía nomás. Al final lo terminé
haciendo de otra forma:

::

    update-initramfs -c -v -k 2.6.27-rc6-rtl8187b-1

Esto me generó el archivo */boot/initrd.img-2.6.27-rc6-rtl8187b-1*\ el
cual tuve que agregar a la entrada del nuevo kernel el archivo
*/boot/grub/menu.lst* para que funcione correctamente.

Reinicié la máquina, bootié con este kernel y me fijé si se había
detectado la placa wifi: perfecto. Me conecté al router, hice algunas
pruebas, intenté switchear sobre los distintos modos (Managed, Monitor,
etc) y funcionaba. Wiiii!

Pero todo no se puede, no tenía **X** porque los drivers de NVIDIA no
estaban funcionando en este kernel :) . Igualmente lo que me importaba
era testear a full este nuevo driver y pude hacerlo. Cuando hice un
**iwlist scan** me detectó la red de mi casa con una señal de 100. Wow!!
Nada que ver a los drivers que estaba usando con ndiswrapper, y cada
tanto veo que oscila entre 90 y 100.

El próximo paso fue investigar como hacer para que funcionen
correctamente los drivers de NVIDIA en el kernel 2.6.27-rc6 que es en
dónde me está funcionando la placa wifi... Tema para otro post.

**Update:**\ Martes 23 de Septiembre

**NOTA:**\ la primer parte (instalación con ndiswrapper) fue probada en
un Live-CD (32bit y 64bit) de Ubuntu también. La compilación de los
kernel's no, pero debe ser exactamente lo mismo. Mejorando esto, lo que
conviene hacer es bajarse los `drivers *Beta* de
NVIDIA <http://www.nvidia.com/object/linux_display_ia32_177.67.html>`__
ya que no tienen ningún problema para instalarse.

.. |Encore ENUWI-G2| image:: http://www.wei.cl/images/products/TJETH00612.gif
