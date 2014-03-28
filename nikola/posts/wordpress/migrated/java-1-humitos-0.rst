.. link:
.. description:
.. tags: java
.. date: 2007/09/14 19:33:50
.. title: Java 1 - Humitos 0
.. slug: java-1-humitos-0


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/09/14/java-1-humitos-0/


Este es el resultado del primer tiempo. Entre la mitad del día de ayer y
todo el día de hoy estuvimos intentando hacer una *mini* aplicación
gráfica con un amigo, `Guille <http://gheize.wordpress.com>`__. En la
tarde de ayer investigamos un poco el lenguaje, hicimos ejercicios de la
guía de actividades de la materia que estamos cursando en la facu (DIED:
*Diseño e implementación de estructura de datos*) y anduvimos bien, ya
que es muy parecido a C++ la sintaxis. Aparte yo había leído la primer
parte del libro *"Aprenda Java como si estuviera en primero"*\ asique
**algo** sabíamos.

Como siempre, hacer ejercicios que no sirven de nada, no tienen ninguna
utilidad, y son aburridos de programar, pensamos en hacer algo un poco
más **lindo** y **agradable** para los dos. Pero tampoco queríamos algo
que sea muy complicado. Entonces nos decidimos por una calculadora *de
bolsillo* con una pequeña
`GUI <http://es.wikipedia.org/wiki/Interfaz_gr%C3%A1fica_de_usuario>`__.
Seguido de esto pensámos que bibliotecas gráficas utilizar, SWT, AWT,
etc... Creamos un `proyecto <http://code.google.com/p/jcalculation/>`__
en Google Code y todo! **Ya**\ queríamos empezar, nos habían venido las
pilas nuevamente.

Al principio *nos daba igual* una librería o la otra, entonces empezamos
por la que nos pareció que era mejor: **SWT** ya que por varios
screenshots que vimos en internet se veía *lindo* en Linux y Windows.
Buscamos e instalamos todo lo necesario en mi máquina y nos pusimos
manos a la obra. Para esto abrimos el Kate ;) y comenzamos a tipear
hasta que teníamos algo, a modo de ejemplo, que muestre sólo una ventana
y nada más. Vamos a la consola y tipeamos:

    *$ javac Run.java*

Ups! Un error que decía que no conocía la clase para crear la ventana de
SWT que queríamos hacer. Fácilmente lo localizamos, descargamos las
librerías para Linux e intentamos nuevamente. Previo a esto encontramos
en Google, gracias a `Juanjo <http://www.juanjoconti.com.ar/>`__, que se
le debía pasar el PATH en dónde se encontraban las librerías que íbamos
a utilizar.

    *$ javac Run.java -classpath swf.jar* *$*

Esto significa que compiló sin errores algunos por lo que *sonreímos* y
ejecutamos el siguiente paso inmediatamente.

    *$ java Run* *Exception in thread "main"
    java.lang.NoClassDefFoundError: [...]*

Lo que nos desilucionó bastante, ya que pensábamos que íbamos a poder
empezar a programar anoche :( Hicimos mil búsquedas en Google y
preguntamos a un montón de personas vía *chat* qué prodría llegar a ser
esto hasta las **3 am**. La verdad terminamos muertos!

Al otro día se nos dió por probar el
`Eclipse <http://www.eclipse.org/>`__ en mi máquina para ver si este
simplificaba algo las cosas. Ya que estábamos desesperados porque
probamos mil cosas (seguro que era una boludez lo que pasaba, pero hay
que saber hacerlo).

    *$ sudo apt-get install eclipse*

Y ¿problema resuelto? **NO!!** nos trajo más problemas que beneficios,
enseguida al momento de abrirlo mi máquina pedía oxígeno (RAM), lo que
no le pude suministrar ni creo que pueda, al menos por el momento. Cerré
absolutamente todo lo que no era necesario para programar, e intentamos
seguir un tutorial de cómo crear el Hello World con SWF que tenía el
Eclipse en la ventana de Welcome. Sinceramente fué imposible e
insaluble, ese programa es un mounstruo. Asique automáticamente buscamos
alternativas. Guille mencionó `NetBeans <http://www.netbeans.org/>`__.
Listo, descargá e instalá contesté.

Grrr... Igual o más pesado que el Eclipse! Dejamos las librerías SWT de
lado y buscamos el libro que yo tengo para ver con cuales trabaja: AWT.
No se habla más, volvimos al maravilloso mundo del Kate y seguimos los
pasos del libro. Nos pusimos a tipear todo el código que necesitábamos
para hacer una simple ventana y *voilá*. La ventana se veía, **muy**
fea, pero se veía. Ya era un avance, **gran** avance.

No discutimos más y nos pusimos manos a la obra para hacer dos o tres
botones y tratar de sumar dos números. Pasaron 45 minutos o más y
estábamos intentando meter el primer botón en la ventana que se
mostraba. A todo esto no teníamos muy buena onda ya, estábamos cansado y
además estamos **extremadamente**\ acostumbrados a
`Python <http://www.python.org>`__ que con dos líneas ves resultados!

Se nos ocurrió la idea de usar Eclipse o NetBeans únicamente para hacer
la parte gráfica, entonces, volvimos de nuevo al NetBeans e intentamos
crear un proyecto (luego de los 12,47 minutos que demoró en cargar),
para luego insertar una ventana y agregarle unos botones y nada más,
sinceramente es inusable este programa también. Pasamos a la solapa en
la que te muestra el código y vimos que eran algo así como
quichisientasmil líneas de código por lo que cerramos el programa
automáticamente y nos pusimos a pensar seriamente (mientras este se
comía la pc) que no podíamos desarrollar una aplicación gráfica sin un
diseñador de ventanas (estilo `Glade <http://glade.gnome.org/>`__ o `Qt
Designer <http://trolltech.com/products/qt/features/designer>`__).

Asique investigamos lo que quedaba de la tarde en ver si se podían
diseñar ventanas con Glade, Qt Designer o cualquier otro programa, y
luego pasarlas a código Java. Encontramos un comando que pasaba lo hecho
en Qt Designer a código Java pero utilizando las librerías Qt. Probamos
y el compilador no encontraba el PATH de las librerías. Asique nos dimos
por vencidos y dejamos todo de lado.

Java, estámos esperando la revancha!
