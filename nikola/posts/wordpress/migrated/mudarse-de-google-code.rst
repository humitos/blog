.. link:
.. description:
.. tags: google, internet, proyectos, python
.. date: 2007/11/18 02:23:18
.. title: Mudarse de Google Code
.. slug: mudarse-de-google-code

Desde que monté un servidor en mi casa de svn para probar algunas cosas,
y debido a que Google Code no me dejaba crear más proyectos. Me convencí
que el servicio que brinda Google es **demasiado** **lento** en
comparación con un servidor propio (¡Ojo! yo no tengo una conexión muy
buena y anda a las mil maravillas el servicio).

Entonces empecé a pensar en mudarme de google e irme a un servidor
propio (o de *alguien* ;) ). Cuando lo decidí empecé a buscar una forma
de sacar mis proyectos de esta página. Pregunté en varios lados y a
varias personas sobre esto, me dijeron que no sabían y que incluso
seguramente que no se podía. Me recorrí *toda* la página de Google
buscando una respuesta, las páginas de mis proyectos, pero nada...

Pensé en hacerme un script que baje desde la primer versión hasta la
última y valla haciendo commits de manera alternada. Pero el problema es
que las fechas de los commits y los usuarios que lo hacían iban a quedar
en cualquiera.

Seguí buscando un poco más, preguntando en los canales de irc amigos, y
al final encontré un programa llamado
`svk <http://svk.elixus.org/view/HomePage>`__, que la verdad **se la re
banca**. Lo que hace el pibe es bajarte el repositorio de google (o
cualquier otro hosting que tenga el servicio de svn) **tal cual** como
lo tenías en ese servidor. Osea, sin perder absolutamente nada. Ni los
logs, ni las fechas ni ná. Y te crea un repositorio local para usarlo
como si fuese el de google pero ahora siendo administrador y no sólo
cliente como te permite Google. Por ejemplo para bajar el repositorio de
mi proyecto Kpaper hago:

::

    $ svk mirror //local http://kpaper.googlecode.com/svn/

    $ svk sync //local

**Update 19/11/07:** bastante feo de mi parte, no había probado esto en
el servidor en el cual me estaba mudando. Cuando lo hice descubrí que el
comando correcto a ejecutar es:

::

    $ svk mirror // http://kpaper.googlecode.com/svn/

    $ svk sync //

Porque sino, de la otra manera estaba creando un subdirectorio en
nuestros repositorios porque lo quedaba en cualquiera a la hora de
importarlo con **svnadmin load**.

De esta forma en el directorio *~/.svk/local* me crea el repositorio
local. Incluyendo los directorios *branches, trunk*\ e\ *etiquetas.*
Para acceder a este código en forma de repositorio (como si estaría en
Google):

::

    $ svn co file:///home/manuel/.svk/local/mirror/trunk kpaper

Ahora bien, si queremos mudarlo a otro hosting podemos hacer un **dump**
con el comando svn, guardarlo todo en un solo archivo y transportarlo al
servidor que más nos guste :) :

::

    $ svnadmin dump -r2:HEAD ~/.svk/local/mirror/ > kpaper.svn.repository

Le saco la primer revisión porque es una que crea este comando (svk).
Bueno ahora podemos hacer lo que queremos con **nuestro** código y ahora
si **somos dueños** del servicio svn.

Y para terminar, me hice un `script en
Python <http://www.paste-it.net/4621>`__ (por supuesto) para bajar más
de un proyecto y no tener que memorizarme estos comandos. Se le pasa la
lista de los nombres de proyectos que queremos bajar separados por
espacios en blanco y listo.

Quiero mejorarlo un poco, ya que cada vez que baja uno te pregunta si
querés crear una carpeta. Ahora no tengo muchas ganas de *pensar*,
después lo veo :P .
