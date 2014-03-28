.. link:
.. description:
.. tags: blog, internet, kde, software libre, ubuntu
.. date: 2007/11/23 21:15:23
.. title: ¿Un escritorio? KDE. - Primera parte: Konqueror
.. slug: un-escrtorio-kde-primera-parte-konqueror


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/11/23/un-escrtorio-kde-primera-parte-konqueror/


|konqueror|

Sin dudarlo esa es mi respuesta. Hace algunas semanas, quizás un mes, no
tengo idea. Instalé Ubuntu en mi otra pc por medio de la red. Le puse
esta distro de linux (con GNOME) ya que la pobre tiene algunos
*problemas serios* y es un poco lenta.

No viene mucho al caso tampoco. El punto importante en esto es que traté
varias veces de utilizar este entorno desde la otra pc, pero no pude
adaptarme todavía. GNOME tiene muchas cosas que no me gustan, y algunas
pocas que sí. Me siento mucho más cómodo con KDE por varios motivos.

Cuando quise configurar la pc con Ubuntu, no me quedaba otra que usar
GNOME, además esa era la idea. Varias veces intenté cambiarme, no sé
bien porqué, supongo que por una cuestión de rendimiendo. Hay muchos que
dicen que KDE es mucho más pesado que GNOME, quizás sea verdad.

Lo primero que noté, es que la mayoría de los diálogos de GNOME no
tienen el botón cancelar, como para deshacer los cambios. Un ejemplo
concreto. Si hacemos botón derecho en el escritorio (esto es bien
Windows) como para cambiar el fondo de pantalla del escritorio (no digo
el camino correcto porque no lo sé). Elegimos uno, al azar, que sé yo, y
si luego queríamos dejar la opción como estaba, no podemos, ya que de la
única forma que podemos salir es aceptando.

Esto lo confirmo cuando en mi máquina con KDE instalo el programa Día
(para hacer diagramas), en el que noté exactamente los mismo. No lo
estoy cuestionando, ni diciendo si esto es mejor o peor. Gustos son
gustos. A mí particularme esto por ejemplo no me gusta.

En estos últimos días aprendí muchas cosas sobre
`Konqueror <http://www.konqueror.org/>`__, el navegador web, explorador
de archivos, lector de páginas de manuales, y un gigante etcétera, por
defecto del KDE. Estuvimos con **leo_rockway**, un flaco que conocí en
el canal de irc de ubuntu argentina (#ubuntu-ar en freenode.net) y
además un beta tester oficial de todos mis programas :P .

"El que busca siempre encuentra", dicen. Hace un tiempo, yo le había
comentado a Leo que quería usar los bookmarks de
`del.icio.us <http://del.icio.us/>`__ en el Konqueror y no podía. Esto
era uno de los motivos por los cuales no dejaba el
`Swiftfox <http://getswiftfox.com/>`__.

Pasó un largo tiempo, instalé miles de plugins para el Swiftfox, y
encima me acostumbré a ellos, mouse gestures, diccionario español para
la corrección ortográfico y demás. Después de este tiempo y un poco más,
recibo un mail de Leo que decía que había encontrado un
`plugin <http://www.kde-apps.org/content/show.php?content=18909>`__ para
el Konqueror que era para los bookmarks de del.icio.us. Lo probé, pero
no me funcionó, tampoco le dí mucha bola porque además tenía los mouse
gestures y *sabía* que el Konqueror eso no lo tenía, asique fue.

Sigió pasando el tiempo, y cada vez necesitaba hacer más y más cosas. Y
siempre le volvía a dar una oportunidad más al Konqueror (de hecho, me
gusta mucho más que cualquier otro navegador, por eso seguía
insistiendo) porque descubría cosas nuevas. En este momento descubrí que
presionando la tecla Control, Konqueror `te muestra sobre los links unas
letras <http://grulicueva.homelinux.net/~humitos/blog/un-escritorio-kde/konqueror_shortcuts.png>`__
y presionando una de las letras que muestra se hace "click" en ese
hipervínculo. Buenísimo, a veces no queremos usar el mouse y esto para
esos casos viene *petacular*!

Seguía pasando el tiempo, y yo al Konqueror no le daba bola, aunque le
seguía encontrando cosas que lo hacían cada vez mejor. ¡Yo quería mis
bookmarks y mis mouse gestures! Leyendo el blog de
`nercof <http://gheize.wordpress.com>`__, en un artículo que nada que
ver con el Konqueror, él usa GNOME y Firefox, asique ni mú. *Descubrí*
que presionando **Control+Shift+Arriba**\ o **Abajo**\ empieza a
desplazarse automáticamente muy sutilmente para la dirección que
presionamos. Si presionamos nuevamente aumenta la velocidad. Puede ser
útil para leer un texto largo, a una velocidad relativamente baja. Yo no
me acostrumbré todavía, pero lo probé y está bueno.

Tampoco hizo que me cambie de navegador, pero al menos me hizo darle
otra oportunidad y saber que siempre estaba ahí mi navegador
esperándome.

Desde que tengo hosting en el servidor nuevo, necesito acceder varias
veces por **ssh**. A esto lo hacía por medio de una consola o con el
`mc <http://www.ibiblio.org/mc/>`__. Pero para copiar ficheros era
bastante embolante usar la consola asique me manejaba con el mc para
esto.

Un día en el canal de PyAr *escucho* que StyXman menciona algo así como
¿Humitos estás conectado con el Konqueror por **fish**? A lo que
respondí que no, que estaba usando el mc. Osea, ni idea de lo que me
estaba hablando. Leí algo y ví que se podía acceder del mismo estilo que
el mc pero con el Konqueror. Instalando un paquete (*kfish* en Ubuntu),
poniendo en la barra de direcciones:

::


    fish://usuario@host/carpeta/a/acceder

Podemos ver en el Konqueror los archivos que están en esa máquina como
si estuvieran en la nuestra, y así poder utilizar cualquier programa que
tengamos instalado en nuestra máquina con los archivos que se encuentran
en la otra. Por ejemplo el `Kate <http://kate-editor.org/>`__, ya **no
más** Vim :) .

Además me hice un bookmark de esto, así no tengo que escribir más la
dirección de la máquina a las que quiero acceder. Por lo que esto me
hizo dejar otra vez el Vim, como así también el mc.

Otra cosa, si pongo un cd de audio y lo exploro con el Konqueror, se
pueden ver muchas carpetas, con los nombres: Ogg, Mp3, Wav, etc... Cada
una contiene todos los temas del disco en el formato especificado por la
carpeta. Osea arrastrando esa carpeta a una de nuestro disco, el
Konqueror automágicamente nos convierte los temas al formato
especificado. ¡Genial!

También se pueden leer los man pages de los comandos desde el Konqueror
poniendo en la barra de direcciones este comando. Con las comodidaes que
esto trae, como agrandar la letra, y verlo con un formato un poco más
amigable que desde la consola:

::


    man:/comando

¿Ya está? No para nada. El Konqueror tiene mucho más. Si quiero pedirle
la ayuda de un programa, hago:

::


    help:/programa

Se pueden habilitar los "Accesos rápidos para web" desde las
configuraciones del Konqueror, para por ejemplo buscar un montón de
cosas en la web. Algunos ejemplos pueden ser, poniendo *gg:humitos*,
busco humitos en Google, *qt3:qtimer* busca qtimer en la documentación
de Qt, *en2es:hello* busca hello en wordreference... ¿Qué más querés?

Y por último, creo que solo porque me cansé de escribir, y no porque
Konqueror termine acá. Mi amigaso leo_rockway hoy me comentó que pudo
hacer funcionar los mouse gestures en Konqueror. Incluso este los trae
por defecto, no es un plugins aparte ni nada, pero no vienen activados.
Para activarlos hay que ir a **kcontrol**, luego *regional y
accesibilidad*, *introducir acciones*, *preferencias generales*,
*importar nuevas acciones* y colocar la dirección:

::


    /usr/share/apps/khotkeys/konqueror_gestures_kde321.khotkeys

¡LISTO! Tengo los gestures que tanto estaba buscando, y además
certificado por
`**leo_rockway** <http://grulicueva.homelinux.net/~humitos/blog/un-escritorio-kde/certificado_leorockway.png>`__.
También tiene sesiones este navegador, está integrado con el gestor de
descargas KGet, tiene soporte para la cartera de KDE, y miles cosas más.

Obviamente, también tiene cosas malas, pero muy pocas. Yo hasta el
momento le encontré sólo una: No funciona del todo bien Gmail, me marca
como que tiene errores la página, el navegador. Otra cosa que no me
gusta, no digo que sea mala esta, pero a mí no me gusta. El plugin que
hasta el momento encontré para del.icio.us, no me gusta para ná.

¿Todavía no usás Konqueror? ¿Qué esperás?

PD: Este post lo escribí de una forma rara, pero **muy** cómoda:
`reStructuredText <http://docutils.sourceforge.net/rst.html>`__, es
simple, fácil, rápido.. :D

.. |konqueror| image:: http://www.guia-ubuntu.org/images/d/dc/Konqueror.png
