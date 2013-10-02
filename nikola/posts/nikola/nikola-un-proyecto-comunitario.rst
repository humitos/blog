.. link: 
.. description: 
.. tags: nikola, blog, software libre, python
.. date: 2013/09/20 19:54:20
.. title: Nikola, un proyecto comunitario
.. slug: nikola-un-proyecto-comunitario


Como todos saben, y los que no se están enterando ahora, `migré mi blog`_ de
wordpress.com a mi servidor personal pero además no estoy usando más wordpress
para gestionarlo, sino que estoy usando Nikola_.

Nikola me gusta, porque además que puedo escribir usando reStructuredText, es
Software Libre y está hecho en Python. Y eso quiere decir que, además de que
puedo modificarlo y agregarle nuevas funciones o corregir errores, sé como
hacerlo. O bueno, eso creía...

La historia ya me ha visto trabajar con reStructuredText, pero nunca hice nada
en serio. Digo, no "en serio", sino enserio. O sea, hablando en serio, nunca
hice nada con él más que usarlo. Hace unos años atrás, cuando trabajaba en
Machinalis_ uno de los proyectos en los que participé era sobre la
documentación de un software que chequeaba unos reactores nucleares. Sí, suena
como super mega increíble, pero lo único que hice yo fue migrar la
documentación de ese software que creo que estaba en Microsoft Word a Sphinx
(que usa reStructuredText). En esa migración tuve unos cuántos problemas con
reStructuredText y que la mayoría de ellos se solucionaban extendiendo
reStructuredText. Digamos, agregando algunas cositas extras mediante algunas
líneas de programación en Python.

Recuerdo que por esos tiempos me partí la cabeza para entender cómo se hacía
para extender reStructuredText y encima que Sphinx se dé cuenta que vos querés
la versión extendida y no la que viene con él. Me acuerdo que me volví loco
para hacer que toda esa cosa funcione, el proyecto estaba interesante y yo lo
quería hacer perfecto, pero el cerebrito que me dieron no cubría con todo lo
que necesitaba hacer (o al menos lo que me hubiese gustado hacer). Asique, no
recuerdo muy bien cómo terminé solucionando las cosas...

Años después, trabajé en la traducción de "`La Confusión de la Tortuga`_" con
Melina y otra vez usamos reStructuredText para hacer el libro. Además, luego
para hacer la versión final en PDF utilizamos una herramienta llamada rst2pdf_,
que "Oh!, casualidad" es del mismo autor_ que Nikola y que "Oh!, mirá vos"
también usa reStructuredText como texto de entrada. Con ese libro tuve varios
problemas con las imágenes, con algunos márgenes y demases que reporté al autor
y siempre me tiró la de "Abrime un issue y yo lo miro esta noche", o "Fijate en
tal archivo que está lo que necesitás cambiar" y yo como buen lazy (y teniendo
en cuenta mi experiencia de extender reStructuredText) siempre tenía unas horas
para esperar a "esta noche". Así, pasado unos días si no tenía noticias de él
lo pingeaba y finalmente tenía mi bug arreglado :)

Esta vez, el "problema" que tenía era que no había forma de linkear un blogpost
con otro dentro de mi blog sin tener que poner la URL completa y yo sabía, por
la traducción del Tutorial de Python, entre otros, que había un rol llamado
`:ref:` que podía servirme para hacer lo que yo quería hacer. Así que, pasó
algo similar que con rst2pdf_ pero con la diferencia que, luego de haber leído
`su blogpost sobre su postura en el proyecto`_, me quise dar un poco más de
maña y vencer esa barrera que había tenido durante este tiempo y finalmente
aprender a extender reStructuredText. Así que, pregunté *qué*, *cómo* y *dónde*
tenía que modificar para poder agregar esa nueva característica a Nikola y que
todos puedan disfrutar de ella.

Mejor que cualquier profesor de cualquier Universidad (no me consta, no fui a
todas), Roberto me tiró las mil y una data sobre cómo hacer lo que yo quería
hacer. El 1, 2, 3 o el A, B, C de cómo hacer lo que yo quería en lenguaje
natural como para que lo entienda cualquier idiota, seguido de unos "fijate
acá" y "fijate allá como lo hizo éste". Así que con toda esa información, me
puse manos a la obra y le dije que en 32hs lo iba a tener terminado. Utilicé
1_, 2_, 3_, 4_, 5_, como referencia para terminar de entender y robé algunas
cosas de esos lugares también.

A medida que estaba laburando, Roberto me dice que me dió permiso de commit en
el repositorio oficial de Nikola, seguido de un "no hagas cagadas nomás", y
luego de tener andando en mi máquina el rol que quería agregar, hice unos
tests, actualicé la documentación, agregué eso al changelog y demás (todo como
corresponde, ¿no?) y "Bueh, ya fue, lo mando". Y así fue como lo mandé al
*master* de una...

Unos minutos después, me entero que había una serie de pasos un poco más
amigables con el entorno que estaban usando, el sistema de chequeo para que
cada commit pase los tests antes de ser aprobado en *master* y que básicamente
me había mandado un *mocaso*. Ahí salió Roberto a decirme: "No te preocupés,
hacé... Nah, dejá. Yo lo arreglo. Si vos supieras los mocos que me mandé yo no
me hablarías más". Así, un rato más tarde ya tenía unas instrucciones_
completísimas sobre cómo hacer para colaborar correctamente con Nikola, sin
mandarse ningún moco y sin hacer que todo explote, que igualmente, cuando lo
hacés explotar te siguen tratando bien y todo :)

Así que, con ustedes, `el nuevo rol reStructuredText para Nikola`_ `:doc:`,
que sirve para linkear un blogpost con otro dentro de un mismo sitio. Este
feature va a ser agregado en la próxima release de Nikola que incluya features.

La verdad que los que laburan en Nikola tienen mucha y muy buena onda con los
que quieren colaborar por más noob que sean. Varias veces me sentí medio
boludo, pero hicieron que eso no se agrave al ayudarme a resolver los problemas
que tenía y que había cometido. Yo creo, que si bien esa es la idea, también
hay que tener ganas de hacerlo todo el tiempo, y estos dos días que estuve
laburando en Nikola, los pibes me tiraron la mejor onda en todo momento.

¡Mis felicitaciones a ellos!

.. _1: http://docutils.sourceforge.net/docs/howto/rst-directives.html
.. _2: http://doughellmann.com/2010/05/defining-custom-roles-in-sphinx.html
.. _3: https://github.com/qsnake/docutils/blob/master/docutils/parsers/rst/roles.py
.. _4: http://docutils.sourceforge.net/docs/ref/rst/roles.html
.. _5: https://github.com/qsnake/docutils/blob/master/docutils/parsers/rst/directives/references.py
.. _Nikola: http://getnikola.com
.. _Machinalis: http://machinalis.com
.. _migré mi blog: http://blog.mkaufmann.com.ar/posts/migrando-a-nikola/
.. _la confusión de la tortuga: http://blog.mkaufmann.com.ar/posts/wordpress/la-confusion-de-la-tortuga/
.. _autor: http://ralsina.me/weblog/index.html
.. _rst2pdf: http://rst2pdf.ralsina.com.ar/
.. _su blogpost sobre su postura en el proyecto: http://ralsina.me/weblog/posts/being-an-inclusive-project-and-how-github-saved-my-day.html
.. _instrucciones: https://github.com/getnikola/nikola/blob/refrole/CONTRIBUTING.rst
.. _el nuevo rol reStructuredText para Nikola: https://github.com/getnikola/nikola/pull/730

