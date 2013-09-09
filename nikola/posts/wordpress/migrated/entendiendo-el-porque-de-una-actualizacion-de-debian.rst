.. link:
.. description:
.. tags: debian, software libre
.. date: 2011/06/22 09:20:18
.. title: Entendiendo el porqué de una actualización de Debian
.. slug: entendiendo-el-porque-de-una-actualizacion-de-debian

Me ha pasado muchas veces de querer hacer un **dist-upgrade** desde la
consola y que APT me diga que quiere desinstalar unos cuantos paquetes
porque entra en conflicto con "vaya uno a saber qué". Como muchas veces
esos paquetes que me quería desinstalar yo quería que sigan estando en
mi PC dejaba de hacer la actualización hasta que en algún momento del
futuro esto no vuelva a pasar.

Bueno, hoy hice una pequeña búsqueda en Google y encontré `un
artículo <http://www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html>`__
que habla exactamente de esto y dice que el "*vaya uno a saber qué*\ "
el mismísimo APT lo sabe y es más, le podemos decir si es tan amable y
nos puede explicar mediante una opción:

    apt-get -o Debug::pkgProblemResolver=yes dist-upgrade

Esto nos ayuda a saber porqué está intentando eliminar algunos paquetes
de nuestro sistema. Grosini!

La solución era mantener algunos paquetes que yo tenía en el sistema en
las versiones actuales, digamos, no actualizar a las nuevas versiones de
algunas librerías porque estas nuevas versiones entraban en conflicto
con las viejas del programa en sí. Entonces, lo que hice fue mantener
dichas versiones en mi PC tal cual las tenía. Acá, hubiese podido
**Pinnear**\ los paquetes buscando las versiones de los que tengo
instalado con *dpkg -l* o bien usar *dpkg --set-selections*\ que fue lo
que finalmente usé como encontré en `este
post <http://www.linux-archive.org/ubuntu-user/532882-hold-back-some-packages-apt-get-upgrade-how-gre.html>`__

    echo backuppc hold \| dpkg --set-selections

Después, para volver a decirle a APT que actualice ese paquete en el
próximo *upgrade* hay que hacer:

    echo backuppc install \| dpkg --set-selections
