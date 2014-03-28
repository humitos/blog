.. link:
.. description:
.. tags: python, ubuntu
.. date: 2007/09/18 12:29:47
.. title: Crear un paquete Debian (.deb) de un programa en Python (.py)
.. slug: crear-un-paquete-debian-deb-de-un-programa-en-python-py


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/09/18/crear-un-paquete-debian-deb-de-un-programa-en-python-py/


|image0|\ Siempre quise aprender a hacer paquetes Debian porque muchas
veces les quería pasar mis programas a mis amigos y se quejaban que
tenían que instalar muchas dependencias o quizás eso me decían a mí para
no correr mis programas en sus máquinas.

También porque evitás todo tipo de explicación de cómo se instala, cuál
es el *.py* que se debe ejecutar, que versión de Python, y muchas otras
cosas. Además que queda lindo ya que podemos hacer que lo ponga en el
Menú K en KDE o Gnome en su correspondiente panel de aplicaciones
indicándole cuál va a ser su ícono y demás.

Hace mucho tiempo me puse a investigar e incluso me leí toda la `guía de
desarrolladores de
Debian <http://linux-cd.com.ar/manuales/debian-desarrollo/index.es.html>`__
la cuál en ese momento no me sirvió, quizás porque no la entendí o
porque no estaba directamente relacionada con Python (y yo recién
empezaba con ambos).

El 9 de Junio de éste año se llevó a cabo la `2da Jornada de Python en
Santa Fé <http://www.python-santafe.com.ar/>`__ en la que vino gente de
otros lados del país y tuve la posibilidad de alojar a dos chicos en mi
casa; `Héctor Sánchez <http://www.karuchin.com.ar/>`__ y `Hugo
Ruscitti <http://www.losersjuegos.com.ar/principal/principal.php>`__ de
Buenos Aires, a los cuales *aproveché*\ para preguntarle de todo tipo de
cosas :D sobre en lo que yo estaba fresquito y ellos ya tenían un poco
más de experiencia.

Cómo Hugo se dedicaba a hacer juegos para una distribución de Debian y
había cosas que hacía en Python le pregunté cómo hacer un paquete de uno
de mis juegos (`Tweety
Finger <http://code.google.com/p/tweety-finger/>`__) y me ayudó a
crearlo en ese momento, explicándome que era lo **básico** para hacerlo
y siguiendo de ejemplo un paquete existente. Existen *muchas* opciones
para crear un paquete Debian, como por ejemplo los *nombres genéricos*
en los distintos idiomas, los cuales son tediosas de indicar e incluso
ni los sabemos; y a mí me interesaba que sean de fácil instalación mis
programas.

Lo más recomendable es *leer*\ la guía expuesta arriba o buscar
información en Google de la estructura de los paquetes de Debian, para
saber y comprender cuáles son las opciones mínimas para que cumpla los
estándares de Debian y poder ser redistribuido e incluso incluído en
alguna de las distribuciones de Debian y sus derivadas.

Lo primero que hice fué abrir una terminal y entrar al programa **mc** y
buscar en la carpeta */var/cache/apt/archives* algún paquete que halla
descargado anteriormente para basarme en su estructura y ver cómo
estaban configurado los distintos archivos. Hoy tenía que hacer otro
paquete y siempre me olvido cómo se hacen, asique agarré de ejemplo el
Kate.

Lo más importante a tener en cuenta es la estructura de directorios del
paquete y el archivo *DEBIAN/control*. Éste es un archivo de texto que
se utilizar para indicar las dependecias del paquete, una descripción
corta, una larga, el nombre, la versión, etc.

Explico la estructura del paquete que vamos a crear con un ejemplo, el
del paquete que acabo de crear recién para el juego `Twisted
Zombie <http://zombie.firebirds.com.ar>`__.

::

    DEBIAN/
        control
    usr/
        share/
            applications/
                twisted-zombie.desktop
            pixmaps/
                twisted-zombie-icon.png
            twisted-zombie/
                data/
                lib/
                COPYING
                README.txt
                create-upload.py
                pyweek-upload.py
                run_game.py

El archivo `DEBIAN/control <http://paste-it.net/3597/raw/>`__ es que el
expliqué anteriormente. La estructura */usr/share/[...]*\ indica dónde
se va a copiar el contenido de ésta; por ejemplo el archivo
*run_game.py* quedará instalado en nuestro sistema con en la ruta
*/usr/share/twisted-zombie/run_game.py*.

El otro archivo importante es
`/usr/share/applications/twisted-zombie.desktop <http://paste-it.net/3598/raw>`__
ya que en este indicamos en dónde se va a ubicar en el Menú K, que órden
debe ejecutarse cuando se llame, qué ícono tendrá, etc. Se pueden ver
los archivos de este ejemplo en los links de cada uno de estos (arriba).

En los archivos fuente (.py) que carguemos archivos externos, como ser
imágenes, sonidos etc; debemos hacer un *change dir* a la **nueva**
ubicación de nuestro programa (en este
caso\ */usr/share/twisted-zombie*) agregando la línea:

    *os.chdir("/usr/share/twisted-zombie")*

Para que al ser llamado desde cualquier otra ruta el programa siempre se
posicione dónde él sabe que tiene los archivos a cargar.

Una vez creada la estructura anteriormente mostrar y configurado los
archivos mencionados a *gusto*, se puede ejecutar este comando para
crear el paquete:

    *$ dpkg --build twisted-zombie/ twisted-zombie-1.0_all.deb*

Si la estructura de la carpeta twisted-zombie/ está mal formada, el
comando nos informa de esto, incluso también si al archivo *control*\ no
le dejamos un espacio en blanco en la última línea, y demás.

El nombre que se le da es de la forma
*<nombre-paquete>-<version>_<arquitectura>.deb*.Luego para probar que
esto funciona correctamente lo instalamos:

    *$ dpkg -itwisted-zombie-1.0_all.deb*

Si algo salió mal, por ejemplo, al hacer click en el Menu K no aparece
nuestro programa basta con buscar el error en el archivo
twisted-zombie.desktop, desintalar el programar, crear el paquete e
instalarlo nuevamente. Para desintalarlo lo hacemos cómo si fuera
cualquier otro paquete:

    *$ sudo apt-get removetwisted-zombie*

Espero que sirva esto y no haberme olvidado ningún paso del proceso,
parece complicado, pero es algo simple; como todo, al principio es
complicado o por lo menos parece. Pero al poder ver cómo están
construidos los demás es fácil guiarse. Incluso se puede usar un paquete
más chico de ejemplo que el Kate.

Cualquier cosa que no se entienda o no quede bien en claro comenten y
depaso me hacen seguir estudiando ;)

.. |image0| image:: http://img212.imageshack.us/img212/2928/debianpythonze3.png
