.. link:
.. description:
.. tags: software libre, ssh, ubuntu
.. date: 2007/10/01 15:53:52
.. title: Conexión remota por SSH
.. slug: conexion-remota-por-ssh


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/10/01/conexion-remota-por-ssh/


`SSH <http://es.wikipedia.org/wiki/Secure_Shell>`__ es un protocolo que
nos permite conectarnos a un equipo de forma remota mediante una red
`LAN <http://es.wikipedia.org/wiki/Lan>`__ /
`WAN <http://es.wikipedia.org/wiki/Wan>`__. Permite manejar por completo
la computadora, de manera que todo lo que ejecutemos se hará sobre ésta
computadora (a la que estamos accediendo de forma remota) y se
visualizará en la que estamos localmente. Por ejemplo si ejecuto el
comando:

    *$ ogg123 "The Crazy - This is a breakfast.ogg"*

El sonido de la reproducción de este archivo de audio saldrá por los
parlantes que posea la máquina remota, quizás nosotros ni escuchemos
este sonido debido a la distancia en la que nos encontramos.

Mediante este protocolo se pueden copiar archivos, visualizar contenido
de éstos, actualizar el sistema, reiniciar el pc, y muchas cosas más.
Para la conexión mediante SSH se necesita tener la máquina encendida :P
y además que se encuentre *corriendo* el demonio servidor de SSH.

Necesitamos instalar el paquete *ssh* en Ubuntu, el cuál nos instala el
cliente de ssh y el servidor ssh. Una vez instalado esto podemos
verificar que se esté ejecutando con el comando:

    *$ ps -ef \| grep sshd root 29080 1 0 12:09 ? 00:00:00
    /usr/sbin/sshd manuel 29154 29087 0 12:11 pts/4 00:00:00 grep sshd*

La primer línea nos indica que el demonio esta activo. Se pueden
configurar varias opciones del servidor de SSH editando el archivo
*/etc/ssh/sshd_config*, por ejemplo para cambiar el puerto por el cuál
trabaja. Yo tuve que utilizar esta opción ya que en la facultad tienen
bloqueado el puerto por defecto (puerto 22).

Podemos *loguearnos* de forma remota en nuestro equipo utilizando
cualquiera de las cuentas de usuario que tengamos creadas en el sistema.
Yo por ejemplo tengo una únicamente *"manuel"*. Tenemos varias formas de
hacerlo:

**SSH desde un sistema Linux:**

La manera más sencilla de hacerlo es, si estamos en un entorno gráfico
abrimos una consola y tipeamos:

    *$ ssh usuario_remoto@ip_remota*

Por ejemplo, desde la otra PC que tengo en red:

    *$ ssh manuel@10.0.0.5 manuel@10.0.0.5's password:*

**SSH desde un sistema Linux con
`MC <http://es.wikipedia.org/wiki/Midnight_Commander>`__:**

De esta forma podemos tener en la vista izquierda nuestra PC local y en
la derecha la máquina remota, por lo que podemos ejecutar todas las
opciones que nos permite el MC. Entre ellas, copiar, cortar, editar,
etc...

|image0|

|image1|

|image2|

Desde una consola tipeamos *mc,*\ lo que nos abre el Midnight Commander,
vamos a la configuración de la vista derecha, por ejemplo, con la tecla
rápida F9 y elegimos *"conexión por sHell"*\ Luego en la ventanita que
se abre escribimos algo similar a lo q

ue tipeamos anteriormente en la consola, con la direfencia que tenemos
que anteponer */#sh:* seguido de lo mencionado arriba.

Finalmente nos pide el *password* y una vez ingresado de forma correcta
nos permite explorar los directorios de la máquina de remota.

**SSH desde un sistema Windows:**

Para esto necesitamos un programita pequeño pero **muy**\ eficaz llamado
`PuTTY <http://es.wikipedia.org/wiki/Putty>`__, el cuál es libre y se
puede descargar su ejecutable desde
`aquí <http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe>`__. No
necesita ser instalado ni mucho menos, sólo doble click y listo.

*Los screenshots de el programa PuTTY son de Linux emulado con Wine, ya
que no tengo Windows en esta computadora.*

Una vez que abrimos el PuTTY nos muestra la pantalla de configuración,
en la que ingresamos el IP de la máquina remota y le damos "Open".

|image3| |image4|

**Algunos Tips:**

-  Programas gráficos, si le pasamos el parámetro *-X*\ al comando
   *ssh*\ este nos visualizará la parte gráfica en la computadora local.
   Lo he probado con pocas aplicaciones y funcionó, por ejemplo el juego
   Twisted Zombie, se ve un poco lento mediante SSH. Pero quizás para
   visualizar fotos y demás sea **muy**\ útil ya que podemos usar todos
   los programas que tenemos instalados en la máquina remota. Ejemplo:

    *$ ssh -X manuel@10.0.0.5*

Ahora cuando ejecutemos cualquier comando que requiera interfaz gráfica,
lo visualizaremos correctamente en la PC en que nos encontramos
físicamente.

-  Copia de archivos, podemos copiar archivos desde el equipo remoto
   hacia el local y viceversa utilizando los siguientes comando
   respectivamente:

    $ scp usuario@ip_remota:archivo_remoto archivo_local $ scp
    archivo_local usuario@ip_remota:archivo_remoto

.. |image0| image:: http://img214.imageshack.us/img214/4560/mc1ly5.th.png
   :target: http://img214.imageshack.us/img214/4560/mc1ly5.png
.. |image1| image:: http://img258.imageshack.us/img258/2373/mc2ec5.th.png
   :target: http://img258.imageshack.us/img258/2373/mc2ec5.png
.. |image2| image:: http://img258.imageshack.us/img258/8874/mc3gl6.th.png
   :target: http://img258.imageshack.us/img258/8874/mc3gl6.png
.. |image3| image:: http://img161.imageshack.us/img161/1523/putty1rt7.th.png
   :target: http://img161.imageshack.us/img161/1523/putty1rt7.png
.. |image4| image:: http://img161.imageshack.us/img161/4999/putty2uf2.th.png
   :target: http://img161.imageshack.us/img161/4999/putty2uf2.png
