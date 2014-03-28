.. link:
.. description:
.. tags: blog, charla, django, python, software libre
.. date: 2010/09/11 18:00:35
.. title: Introducción a Django (charla)
.. slug: introduccion-a-django-charla


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2010/09/11/introduccion-a-django-charla/


Es la primera vez que voy a hacer esto, no estoy seguro porqué se me
ocurrió en este momento, pero ya lo había visto en el blog de
`Juanjo <http://www.juanjoconti.com.ar>`__ hace un tiempo aunque no le
dí mucha bola y ahora que me surgió **la idea** nuevamente, me acordé
que ya lo había visto y que **la idea no era mía** :P

Voy a intentar *dar la charla* por mi blog, para todos los que alguna
vez la quisieron ver y no tuvieron la oportunidad o ya han ido y se
quedaron con dudas, o simplemente para los que les interese :)

Voy a ir mostrando cada una de las diapositivas y tratando de escribir
lo que *debería* decir en cada una de ellas, aunque no estoy seguro si
va a quedar lindo, vamos a probar a ver que pasa.

|image0|

Para ir rompiendo el hielo de "cómo hacer esto"... Mi nombre es Manuel
Kaufmann, quizás más conocido como "humitos". Pertenezco a
`PyAr <http://python.org.ar/pyar/>`__ hace unos años ya y estoy muy
contento de eso. Hoy voy a dar una charla introductoria sobre
`Django <http://djangoproject.com/>`__ ya que me parece una herramienta
muy poderosa, sencilla y *amigable,* entre otras cosas, para los
desarrolladores webs.

La idea de esta charla es hacer un recorrido sobre las funciones básicas
de Django, **creando un proyecto desde cero** y obteniendo como
resultado final un **blog muy simple,** si es que se lo puede llamar
así. Vamos a ver características básicas que se utilizan en todo momento
del desarrollo y quizás que se olvidan con frecuencia.

Charlaremos algunos conceptos teóricos básicos de cómo está construido
Django y porqué es así y luego haremos una parte práctica en dónde
programaremos "juntos" si se quiere un blog muy sencillo con muy poco
código escrito.

|image1|

Django es un `framework <http://es.wikipedia.org/wiki/Framework>`__
pensado para hacer aplicaciones webs. Un framework no es más que un
conjunto de programas, funciones, utilidades y un gran etcétera pensado
para solucionar problemas típicos en el desarrollo de aplicaciones webs.
Digo que está pensado para hacer aplicaciones webs porque también se
pueden usar muchas de sus características para realizar otro tipo de
aplicaciones, como ser de escritorio.

Existen muchos frameworks para desarrollar aplicaciones webs, pero de
los que he probado o visto, este es el que más me ha gustado por su
rapidéz y su simpleza a la hora de programar. Además me ha inspirado a
hacer aplicaciones webs ya que nunca antes había indagado en el tema.

Este framework se utiliza para cualquier tipo de aplicaciones webs,
desde algo muy sencillo hasta algo más complejo. He trabajado en
proyectos extremadamente simples en dónde el usuario simplemente
necesita administrar contenido y que sea visualmente fácil de localizar
hasta una tienda online o un sistema de e-learning dónde se dictan
cursos por internet.

La historia de Django se remonta al año 2003 en dónde la gente que
desarrollaba el sitio para el diario Lawrence Journal World se estaba
dando cuenta que había mucho código que estaban repitiendo, muchas
funciones útiles que necesitaban en otros proyectos y que compartían con
otros sitios. Además, en el desarrollo de nuevos sitios se daban cuenta
que en el otro proyecto más antiguo la clase de problemas que se habían
presentado eran muy similar a los que estaban teniendo actualmente y en
el otro proyecto ya lo tenían resuelto. En pocas palabras, así es como
nació Django: juntaron todo eso que habían desarrollado durante años, lo
pulieron, generalizaron varios aspectos para que sea fácilmente
modificable, charlaron,  se pusieron de acuerdo, eligieron un nombre y
en 2005 lo liberaron como Software Libre.

¿Qué más se puede decir? Desde ese momento no ha parado de crecer y la
comunidad que lo rodea sigue proponiendo ideas, solucionando nuevos
problemas, creando nuevas funciones y utilidades, etc. Es muy activo el
desarrollo de este framework y eso lo hace muy potente y extendible.

|image2|

Django está construido siguiendo el `patrón de diseño
MVC <http://es.wikipedia.org/wiki/Modelo_Vista_Controlador>`__ (Modelo -
Vista - Controlador) que consiste básicamente, en separar y aislar los
componentes de la aplicación. Django cambia un poco el nombre de este
patrón y se llama a sí mismo como MTV (Modelo - Template - Vista),
entonces el mapeo con el clásico patrón sería Modelo-Modelo,
Vista-Template, Controlador-Vista. Por lo tanto, si ya conocen este
patrón de diseño, al principio puede ser un poco confuso.

Los diferentes componentes son:

-  *Modelo*: los datos de la aplicación en cuestión. Es todo lo
   relacionado con la base de datos; la descripción de las tablas se
   realiza en los archivos **models.py** escribiendo código Python.
-  *Template*: está asociado a la interfaz de usuario, es quien dice
   *cómo* se van a mostrar los datos al usuario, cuál va a ser su
   disposición en la pantalla y cuales widgets se van a utilizar para
   cada uno. Esto se hace mediante archivos HTML's con un poco de código
   de template de Django.
-  *Vista:* es la parte encargada de procesar y ordenar los datos
   obtenidos del modelo o bien ingresados por el usuario.

Considerando este ejemplo: "Un usuario ingresa al home del sitio, se le
muestra un formulario en dónde puede dejar sus datos para suscribirse a
las noticias". La interacción entre las diferentes partes queda dada de
esta manera:

-  Al ingresar al home se le presenta al usuario una página que contiene
   el formulario en algún lugar de la misma, esta estructura está
   definida en el *Template.*
-  El usuario ingresa sus datos (nombre y apellido y luego su dirección
   de mail).
-  Estos datos son enviados a la (función) *Vista* que maneja esa
   petición. Es esta vista la encargada de "manipular" estos datos, por
   ejemplo poniendo el nombre y el apellido en mayúsculas y comprobando
   que la dirección de mail sea válida (que contenga una arroba y un
   punto mínimamente).
-  Luego de esta verificación, la *Vista* le informa al *Modelo* que
   puede guardar estos datos en la base de datos ya que son correctos.

|image3|

Una vez que tenemos instalado Django en nuestro sistema (la instalación
`está cubierta en éste
documento <http://docs.djangoproject.com/en/dev/intro/install/>`__)
podemos comenzar un proyecto desde cero. Para eso debemos ejecutar el
programa \ **django-admin.py** e indicarle que queremos crear un
proyecto nuevo mediante el comando  **startproject** seguido del nombre
del proyecto.

*NOTA: no está permitido ponerle cualquier nombre al proyecto; por
ejemplo, no se pueden usar espacios o guiones medios. El nombre del
proyecto tiene que ser un nombre de módulo de Python válido.*

Una vez que tenemos creado el proyecto, podemos ejecutar el *servidor
web de desarrollo* que trae Django consigo. Para esto ingresamos al
directorio que va a tener el mismo nombre del proyecto y ejecutamos el
programa \ **manage.py** con el comando **runserver**. De esta forma le
indicamos a Django que levante el servidor para este proyecto
específicamente.

Debe quedar bien claro que **este servidor es sólo para desarrollo** y
de ninguna manera debe ser utilizado para un sitio que está en
producción ya que no pretende ser utilizado para eso. Lo bueno de este
es que es *muy útil* a la hora de programar el sitio, ya que posee
*auto-reload.* Esto es, cada vez que modificamos un archivo de nuestro
proyecto el servidor se reinicia cargando la nueva configuración. Por lo
tanto, al comenzar el desarrollo lo ejecutamos, luego modificamos los
archivos y lo único que hacemos es presionar F5 en nuestro navegador
para ver los cambios a medida que vamos avanzando o probando nuevas
configuraciones.

Si ahora abrimos un navegador y apuntamos este a la dirección
**http://localhost:8000** vamos a ver un mensaje de bienvenida de Django
indicando que el proyecto funciona correctamente.

Los archivos que nos crea el comando **django-admin.py** son realmente
poquitos a diferencia con otros frameworks y cada uno tiene una función
muy bien definida:

-  *__init__.py*: este archivo no está relacionado con Django
   particularmente, sino que es más específico de Python y le indica que
   el directorio actual es un módulo.
-  *manage.py:*\ es un programa que se utiliza para interactuar con este
   proyecto en particular. Es similar a **django-admin.py** pero
   específico de este proyecto. Mediante este programa se puede
   actualizar la base de datos, ejecutar el servidor de desarrollo,
   correr tests, etc.
-  *settings.py:* en este archivo se encuentra toda la configuración del
   proyecto en general; la conexión a la base de datos, qué tipo de base
   usar, en qué lenguaje está el sitio, etc.
-  *urls.py:* en este archivo se encuentran todas las url's disponibles
   para nuestro sitio.

|image4|

Como dijimos en la diapositiva anterior, Django tiene un archivo llamado
*urls.py* en dónde se encuentra la definición de todas las url's del
proyecto en cuestión. Estas url's están asocian un **nombre** con una
**función vista**\ encargada de procesar la petición web (request). El
nombre está dado mediante una **expresión regular** y prácticamente
puede ser de la forma que más nos guste. La función vista puede ser
asociada mediante una cadena de caracteres indicando el *path* hacia esa
función o bien el objeto función de Python. También se pueden asociar
varias url's hacia la misma vista, esto es muy útil cuando el proyecto
estuvo en producción durante un tiempo y luego se decidió cambiar el
nombre de una url para que sea más legible o algún otro motivo, entonces
podemos hacer que siga funcionando la url vieja (para los usuarios
viejos) y además agregar la nueva url (para los usuarios nuevos).

Puede que nosotros queramos pasar argumentos por la url, por ejemplo si
tenemos un blog quizás la url sea algo similar a
*/año/mes/dia/slug-post*\ por lo tanto vemos que tenemos 4 argumentos
conocidos en el nombre de la url. Para estos casos podemos usar los
grupos de las expresiones regulares para que cada grupo sea pasado como
un argumento posicionales a la vista que va a manejar la petición o sino
podemos utilizar grupos nombrados que van a ser pasados como
argumentos \ *keyword.*

De esta manera tenemos un control absoluto sobre los nombres de las
url's ya que Django nos permite un procesamiento granular de los nombres
gracias a que soporta las expresiones regulares en su definición.
Existen otros frameworks que no nos permiten esta definición de url's
sino que utilizan el nombre de la función o la estructura de los
directorios para dar el nombre a la url, lo cuál no me parece que sea
cómodo a la hora de modificar un nombre o hacer un poco de refactoring
:S

Hemos estado hablando de *Vistas* casi sin hacer ninguna diferencia con
una función de Python y es porque simplemente (casi) no la hay. Una
función vista no es más que una función común de Python que recibe como
primer argumento el **request** (un objeto HttpRequest de Django) y
retorna un **response** (un objeto HttpResponse de Django). Eso es todo,
en el medio la función puede realizar cualquier tipo de operación que
Python lo permita :)

|image5|

Un proyecto no es más que un puñado de aplicaciones de Django, pero ¿qué
es exactamente una aplicación Django?. Bueno, simplemente es un conjunto
de archivo de código fuente de Python agrupados en una carpeta con el
nombre de la aplicación :) .

Lo bueno de esta distinción es que permite compartir una misma
aplicación entre varios proyectos, ya que cada aplicación cuenta con sus
modelos, sus vistas y sus propios templates. Además puede ser que
también utilice modelos de otra aplicación, por lo que para su correcto
funcionamiento deben compartirse ambas aplicaciones.

Por ejemplo, si en algún proyecto *solucionamos un problema*\ o
*agregamos una funcionalidad buena* y queremos que también esté en otro
proyecto, simplemente copiamos la carpeta que contiene la aplicación, la
configuramos en el proyecto y listo.

Todas las aplicaciones que están dentro del mismo proyecto comparten las
configuraciones de éste, por ejemplo el idioma, la conexión a la base de
datos, el **template base** utilizado y muchas otras configuraciones
más.

La forma de crear una nueva aplicación es indicarle esto al programa
**manage.py** del proyecto. Para esto lo ejecutamos con el comando
**startapp**\ y le pasamos el nombre de la aplicación como argumento.
Como resultado, este programa nos crea el directorio con el nombre de la
aplicación que elegimos y dentro de esta tres archivos:

-  *__init__.py:*\ este archivo le indica a Python que este
   directorio es un módulo.
-  *models.py:* en este archivo va la definición de todos los modelos de
   esta aplicación.
-  *views.py:* acá va la definición de todas las vistas de esta
   aplicación.

|image6|

Como charlamos antes, los modelos hacen referencia a la base de datos y
son propios de cada aplicación aunque pueden ser compartido por varias
aplicaciones del mismo proyecto. Por ejemplo, en Django existe un modelo
llamado *User* que es usado por la mayoría de las aplicaciones que
escribimos.

Este framework soporta diferentes "backends" de bases de datos, entre
ellos MySQL, PosgreSQL, SQLite3 y Oracle. También está permitido
extender el framework para soportar otras bases de datos, aunque nunca
lo he necesitado. En este caso vamos a utilizar SQLite3 ya que es muy
sencillo de configurar y es muy útil para desarrollar por su simpleza.

En esta versión de Django está soportado utilizar múltiples bases de
datos y aunque nunca lo he utilizado aprendí a configurar la base de
datos por\ *default*\ del proyecto. Para esto hay que modificar el
diccionario **DATABASES** que se encuentra en el archivo de
configuraciones\ **settings.py**.

El procedimiento para definir modelos en nuestra aplicación es bastante
sencillo. Una vez que tenemos pensadas las tablas que necesitamos en
nuestra base de datos abrimos el archivo **models.py**\ de la aplicación
a la cual le queremos agregar un modelo y definimos la tabla con
sintaxis Python definiendo una nueva clase que hereda de
*django.db.models.Model;*\ asignando un atributo a la clase por cada
columna que queremos en la tabla.

Con esto se puede notar que no es *necesario* saber SQL para poder
definir los modelos, aunque sí recomendable. Pero lo que quiero decir es
que se pueden definir los modelos de la base de datos con un mínimo
conocimiento de SQL.

|image7|

En esta diapositiva estamos definiendo el modelo **Post** que representa
un post en nuestro blog. Las columnas que queremos que tenga esta tabla
son *título, contenido y etiquetas.*\ De la misma forma que en SQL cada
una de las columnas son de un tipo de dato en particular, los atributos
de nuestra clase también. Entonces, necesitamos indicarle a Django qué
tipo de dato es cada uno de sus atributos. Por ejemplo, vemos que el
**título** es un campo de caracteres de longitud máxima de 60, el
**contenido** es campo de texto y las **etiquetas** es una relación
muchos-a-muchos con *Etiqueta* (un modelo que todavía no definimos).

Django automáticamente crea una columna llamada **id** en la tabla de
SQL y es incrementada automáticamente cada vez que se crea una nueva
fila.

Más adelante veremos que Django *sabe* cómo representar cada uno de
estos campos cuando son utilizados en los Templates para mostrárselos al
usuario en la pantalla.

Una vez que tenemos creados nuestros modelos, y si tenemos algún
conocimiento de SQL, podemos preguntarle a Django cuál es el código SQL
que va a ejecutar para crear los modelos que nosotros definimos mediante
clases de Python. Para eso podemos utilizar el comando **manage.py** con
el argumento **sql** seguido del nombre de la aplicación que queremos
ver.

|image8|

Agregamos estos dos nuevos modelos al archivos **models.py** de la
aplicación **posts** que estamos editando recién.

Una vez que tenemos definidos los modelos en la aplicación, podemos
*instalar* esta aplicación en el proyecto actual. Esto sirve para
indicarle a Django qué aplicaciones pertenecen a este proyecto y qué
modelos, vistas y templates están disponibles para este proyecto.

Para esto, editamos el archivo **settings.py** y agregamos nuestra
aplicación a la variable **INSTALLED_APPS**, de esta forma
*'newblog.posts'.*\ Una vez que tenemos nuestra aplicación instalada
podemos correr el comando que mencionamos antes: **manage.py sql posts**
y veremos en la salida estándar el código SQL que Django va a ejecutar
cuando le indiquemos que cree las tablas. En este momento podemos
verificar que sea correcto y de no serlo modificar nuestros modelos para
que lo sea.

Lo que sigue, una vez que vemos que nuestro SQL es el correcto, es
decirle a Django que cree las tablas por nosotros. De la misma forma que
podríamos copiar el código SQL que Django nos mostró y ejecutarlo
nosotros mismos lo puede hacer Django. Entonces le decimos esto con el
comando **manage.py syncdb**.

Este comando busca todas las aplicaciones instaladas (listadas en
**INSTALLED_APPS**) y crea todas las tablas de esas aplicaciones. La
primera vez que ejecutamos **syncdb** Django nos va a preguntar por un
usuario Administrador y su clave, que será un usuario que usaremos más
adelante para administrar algunas cuestiones del proyecto.

|image9|

Como venimos hablando, un proyecto de Django está compuesto por varias
aplicaciones y éstas son reutilizables. Es por esto que Django viene de
fábrica con algunas aplicaciones y mini-frameworks útiles para los
desarrolladores e incluso para el usuario final.

Por ejemplo viene con un framework para manejar comentarios en los
modelos, otro para exportar feeds rss en diferentes formatos, otro para
manejar mensajes temporales a los usuarios, y muchos otros. En este caso
vamos a ver la aplicación **admin** que es utilizada como ABM
(alta-baja-modificación) de los modelos de nuestro proyecto. Incluso
existen algunos sitios que se basan en esta aplicación (modificada) como
la principal del sistema.

Al comienzo dijimos que Django nos simplificaba y resolvía varios
problemas, bueno, este es uno de esos casos. Normalmente mientras uno
está desarrollando es necesario modificar datos o simplemente agregar
datos a la base para hacer algunas pruebas de las funciones. Es acá
donde entra en juego en primera instancia esta aplicación, ya que nos
**facilita mucho** esto por su sencillo uso.

Si estamos haciendo un sistema en dónde es necesario que el usuario
final cargue sus productos en este, se pueden definir todos los modelos
necesarios y luego configurar esta aplicación que trae Django para que
el usuario pueda empezar a cargar sus productos a la base de datos sin
siquiera haber terminado el desarrollo del sistema. Lo cual ahorraría
mucho tiempo.

La aplicación **admin** que viene con Django se instala de la misma
forma que se instala cualquier otra aplicación:

-  se agrega el nombre de la aplicación a la
   variable \ **INSTALLED_APPS**
-  se agrega la url en la cuál queremos que se encuentre esa aplicación
-  se sincronizan los modelos de esta aplicación ejecutando el comando
   **syncdb**

Una vez que tenemos esto hecho, podemos ir a la URL que definimos y
veremos la aplicación **admin** funcionando. Esta aplicación es bastante
grande y permite ser *tunneada* bastante para que cumpla los
requerimientos del usuario o simplemente luzca mejor, es por esto que
probablemente queramos configurar algunas cosas más luego de haberla
instalado para que sea vea como queremos. Entonces, para que se vean los
modelos que hemos definido en nuestras aplicaciones hay que
registrarlos.

|image10|

Las vistas en Django son simples funciones de Python que reciben un
`HttpRequest <http://docs.djangoproject.com/en/dev/ref/request-response/#httprequest-objects>`__
y devuelven un
`HttpResponse <http://docs.djangoproject.com/en/dev/ref/request-response/#httpresponse-objects>`__.
En realidad esto es todo lo necesario a saber para definir una vista de
Django correctamente. Después hay cosas que "habitualmente hacemos" para
manejar el requerimiento del usuario, por ejemplo, si este ha ingresado
datos hacemos una diferencia entre el método **GET** y **POST**, una vez
que tenemos los datos que el usuario ingresó, los validamos y luego los
guardamos en la base de datos. Por el contrario la primera vez que se le
muestra el formulario al usuario será mediante un GET, entonces en este
caso lo que hacemos es renderizar el formulario en el template
correspondiente.

Entonces, lo más común es que cada vista tenga al menos dos caminos: uno
para el GET y otro para el POST separados por un **if**\ y en cada caso
se retornará lo que corresponda o se lo redirigirá al usuario a otra
URL. También se puede renderizar el mismo template en ambos casos pero
con diferentes valores en sus variables.

El workflow habitual para definir una *vista* consiste en importar los
módulos que se utilizarán en esta vista, por ejemplo
﻿\ *render_to_response, PIL,*\ etc\ *.* Luego se define una función
Python con el primer argumento con el nombre ***request* y luego los
demás argumentos que vienen por la URL (ya sean como grupos nombrados o
no). Seguido de esto se escribe el cuerpo de la función como antes
comentamos y finalmente se edita el archivo *urls.py*\ mapeando una url
a la nueva vista que acabamos de definir.**

**|image11|**

**En este ejemplo se ve claramente lo que acabamos de explicar. Las
primeras tres líneas importan las funciones, modelos y formularios
necesarios para definir la vista. Luego se define la vista llamando al
primer y único argumento *request*\ y en el cuerpo de la vista se maneja
el método GET y el POST.**

**Para el método GET lo que se hace es crear un formulario para el
modelo Post** y luego se lo renderiza en el template
*agregar_post.html* de la aplicación **Post**.

Cuando la petición web es un POST se crea un un **nuevo formulario** a
partir de los datos enviados por el usuario (mediante el POST), luego se
pregunta si es válido. Si lo es, se guarda en la base de datos este
formulario, creando un nuevo objeto del modelo Post y con esto una nueva
fila en la tabla Post del SQL. Una vez que se hace esto se redirige al
usuario al home (root) de nuestro sitio web (/) mediante el código de
respuesta **302.**

**|image12|**

En el ejemplo anterior hablamos de *renderizar un template,* pero hasta
ahora no vimos como lucen estos y tampoco cómo escribirlos. Los
templates no son mucho más que código HTML y un poco de código **Django
Template**. Si tenemos un poco de conocimiento sobre HTML y un poco de
conocimiento estructuras de flujos nos va a resultar muy sencillo
escribir los templates que Django luego va a renderizar.

Existen tres grandes conceptos en el código Django Template, los
filtros, las variables y las etiquetas. Las variables son justamente
eso: variables, las cuales contienen un valor que puede ser insertado en
cualquier lugar del template encerrando su nombre entre dos llaves ({{
variable }}). De esta forma, en el lugar que ingresemos esa sustitución
se pondrá el contenido de la variable en ese lugar.

Las etiquetas se utilizan para organizar el flujo del programa y así
mostrar los datos correspondientes en cada caso. Algunas
etiquetas comúnmente usadas son if, for, trans, blocktrans, comment,
etc. Estas se encierran entre llaves simples y un signo de porcentaje
({% comment %}).

Otra gran característica de los templates es la **herencia.**
Normalmente se utiliza para no repetir código y que sea más fácil de
mantener. Los sitios habitualmente tienen un header y footer estático,
que no cambian al navegar el sitio: este puede ser un menú en el header
y algún texto que diga "Copyright Humitos ©" o similar en el footer.
Entonces, para estos casos en los cuales yo quiero tener dos porciones
de mi página que sé que no van a cambiar en todo el sitio puedo escribir
esto en un template **base** e indicar cuáles son las partes de este
template que se pueden cambiar. Luego en otro template, **el que hereda
de base**, defino cuales son los bloques del template que estoy
heredando que deseo cambiar y así sólo modifico el contenido relevante y
la porción del sitio que se repite en todos los templates me queda
centralizado en un sólo archivo.

|image13|

En la variable **TEMPLATE_DIRS** del archivo **settings.py** están
listados los directorios en los cuales Django debe buscar los templates
que las vistas van a usar para renderizar su contenido. Por lo tanto,
debemos agregar los directorios dónde vamos a tener nuestros templates a
esta variable.

Además, existe una notación específica para ubicar los templates dentro
de cada aplicación y que sean encontrados *automáticamente*\ por Django
sin tener que agregar cada uno de los directorios de nuestras
aplicaciones. Esta notación es
﻿\ *<app_name>/templates/<app_name>/template.html.*\ Por ejemplo para
el template *agregar_post.html* que usamos anteriormente en la vista la
ruta parados desde el **root del proyecto** sería:
*posts/templates/posts/agregar_post.html*

Los filtros se aplican a las variables y se utilizan
para \ **modificar** el valor que esta contiene o bien darle formato.
Por ejemplo si en la variable tenemos una fecha y la queremos mostrar
como\ *dd/mm/aaaa* se puede usar el filtro \ **date.**\ La forma de
utilización es similar a la de la sustitución de la variable pero
seguido del nombre va un pipe y luego el nombre del filtro. Por ejemplo,
para pasar el contenido a minúsculas se puede usar el filtro \ *lower:*
{{ variable\|lower }}.

Otra de las cosas que me gusta de Django es lo simple y fácil que es
extenderlo. Me ha pasado varias veces que necesito hacer un filtro o un
templatetag y me he sorprendido lo fácil que es escribir uno propio.
También con esto hay que *tener cuidado* ya que lo que se puede hacer en
un filtro o un templatetag es bastante poderoso, pero en realidad, éstos
no están pensados para tener mucha lógica, sino más bien están pensado
para hacer alguna mínima modificación en la estructura o en el valor de
la variable. La lógica compleja sobre qué datos o cómo se deben mostrar
debería estar en la vista y no en el template.

|image14|

¿Preguntas? Usen los comentarios para hacerlas, las contestaré a medida
que pueda :)

|image15|

Algunos links de referencia:

-  http://www.djangoproject.com/
-  http://docs.djangoproject.com/en/1.2/
-  http://django.es/
-  http://django.es/docs/intro/general/
-  http://django.es/docs/intro/tutorial01/
-  http://trac.usla.org.ar/django-book

.. |image0| image:: http://humitos.files.wordpress.com/2010/09/img0.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img0.jpg
.. |image1| image:: http://humitos.files.wordpress.com/2010/09/img1.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img1.jpg
.. |image2| image:: http://humitos.files.wordpress.com/2010/09/img2.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img2.jpg
.. |image3| image:: http://humitos.files.wordpress.com/2010/09/img3.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img3.jpg
.. |image4| image:: http://humitos.files.wordpress.com/2010/09/img4.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img4.jpg
.. |image5| image:: http://humitos.files.wordpress.com/2010/09/img5.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img5.jpg
.. |image6| image:: http://humitos.files.wordpress.com/2010/09/img6.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img6.jpg
.. |image7| image:: http://humitos.files.wordpress.com/2010/09/img7.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img7.jpg
.. |image8| image:: http://humitos.files.wordpress.com/2010/09/img8.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img8.jpg
.. |image9| image:: http://humitos.files.wordpress.com/2010/09/img9.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img9.jpg
.. |image10| image:: http://humitos.files.wordpress.com/2010/09/img10.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img10.jpg
.. |image11| image:: http://humitos.files.wordpress.com/2010/09/img11.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img11.jpg
.. |image12| image:: http://humitos.files.wordpress.com/2010/09/img12.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img12.jpg
.. |image13| image:: http://humitos.files.wordpress.com/2010/09/img13.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img13.jpg
.. |image14| image:: http://humitos.files.wordpress.com/2010/09/img14.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img14.jpg
.. |image15| image:: http://humitos.files.wordpress.com/2010/09/img15.jpg?w=300
   :target: http://humitos.files.wordpress.com/2010/09/img15.jpg
