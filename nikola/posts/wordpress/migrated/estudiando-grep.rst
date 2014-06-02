.. link:
.. description:
.. tags: software libre, ubuntu
.. date: 2007/11/11 14:59:50
.. title: Estudiando "grep"
.. slug: estudiando-grep


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/11/11/estudiando-grep/


|image0|

Después de tantas luchas para saber si lo que `estoy haciendo
en
Java <http://humitos.wordpress.com/2007/11/09/python-mas-rapido-que-java/>`__
funcionaba como debería funcionar, me puse a estudiar el comando
*`grep <http://es.wikipedia.org/wiki/Grep>`__.*

**"grep"** es un comando que te permite buscar un patrón de
coincidencias en archivos de texto, mostrándote la línea entera en dónde
se encontró esta coincidencia. Es bastante configurable y también
permite `expresiones
regulares <http://es.wikipedia.org/wiki/Expresiones_regulares>`__ para
indicar este patrón.

Este comando puede recibir el nombre del archivo sobre el cuál se debe
buscar el patrón o puede tomar la información desde la entrada estándar,
por ejemplo:

::

    [manuel] [~]$ grep manzana diccionariocs.txt

    amanzanamiento

    amanzanar

    manzana

    manzanal

    manzanar

    [manuel] [~]$ cat diccionariocs.txt | grep manzana

    amanzanamiento

    amanzanar

    manzana

    manzanal

    manzanar

    [manuel] [~]$

*El archivo diccionariocs.txt contiene muchas palabras (una por línea) y
es el que nos dieron en la cátedra de la materia para realizar el
trabajo de Java.*

La idea era poder saber si el resultado que me arrojaba mi árbol de
búsqueda era lo que realmente me tenía que estar devolviendo o no, en
otras palabras, si funcionaba o se mandaba cualquiera. Asique me hice un
`intérprete
interactivo <http://img137.imageshack.us/img137/7421/interpretejavaxs4.png>`__
en Java para poder realizar varias búsquedas sobre el árbol una vez que
esté cargado en memoria (suena wow!, pero es una boludez lo que hice :P
).

El intérprete te informa cuales son las palabras que encontró y cuál fue
la cantidad de palabras que concordaron con la búsqueda. Pero con el
comando anterior me está mostrando todas las líneas en las que aparece
la cadena **manzana**, y sólo necesito las líneas (palabras) que
empiecen con **manzana**, como muestra mi intérprete:

::

    [manuel] [~/proyectos/procesadorpalabras]$ java Main

    Cargando diccionario...

    Diccionario cargado correctamente.

    Ingresando al modo interactivo...

    >>> manzana

    manzana

    manzanal

    manzanar

    Total de coincidencias: 3

    >>>

Asique pregunte, y me dijeron que **grep** soporta expresiones regulares
(hasta ese momento yo no lo sabía) y me bastó con poner el siguiente
comando:

::

    [manuel] [~]$ grep ^manzana diccionariocs.txt

    manzana

    manzanal

    manzanar

    [manuel] [~]$

Notar el "^" que se antepone a la cadena **manzana**, de este modo logré
mostrar sólo las palabras que me interesaban. Pero también tuve un
problema, si hago la consulta "empieza con a", me tira tres millones de
resultado (¿tanto?), más o menos, y quién va a contar línea por línea
cuántos son en total: NADIE... Busqué y encontré que tiene una opción
para que te devuelva la cantidad de líneas que coinciden con el patrón:

::

    [manuel] [~]$ grep ^a diccionariocs.txt -c

    9996

    [manuel] [~]$

Lo que demoró milésimas de segundo. Hice la misma búsqueda con mi
programa y todavía estoy esperando la respuesta, está bien, el mío
además está imprimiendo los resultados en pantalla, y eso demora... :(

::

    >>> a

    [...]

    Total de coincidencias: 9954

    >>>

Ups, parece que no está andando a la perfección mi programa, se comió
9996 - 9954 =
**`42 <http://es.wikipedia.org/wiki/El_sentido_de_la_vida,_el_universo_y_todo_lo_dem%C3%A1s>`__**\ palabras.
Tendré que revisar el código o ver que está pasando (recién me entero de
esto).

**Update 11/11:** estuve revisando el código y ví que no ingresaba las
palabras que sean subpalabras de otras, esto es, si primero lee desde el
archivo\ *palabra* y después lee *pala*, esta última no la ingresaba.
Pero si las leía en orden inverso no había ningún problema, por eso
parecía que funcionaba bien, porque la mayoría de las palabras están
ordenas alfabéticamente entonces esto era **casi** transparente. Igual
sigo con un problema ya que al buscar *a* encuentra 9965, le están
faltando 9996 - 9965 = 31 palabras todavía :( .

**Update 12/11:** como no podía ser de otra forma, como me pasa en
*todos*\ los lenguajes que programo, tengo problemas de codificación.
Esto es, si hay palabras como *buchón ybuchín*, devuelve una de estas
dos, ya que **ú** e **í** las toma como el mismo caracter. Ya veremos...

Otras opciones que me parecen útiles y que he utilizado anteriormente
copiando el comando de páginas o blogs sin saber qué significaban son:

-  **-i** No hace caso de si las letras son mayúsculas o minúsculas, ni
   en el patrón ni en los ficheros de entrada.
-  **-n** Además de la línea con la concordancia, antepone el número de
   la misma.
-  **-v**\ Invierte el sentido de la concordancia, para mostrar las
   líneas en donde no las hay.
-  **-w**\ Sólo muestra aquellas líneas en dónde la palabra se encuentre
   completa, esto es, donde la palabra se encuentre precedida y sucedida
   de un caracter de espacio.

Referencias: `manpage grep <http://man.cx/grep(1)/es>`__

La publicación de este documento se demoró debido a que me encapriché
con que quería ponerle un dibujo, buscando en
`Google <http://www.google.com.ar>`__ caí a `ésta
página <http://www-psych.stanford.edu/~gruffydd/290/grepsedawk.html>`__
en la que ví el
`bicho <http://www-psych.stanford.edu/~gruffydd/290/grep.jpg>`__ y me
gustó :P . Cómo tenía ganas de *no hacer nada*, me puse a copiarlo desde
el monitor en un papel (soy pésimo dibujando ¿se nota?, en mi vida he
hecho dibujos, pero este me pintó y lo hice).

Después quise pintarlo y demás con el `Gimp <http://www.gimp.org/>`__ y
el `Inkscape <http://www.inkscape.org/>`__, pero no hubo caso, asique lo
dejé así nomás, como lo había dibujado en un papelito... Y bueno, los
ingenieros no estamos para estas cosas... ;)

.. |image0| image:: http://img80.imageshack.us/img80/7391/grepresizema9.jpg
