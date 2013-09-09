.. link:
.. description:
.. tags: general
.. date: 2011/07/14 20:29:59
.. title: Recuperar un disco rígido
.. slug: recuperar-un-disco-rigido

Se me murió el disco de la netbook hace un par de meses ya (sí, putié
bastante, de pedo que tiene un año la máquina y ya tubo problemas con el
flex del monitor y ahora esto), bue...

La cosa es que la formatié y le instalé Debian Wheezy desde un USB y le
dí formato con:

    mkfs.ext3 -c /dev/sdX

La cosa es que me encontró varios *bad blocks*, pero formatió y pude
instalar Debian sin problemas. Después de unos días empezó a fallar de
nuevo y ahora me encontré con que puedo marcar los *bad blocks* de un
file system "ya funcionando" digamos. (desmontándolo, ¿no?. Claro esta)

¿Qué opinan de este comando?

    e2fsck -c -c -k /dev/sdX

-  **-c:** lo que hace es buscar los *bad blocks*\ en ese dispositivo
-  **-c:** (de nuevo) hace que el test sea de lectura y escritura
   no-destructivo
-  **-k:** hace que mire la tabla de *bad blocks* que ya tiene y que
   conserve los que ya están marcados como defectuosos

¿Estas cosas funcionan o tengo que llevar a que me cambien el disco
rígido y entregar mi parte trasera?
