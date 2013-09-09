.. link:
.. description:
.. tags: debian, software libre
.. date: 2010/06/18 20:15:35
.. title: GREP_OPTIONS is the evil
.. slug: grep_options-is-the-evil

Sí, cómo dice el título: no es nada bueno tener la variable de entorno
GREP_OPTIONS configurada en el entorno en el que se está trabajando.

La semana pasada tuve varios problemas por esta misteriosa variable,
pero vamos de a poco contando porqué la configuré y porqué me causó
tantos problemas.

El motivo por el cuál configuré esta variable es porque me gustan un par
de opciones de **grep** y no las quiero escribir cada vez que lo uso a
este comando, es similar a un alias, pero funciona de otra forma.

Por ejemplo, si configuro un alias de esta forma:

``alias grep='grep --color'``

cuando ejecuto **grep** en la terminal, bash hace la sustición de "grep"
por "grep --color" antes de ejecutar el comando "grep".

Por el contrario, si seteamos la variable GREP_OPTIONS de esta forma:

``export GREP_OPTIONS='--color'``

cuando ejecutemos en una terminal "grep" bash ni se entera de que está
esta variable configurada y es el comando **grep** quién lee esta
variable para tomar las configuraciones del entorno.

Normalmente, esto no causa ningún problema, siempre y cuando
configuremos opciones de **grep** que no modifiquen la salida. En
cambio, si usamos opciones como **--line-number** que agrega el número
de la línea en dónde matcheo la expresión que pusimos esto puede causa
problemas.

Hay programas, scripts, y demás, que esperan una salida en particular de
un comando y a esta se la entuba (mediante un pipe \|) y posiblemente
luego se la pase mediante un **sed** para tomar la parte relevante.
Entonces, ¿qué pasa si agregamos un número de línea al principio de cada
línea en la que la expresión regular matchea? es simple: el programa
**crashea**.

Esto me paso utilizando virtualenvwrapper, ya que utiliza este comando
para ubicar el PATH de virtualenv:

``humitos@eulogia:~$ (\which virtualenv | grep -v "not found")  /usr/bin/virtualenv  humitos@eulogia:~$``

Ahora, si activamos esta variable para que muestre el número de línea...
Veamos que pasa y porqué falla:

``humitos@eulogia:~$ export GREP_OPTIONS='--line-number'  humitos@eulogia:~$ (\which virtualenv | grep -v "not found")  1:/usr/bin/virtualenv  humitos@eulogia:~$``

Lo mismo sucede si creamos un alias:

``humitos@eulogia:~$ unset GREP_OPTIONS  humitos@eulogia:~$ alias grep='grep --line-number'  humitos@eulogia:~$ (\which virtualenv | grep -v "not found")  1:/usr/bin/virtualenv  humitos@eulogia:~$``

Sinceramente, este problema es muy básico, pero en diferentes scripts de
configuración del sistema operativo o en scripts que se utilizan para
compilar programas y librerías, te aseguro que puede ser un gran dolor
de cabeza debuggear porqué no está funcionando como uno espera.

Referencias y links:

-  https://bugs.launchpad.net/ubuntu/+source/mysql-dfsg-5.0/+bug/75031
-  https://bugs.launchpad.net/ubuntu/+source/devscripts/+bug/581319
-  http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=432873
-  ﻿\ http://bitbucket.org/dhellmann/virtualenvwrapper/issue/51/unset-grep_options-before-using-grep

