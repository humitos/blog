.. link:
.. description:
.. tags: general
.. date: 2010/08/29 15:56:57
.. title: Uso práctico de VNC
.. slug: uso-practico-de-vnc


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2010/08/29/uso-practico-de-vnc/


Actualmente tengo una computadora de escritorio, que dejo siempre
prendida y uso como server: para descargar cosas de internet, para
guardar la música, como backup, servidor web y demás.

Como todas las cosas que bajo de internet están en ese equipo, necesito
organizar las cosas que bajo y no siempre uso un programa en modo texto
(consola) para hacer esto. Por ejemplo, si es un disco con mp3 me gusta
ponerle los ID3 correctos con **easytag**, o si bajo un DVD9 lo tengo
que convertir a DVD5 para poder grabarlo y lo hago con **k9copy**.

Para estos programas necesito tener una interfaz gráfica, entonces uso
VNC para ello. De hecho, normalmente tengo corriendo el **JDownloader**
en un VNC porque lo quiero tener siempre abierto, pero no quiero que me
moleste en la barra de tareas y además también me interesa controlarlo
remotamente, si bien para esto uso el servidor web que trae, éste no
cubre toda la funcionalidades que se pueden hacer mediante la interfaz
gráfica. Por ejemplo, ingresar los códigos que piden algunos File
Hosting.

Entonces, la idea de esto es, levantar un servidor VNC y ejecutar
programas dentro de éste (sin que alteren el escritorio actual) y luego
poder comandar estos programas que lanzamos en el VNC desde cualquier
otro equipo. Mi idea fue así::

    vncserver :4 export DISPLAY=michifus:4 java -Xmx512m -jar ~/.jd/JDownloader/JDownloader.jar &

Con esto estoy levantando un servidor en el display 4 de **localhost**
(que se llama **michifus** en la red). Entonces, después exporto ese
display para ser usado por los programas y ejecuto el JDownloader.

Luego, desde otra PC me conecto usando el **xtightvncviewer**::

    xtightvncviewer michifus:4

Y ahora puedo administrar el JDownloader mediante VNC como si estuviera
sentado en la PC que lo está ejecutando realmente. Esto es normalmente
lo que tengo ejecutando en el VNC siempre. Además, cuando bajo algo como
antes comentaba, quiero levantar otro programa; para eso me conecto por
**ssh**\ al servidor y hago::

    export DISPLAY=michifus:4 k9copy &

Luego me conecto nuevamente por VNC a **michifus** y veo que se cargó el
**k9copy** en el escritorio que estoy sirviendo por VNC.
