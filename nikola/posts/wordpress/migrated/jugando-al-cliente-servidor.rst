.. link:
.. description:
.. tags: hosting, internet, software libre, ubuntu
.. date: 2008/03/12 21:43:56
.. title: Jugando al Cliente-Servidor
.. slug: jugando-al-cliente-servidor


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2008/03/12/jugando-al-cliente-servidor/


Esta semana se me terminó la joda. El lunes empezaron las clases en la
facultad y yo de colgado no fui porque no sabía cuando empezaban, asique
fui el martes (ayer) por primera vez. Hoy teníamos una clase de práctica
de una materia que todavía no dimos la teoría asique no tuvimos clases.

Pensando en esto, que ya no iba a tener más vacaciones, me puse las
pilas con la otra máquina que tenía en casa para dejarla funcionando
como un servidor. **¿Servidor de qué?** De cualquier cosa, lo que
necesite en el momento, algo. Ésta ya tiene historia, porque es la que
tiene la instalación de Ubuntu hecha por red.

Lo primero que se me ocurrió, fue pasar toda la música al servidor y que
todas las pc de la casa la utilicen de ahí, así no hay temas repetidos,
lo que implica el doble de espacio de almacenamiento. Pero antes que
nada configuré el servidor ssh para poder realizar todo esto.

**SERVIDOR NFS**

Para compartir la música, tenía dos posibilidades, o al menos son las
que conozco yo: NFS o Samba. Opte por NFS porque con Samba ya había
tenido varios problemas. Ahora sí, los usuario de Windows no sé como van
a hacer para sacar archivos de acá por el momento.

NFS es tan simple configurarlo que me llevó 2 o 3 minutos. Primero
instalé el paquete **nfs-kernel-server,**\ y agregué la carpeta que
quería compartir a */etc/exports* con una sóla línea:

::

    /home/humitos/Música    10.0.0.5(rw,sync)

Moví toda mi música ahí, y luego le dije a la máquina cliente (la que
utilizo habitualmente) que me monte, en mi carpeta donde toda la vida
tuve la música, esa carpeta que se encuentra en la red. En el archivo
*/etc/fstab* agregué una línea:

::

    silvita:/home/humitos/Música /home/manuel/musica nfs rsize=8192,wsize=8192,timeo=14,intr

No tuve que cambiar ninguna configuración en Amarok ni nada por el
estilo, es como si esa carpeta estaría en mi máquina y nunca hubiese
pasado nada. Eso es lo bueno de poder montar lo que se te raje en dónde
se te raje, y no andar creando unidades de disco remotas en **X:\\** por
ejemplo.

**Nota:** la máquina servidor se llama *silvita* y el cliente
*michifus*. Sí **¿Y qué?**

**AMULE-WEB**

Lo segundo fue poner amule-web. Esto sirve para poder gestionar el aMule
desde cualquier lado mediante un explorador web. Buscar, pausar,
conectar, desconectar, cambiar configuraciones, etc.

Primero instalé el paquete **amuled** que me instaló algunas cosas más,
no recuerdo bien, pero eran dependencias extricta, no sugerencias ni
recomendaciones. Que en fin *son lo mismo*, pero Ubuntu hace la
diferencia.

Ejecuté *amuled*, me creó los archivos de configuraciones y demas. Cerré
el demonio con CTRL+C ejecuté este comando:

::

    $ echo -n CONTRASEÑA | md5sum | cut -d ' ' -f 1

    d287200e83ee04f67294de90dd72f9c6

    $

y edité el archivo *~/.aMule/amuled.conf*:

::

    AcceptExternalConnections=1

    ECPassword=CONTRASEÑA

En la sección [WebServer]:

::

    Enabled=1

    Password=CONTRASEÑA

Abrí los puertos 4662 TCP, 4665 UPD, 4672 UPD y 46711 TCP, corrí el
demonio nuevamente y ¡listo! ahora se puede acceder desde cualquier lado
ingresando **http:/host.ejemplo:4711**

**Fuente:**
`usrweblog <http://usrweblog.wordpress.com/2007/03/05/usando-amuleweb-con-amule-daemon/>`__

**APACHE**

Lo que sigue (configuración de torrentflux) necesita tener configurado
Apache, aunque yo no lo hice en este orden, me parece que es mejor
primero instalar Apache y luego TorrentFlux o por menos al mismo tiempo.

Lo que cambié en la configuración que trae por defecto apache, fue
agregar dos líneas al archivo */etc/apache2/apache2.conf* para poder
compartir al mundo (internet) las carpetas public_html de los home de
cada uno de los usuarios. Al final de todo el archivo puse esto:

::

    UserDir public_html

    UserDir enabled all

Lo que hace es habilitar el módulo UserDir para que se puedan compartir
estas carpetas. Aunque todavía no le indiqué que tiene que cargar el
módulo (para que esto funcione). Esto se hace creando un link simbólico,
yo lo hice así:

::

    $ cd /etc/apache2/mods-enabled

    $ sudo ln -s /etc/apache2/mods-available/userdir* .

    $ sudo /etc/init.d/apache2 restart

**Fuente:**
`huevas <http://huevas.wordpress.com/2007/07/03/habilitar-directorios-de-usuario-en-apache2-userdir/>`__,
`apache <http://httpd.apache.org/docs/1.3/mod/mod_userdir.html>`__

**TORRENTFLUX**

`TorrentFlux <http://www.torrentflux.com/>`__ es un cliente bittorrent
desarrollado en PHP al cual le doy la misma utilidad que al amule-web.
Poder gestionar las descargas desde cualquier lado. La verdad que está
buenísimo, es multi-usuario, se puede hacer lo mismo que en cualquier
cliente bittorrent o más...

Para instalarlo seguí `esta
guía <http://www.beernut.ca/roy/archives/004370.html>`__, que no voy a
reproducir porque está demasiado bien explicado aunque esté en inglés,
es ir tipeando comandos en la consola, casi como un click en
**Siguiente-Siguiente**.

**XDMCP**

¿Qué es esto? No tengo la más mínima idea, pero está buenísimo. Es como
un **ssh -X** pero en vez de redireccionar sólamente una ventana tenés
todo el escritorio de forma remota. Estuve leyendo algo en wikipedia, y
demás webs. Siempre me había preguntado porqué el Kubuntu traía algo que
decía al inicio de la sesión "Remote Login", que de hecho no tiene
porqué estar en inglés.

Pero bueno, busqué y encontré al toque, en menos de 15 minutos lo tenía
funcionando. ¿Qué hice? busqué este archivito en la máquina servidor
(silvita) */etc/gdm/gdm.conf*\ y cambié un parámetro:

::

    [xdmcp]

    Enable=true

Reinicié el servidor porque no sabía como reiniciar sólo esto de gdm
(supongo que con un CTRL+ALT+BACKSPACE se solucionaba) volví al cliente,
michifús, puse en kde que quería iniciar una sesión nueva y que sea de
remota. Al toque me apareció un item en la lista, doble click y voilá,
estaba en el login de la otra pc. Asique ahora tengo en CTRL+ALT+F7 mi
sesión de KDE en mi máquina y en CTRL+ALT+F9 tengo una sesión de GNOME
en el servidor. Lero lero!
