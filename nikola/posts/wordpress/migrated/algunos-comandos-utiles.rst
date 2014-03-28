.. link:
.. description:
.. tags: debian, software libre
.. date: 2010/08/28 14:17:57
.. title: Algunos comandos útiles
.. slug: algunos-comandos-utiles


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2010/08/28/algunos-comandos-utiles/


Hace un tiempo, por lo menos 2 años, que tengo un Trac instalado en casa
para uso personal. La idea surgió para organizar mis cosas personales,
como repositorio de código para los scripts que vaya haciendo y además
para anotar documentación sobre las cosas que voy investigando: links,
paquetes, configuraciones, instalaciones de programas, comandos y demás.

En este post voy a poner algunos comandos (surtidos) que no tienen nada
que ver uno con el otro, pero que son realmente útiles y que normalmente
los busco en internet cada vez que necesito hacer algo similiar, a
partir de que los anoté en el wiki del trac que uso me pasa que
probablemente me lo acuerdo o sinó, al menos, ya sé dónde buscar.

**Seleccionar el programa a usar por defecto**

En Linux podemos tener instalados varios programas para hacer lo mismo
en pocas palabras, como ser el Java o bien el Navegador Web. Existen
otros programas que en algún momento por ejemplo quieren abrir una
página web y se fijan cual es el navegador que tenemos configurado por
defecto, y lo lanzan con el link en cuestión. Puede ser que el navegador
configurado en nuestro Linux por defecto no sea el que realmente usamos
comunmente. Para cambiar esto existe el comando **update-alternatives**

::

    humitos@teresa: ~$ update-alternatives --config x-www-browser There
    are 5 choices for the alternative x-www-browser (providing
    /usr/bin/x-www-browser).

    Selection    Path                    Priority   Status
    ------------------------------------------------------------
    0            /usr/bin/google-chrome   120       auto mode
    1            /usr/bin/google-chrome   120       manual mode \*
    2            /usr/bin/iceweasel       70        manual mode
    3            /usr/bin/konqueror       100       manual mode
    4            /usr/bin/opera           90        manual mode
    5            /usr/bin/xlinks2         69        manual mode

    Press enter to keep the current choice[\*], or type selection
    number: 2 humitos@teresa: ~$

Como cualquier comando de Linux, hay un montón de opciones y de
variables para configurar, recomiendo mirar el **man
update-alternatives**

**Sincronizar directorios**

Una cosa que hago mucho es copiar información de una máquina a otra por
la red en mi casa, o cuando voy a la casa de un amigo y me quiero llevar
varias cosas de las que tiene en su máquina. Entonces, ¿seguimos
utilizando el método antiguo de Windows que cuando se corta la
transferencia por algo tenemos que hacer todo de nuevo o empezar a ver
qué era lo que ya pasó y qué lo que no? Al menos yo, nunca supe qué
hacer en esos casos y copiaba todo de nuevo: ¿se me había pasado algo?

Bueno, en Linux estoy usando **rsync**\ para esto y para algunas cosas
más (por ejemplo para hacer backups). Lo bueno de **rsync** es que
compara los dos directorios y copia sólo lo que falta, digamos, continúa
con la copia anterior. Además se puede hacer que sincronice los
directorios, borrando lo que corresponda de cada lado luego de hacer la
transferencia. En pocas palabras: se puede hacer *mucho* con **rsync** y
no lo sé usar para todo lo que se puede.

    rsync --recursive --human-readable --verbose --checksum
    --delete-after \\ --exclude winxp.img /media/sdb1/trabajo trabajo

El comando anterior es el que usaba cuando no tenía notebook y trabajaba
en mi casa y además en la oficina, entonces lo que hacía era sincronizar
todo lo que tenía en el *pen drive* con la carpeta local borrando las
cosas que estaban de más en la carpeta de destino (en este caso la de la
máquina, no la del pen drive). Las otras opciones más o menos se caen de
maduras :)

**Levantar un trac de forma simple**

Durante mucho tiempo (antes de tener el trac que tengo ahora en casa) lo
tenía en el *pen drive* y me resultaba extremadamente útil, porque iba a
dónde iba podía levantarlo con toda la documentación que hacía un tiempo
venía escribiendo, buscar cualquier cosa y actualizarlo. De hecho, lo
podía levantar en Windows también si hiciera falta, aunque era un
poquito más complicado.

    tracd -p 8080 --basic-auth=trac,/media/humitos/trac/htpasswd,trac
    /media/humitos/trac

De esta forma estoy levantando el trac en el puerto 8000 y diciéndole
que utilice el archivo **htpasswd** para obtener los usuarios y las
claves desde ahí. El último argumento es la ruta a dónde se encuentra el
trac.

*Nota: la idea de meter un trac en el pen drive fue de un compañero de
trabajo en el Ministerio de Innovación y Cultura: Cristian, se merece
sus créditos :)*

**Ordenar los mp3 en el reproductor de mp3**

Muchas veces me ha pasado con algunos reproductores de mp3 que no
reproducen los archivos siguiendo el orden alfabético de los mismos sino
que siguen el orden que tienen en la tabla FAT. No estoy seguro si esto
pasa únicamente cuando copiamos los archivos con Linux o también pasa
con Windows. Nunca escuché a un usuario de Windows que tenga este
problema, pero sí lo he escuchado de algunos usuarios de Linux.

El programa que utilizo para ordenar los mp3 de la forma que quiero que
se reproduzcan se llama **fatsort** y se usa así:

    fatsort /dev/sdc

*Nota: esta forma de ordenar los mp3's se la debo a Nicolás, un groso*

**Utilizar ssh en el puerto 443 y mediante https**

Existen muchos lugares en los que limitan el acceso a internet a sólo
conexión *https*\ y *http* entonces no podemos acceder a nuestra máquina
linux en la que tenemos corriendo un *ssh* en el puerto 22 (que es el
puerto por default). Para estos casos, yo tengo configurado el *ssh*
corriendo en el puerto 443 y utilizo un programa llamado **corkscrew**
para que meta el ssh dentro de una conexión https :)

Los único que hay que hacer es editar el archivo de configuración de ssh
en la máquina desde la cuál nos vamos a conectar a la que tiene el *ssh*
corriendo en el puerto 443. El archivo es este ``~/.ssh/config``

    Host=humitos.homelinux.net ProxyCommand /usr/bin/corkscrew
    10.2.6.219 3128 %h %p Port 443

En el ejemplo anterior el ip 10.2.6.219 es el ip del proxy al cuál nos
vamos a conectar para salir a internet y el 3128 es el puerto de este.
