.. link:
.. description:
.. tags: general, hosting, kde, python
.. date: 2007/12/20 20:46:26
.. title: Resumiendo días
.. slug: resumiendo-dias


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/12/20/resumiendo-dias/


Ultimamente no tengo tiempo para nada, asique no me estaba sentando a
escribir algún que otro post sobre qué estoy haciendo, o investigando.
Esto se debe a que estuve rindiendo una materia de la facultad, dando
clases particulares de Python a unos chichos de secundaria, trabajando
para Diego (un amigo), peleando con la generación de **códigos de
barras** y demás.

**Konqueror**

Hace un tiempo me dí cuenta que además de no ser compatible con Gmail,
este maravilloso navegador, gestor de archivos y demás, tampoco es
compatible con Wordpress en su totalidad. No me deja escribir / editar
mis post de la forma "What you see is what you get" (Lo que ves es lo
que es obtienes -creo que se dice así-), como a los post los venía
escribiendo con el Kate y
`reStructuredText <http://docutils.sourceforge.net/rst.html>`__ a esto
no lo había notado.

**Swiftfox**

Hace un par de días se me actualizó el Swiftfox a la versión 3.0b3pre;
con lo que noté que anda un *poco*\ más rápido que antes y
**dicen**\ que consume menos memoria RAM que antes. A decir verdad, no
sé cuanto consumía antes, sé que era mucha, pero no recuerdo cuanto...
Ahora lo tengo con 6 solapas abiertas y consume algo así como 71124
kBytes. No me parece poco.

También noté, que puedo pegar con el botón del medio del mouse (como en
cualquier aplicación de linux) lo que tengo en el portapapeles de la
última selección en la ventana de edición del post. Esto antes no se
podía porque aparecía las flechitas de scroll.

Otra cosa, todos los plugins que tenía instalados no son compatibles con
esta nueva versión, incluso quise instalar el diccionario Spanish
(Argentina) y me dijo que no es compatible con esta versión. Lo cual es
bastante malo.

Está bien, estoy de acuerdo con que todavía no es la versión final,
pero... ¿Porqué Swiftfox se me actualizó a una versión que\ *no es la
final y tiene algunos problemas?*

**Código de barras**

Para el trabajo que estoy haciendo con Diego, necesitábamos de alguna
manera generar el código de barra de los productos del negocio. Buscando
en Google, preguntando en la lista de PyAr y por otros lados también,
caí en una
`receta <http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/426069>`__
de Python la cuál genera el código EAN que queramos. Este tiene algunas
limitaciones a mi entender: no puedo generar códigos con letras y como
necesitaba esto, lo descarté. Igualmente me fijé como estaba hecho.
Levantaba una letra que tenía internamente codificada y luego utilizaba
PIL (Python Image Library) para generar un .gif con el código.

Funciona muy bien. Otra restricción que tiene es que el código
**debe**\ ser de 12 digitos, o 13 si este trae el bit de comprobación,
el cuál mediante un algoritmo indica si el código está bien formado o
no. Y como los códigos que necesitaba era de una cantidad variable de
dígitos tampoco me servía...

Preguntando **bastante** en la lista de PyAr (se deben acordar de
algunos familiares míos :) ) logré hacer el código que realmente
necesitaba: escribir cualquier cantidad de caracteres y de cualquier
tipo y obtener un código de barra. Lo que hice está **muy** orientado
por Facundo quién me pasó un ejemplo de cómo usar la `Font libre de
Code39 <http://www.squaregear.net/fonts/free3of9.shtml>`__ con PIL, que
no tenía mucha idea.

Probando, investigando, reinventando un poco la rueda, peleando con el
lector de códigos de barras (que no me quizo agarrar el teclado y el
lector al mismo tiempo) `llegué a la versión del código que
funciona <http://grulicueva.homelinux.net/~humitos/blog/resumiendo-dias/barras.py>`__.
Esto es, al programa le paso el código que quiero que genere y me guarda
en el directorio actual un PNG con ese código. Ejemplo de uso:

::

    [manuel] [~]$ python barras.py "*ABC123*"

    *ABC123*

    [manuel] [~]$

Ahora en \*ABC123\*.png tengo el código listo para imprimir. También
hice que abajo del código de barras aparezca de forma legible para los
humanos el código por si el lector no lo lee. Para esto utilicé una
fuente cualquiera, que después cambiaré por una un poco más linda.

**Curso de Python**

Ayer miércoles, fue la tercer clase que tube con los chicos del curso de
Python. Yo les había dado una guía de ejercicios para que hagan en sus
casas y un trabajo práctico también. Hacía una semana más o menos que no
los veía, y no hicieron casi nada. Sólo 5 ejercicios. Asique les pedí
que me expliquen cómo lo habían hecho a algunos y cuales eran las dudas
que tenían con respecto a los que no puedieron hacer. La verdad que la
hora se pasó volando y alcanzamos a hacer bastante poco, por lo que les
dije que si querían se podían quedar un poco más haciendo los ejercicios
que les había dado y yo mientras programaba un poco

Me hicieron algunas preguntas, y como estábamos en horario fuera de la
clase, los obligué a buscar en Google y a preguntar en el canal de PyAr
:D .Entraron, saludaron, preguntaron, y me dijeron que había muy buena
onda en ese lugar y que sabían una cantidad los que estában ahí. Espero
que se **copen** con Python y sigan estudiando, que les halla servido lo
que intenté enseñarles y aprueben la materia.

**Facultad**

El martes pasado rendí por segunda vez **Sistemas y Organizaciones**,
una materia de primer año de mi facultad. Con la cual tuve problemas
durante los cuatro años que hace que estoy estudiando. Aunque esa
materia es una lotería, y a decir verdad, no importa cuanto sepas, sino
si pegás un examen en el cual estén un poco menos soretes. El exámen es
multiplechoice, son 50 preguntas, las que contestás mal restan, y
algunas otras cositas más.

Cuando me dijeron que era multiplechoice, casi que me quedé tranquilo,
porque no podía ser muy complicado. Pero bueno, el tema es que no es
difícil el exámen, tenés que estar **bien** concentrado y no dejar
llevarte por lo que está en lo que vos estudiaste y sabés que es así.
Sino que tenés que pensar como piensan ellos, ponerte en el lado de
ellos, pensar como el profesor: "La respuesta verdadera para esta
pregunta es la b), pero la **mas-verdadera** es la d)"; entonces tenés
que poner la d).

¿Cómo puede ser esto? No sé, pero en casi todas las respuestas hay dos
que son verdaderas, según ellos hay una que es más verdadera. Bueno, eso
me dijeron al menos hace dos semanas, la primera vez que la rendía y
saqué un 2 con 32 correctas, sobre 35 que se necesita para aprobar. Osea
tenía un 64% aprobado del exámen, pero esta matería única en la facultad
y en su género se aprueba con 70%.

La segunda vez que la rendí se puede decir que **entendí** este concepto
de **mas-verdadera**. Si te fijás bien en cada una de las respuestas hay
dos que son verdaderas, pero hay una que está un poco más completa la
respuesta. Igualmente dicen el concepto de formas totalmente diferentes,
y en muchas preguntas me hubiese gustado tener un diccionario ahí.

Además juegan con los nervios de uno porque hacen una pregunta o
afirmación y ponen "marque la *correcta*" o "marque la *incorrecta*".
Imaginate a la pregunta número 40, pensando cuál es la más verdadera y
que sé yo que otra cosa (esas cosas que uno piensa cuando está un final:
"Que lindo sería estar en casa con el aire"), sinceramente llega un
punto en el que te confunden. Encima también juegan con la doble
negación, un ejemplo sencillo de esto: "¿Cuáles de los siguientes
conjuntos de partes no es un sistema? (indique lo *incorrecto*)". Más de
uno caemos en estas trampas...

**Cumpleaños**

Ayer fue mi cumpleaños, aunque no parezca tengo 22 añitos recién. Si ya
sé, estoy de vuelta, pero bueno algún día tendré plata y me pondré botox
:) . El sábado no juntamos en mi casa con algunos amigos y amigas a
comer unas hamburguesas y tomar algo, después salimos. A ver que tal se
pone esto; el año pasado me llovió de una forma increible.

Hoy es el cumple de Juanjo, un amigo de la facultad, al cual ya estoy
llegando tarde... Asique me voy para allá.
