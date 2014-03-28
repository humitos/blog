.. link:
.. description:
.. tags: circo, general
.. date: 2010/11/13 15:26:34
.. title: Welcome to the Juggle, baby!
.. slug: welcome-to-the-juggle-baby


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2010/11/13/welcome-to-the-juggle-baby/


En la PyConAr 2010 estuve hablando con `Héctor
Sanchez <http://www.karuchin.com.ar/wordpress/>`__, un amigo de la
comunidad de Python de hace varios años ya. En pocas palabras, un
tipaso. Por lo general lo veo poco y chateamos... "nunca", por decir la
verdad. Pero cuando nos encontramos en algún tipo de evento o situación
tratamos de ponernos al tanto de nuestras vidas y pasar un buen rato
charlando.

En esta oportunidad uno de los temas que conversamos fue mi comienzo en
el circo y sobre las actividades que hacemos en la escuelita. También le
dije que me compré unas clavas y ahí el me contó de un amigo que daba
una charla que se llamaba "**Malabares y Software Libre**\ ". What the
fuck!?

Héctor intentó explicarme de qué se trataba la charla y me dijo que el
tipo este mostraba algunos programas didácticos para hacer malabares.
Sinceramente, en ese momento no le creí y pensé que me estaba jodiendo.
Me siguió contando un poco más y me dijo que busque en Google y demás
(todas esas cosas nerd que uno hace para demostrar la veracidad de
alguna cosa).

La cuestión es que busqué en Google y encontré un montón de información
sobre malabares y computadoras. Realmente hay muchos simuladores de
malabares y son bastante didácticos y útiles.

Dejo acá algunos links que me parecieron interesantes:

-  http://www.juggling.org/programs/java/
-  http://www.jugglingdb.com/compendium/geek/software/simulators.html
-  http://www.jongl.de/

El que actualmente estoy probando, es Jongl. Aunque es un poco
complicado de configurar, parece que está bastante bueno ya que permite
hacer muchas cosas. En alguna otra oportunidad, cuando lo tenga un poco
más visto al programa, comentaré más cosas. Por ahora, dejo estos links
para los que se quieren poner a ver esto.

|image0|

Si sabés de otros programas (para cualquier plataforma), decime cuál es
así lo pruebo. También usá los comentarios para comentarme si te
sirvieron esos programas y si encontraste algunas opciones interesantes.

Explico cómo hice para instalarlo, ya que tuve que descargar algunas
cosas más además del programa en sí. Los pasos están hechos en un Debian
Squeeze (testing).
``  wget -c http://www.jongl.de/download/jongl-14.0-linux.tgz  sudo apt-get install libpng3 libgl1-mesa-swx11 tcl8.4 tcl8.4-dev ``

Luego para ejecutarlo, hay que escribir escribir este comando:
``  ./jongl ``

El comando que utilicé para buscar los programas que tuve que instalar
con apt fue este:
``  [humitos] [~/juggle/jongl/JonglV14.0]$ ldd jongl  linux-gate.so.1 =>  (0xb782b000)  libglut.so.3 => /usr/lib/libglut.so.3 (0xb77d5000)  libGLU.so.1 => /usr/lib/libGLU.so.1 (0xb7765000)  libGL.so.1 => /usr/lib/libGL.so.1 (0xb769b000)  libX11.so.6 => /usr/lib/libX11.so.6 (0xb757e000)  libXext.so.6 => /usr/lib/libXext.so.6 (0xb756f000)  libXi.so.6 => /usr/lib/libXi.so.6 (0xb7562000)  libXmu.so.6 => /usr/lib/libXmu.so.6 (0xb754c000)  libm.so.6 => /lib/i686/cmov/libm.so.6 (0xb7526000)  libpng.so.3 => /usr/lib/libpng.so.3 (0xb7501000)  libz.so.1 => /usr/lib/libz.so.1 (0xb74ed000)  libtcl8.4.so => /usr/lib/libtcl8.4.so (0xb7435000)  libtk8.4.so => /usr/lib/libtk8.4.so (0xb7353000)  libc.so.6 => /lib/i686/cmov/libc.so.6 (0xb720d000)  libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0xb7117000)  libgcc_s.so.1 => /lib/libgcc_s.so.1 (0xb70f9000)  libnvidia-tls.so.260.19.12 => /usr/lib/tls/libnvidia-tls.so.260.19.12 (0xb70f7000)  libnvidia-glcore.so.260.19.12 => /usr/lib/libnvidia-glcore.so.260.19.12 (0xb5a47000)  libdl.so.2 => /lib/i686/cmov/libdl.so.2 (0xb5a43000)  libxcb.so.1 => /usr/lib/libxcb.so.1 (0xb5a29000)  libXt.so.6 => /usr/lib/libXt.so.6 (0xb59d7000)  /lib/ld-linux.so.2 (0xb782c000)  libpthread.so.0 => /lib/i686/cmov/libpthread.so.0 (0xb59be000)  libXau.so.6 => /usr/lib/libXau.so.6 (0xb59bb000)  libXdmcp.so.6 => /usr/lib/libXdmcp.so.6 (0xb59b6000)  libSM.so.6 => /usr/lib/libSM.so.6 (0xb59ad000)  libICE.so.6 => /usr/lib/libICE.so.6 (0xb5996000)  libuuid.so.1 => /lib/libuuid.so.1 (0xb5992000)  [humitos] [~/juggle/jongl/JonglV14.0]$ ``

En este caso, tengo todas las librerías necesarias, pero puede ser que
alguna falte y el mensaje sería "Not found" o similar. Después, con el
nombre del archivo en mente, utilicé "apt-file search" o "apt-cache
search" para buscar el paquete necesario.

Además tuve que crear un symlink hacia una lib en mi caso:
``  $ sudo ln -s /usr/lib/libtk8.4.so.0 /usr/lib/libtk8.4.so ``

¿Algo más?

.. |image0| image:: http://www.jongl.de/pics/V14.0-Fogo.jpg
