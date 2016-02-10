.. title: Hotkeys for the win
.. slug: hotkeys-for-the-win
.. date: 2016-02-08 19:13:07 UTC-03:00
.. tags: perú, hotkeys, xubuntu, las lomas
.. category: 
.. link: 
.. description: 
.. type: text

¿Cuántas aplicaciones utilizás en el día a día? Digamos que nos
limitamos a *las más comúnes* únicamente. En ese caso, mi respuesta
sería: 6 (emacs, firefox, terminator, pidgin, thunar y thunderbird)

Esas aplicaciones las tengo abiertas casi todo el día. Además, a
medida que voy trabajando comienzo a abrir otras: Google Chrome,
LibreOffice, JOSM, gThumb, inkscape, Skype y algunas más. A mitad de
la tarde, ¿cuántas aplicaciones tenés abiertas? Y lo más importante:
¿cuántas veces hiciste Alt + TAB? Aunque lo peor de todo es: ¿cuántas
veces hiciste Alt + TAB y *te pasaste* por una ventana y diste toda la
vuelta hasta la correcta o bien, te fracturaste un dedo haciendo Alt +
Shift + TAB para volver una selección?

Bueno, hace varios años que yo me cansé de eso y decidí buscar una
solución. La solución vino exactamente con la primera pregunta que te
hice: *¿cuántas aplicaciones utilizás en el día a día?*. Básicamente
quería poder acceder a cualquiera de esas 6 aplicaciones sin que
importara en qué orden las había abierto o había estando navegando por
ellas. Digamos, que si fui a firefox, luego a pidgin y luego a
thunderbird; quería poder saltar en un solo hotkey a terminator -que
si usamos Alt + TAB tendríamos que presionarlo 3 veces consecutivas.

Primero me puse a investigar cómo se puede hacer para cambiar de
ventanas utilizando la línea de comandos. Ahí llegué a wmctrl_, que te
permite listar las ventanas activas y también cambiar entre cada una
de ellas mediante una interfaz de línea de comandos.

.. TEASER_END

.. code::

   $ wmctrl -l -x
   0x01600003  0 Thunar.Thunar         victoria humitos - Administrador de archivos
   0x040000a3  0 emacs.Emacs           victoria emacs-victoria: ~/bin/change-window [-]
   0x024000ab  0 Navigator.Firefox     victoria Inbox (0) - someone@gmail.com - Gmail - Mozilla Firefox
   0x04200db8  0 Pidgin.Pidgin         victoria (someone@gmail.com)
   0x0420006a  0 Pidgin.Pidgin         victoria Lista de amigos
   0x03e00001  0 Google-chrome.Google-chrome  victoria Nueva pestana - Google Chrome

Ahora bien, con esa información de WINDOW_ID, NAME y WINDOW_TITLE ya
puedo cambiar de una ventana a la otra utilizando su WINDOW_ID
así -por ejemplo para ir a la lista de amigos de Pidgin:

.. code::

   $ wmctrl -i -a 0x0420006a

Ahora necesitaba presionar un hotkey y que *ejecute algo* que parsee
esa salida y cambie a la ventana que quiero utilizando wmctrl_. La
ventana que "quiero" dependerá del hotkey presionado.

Entonces, ¡escribí un script en Python, por supuesto!

.. listing:: listings/hotkeys-for-the-win/change-window python
   
Básicamente hace eso que dijimos. Sin embargo, le agregué una cosita
más. A veces pasa que tengo abierta la "Lista de amigos" y una
"Ventana de conversación" en Pidgin y necesitaba poder decirle que
vaya a la ventana de conversación de alguna forma. Esto es porque
cuando estás chateando con alguien querés poder presionar el hotkey,
contestarle, presionar el hotkey del emacs y seguir codeando; sin
necesidad de pasar por la lista de amigos. Entonces, hace eso: si hay
una ventana con "Lista de amigos" en su WINDOW_TITLE, elije la otra
que sea de Pidgin :)

.. admonition:: Nota

   No te olvides de asignarle permisos de ejecución a tu programa python con:

   .. code:: bash

      chmod +x change-window

Perfecto, lo único que queda es decirle a nuestro entorno gráfico que
cuando presionemos nuestro *hotkey maravilla* ejecute nuestro
programa. Yo uso xfce_ por lo tanto, tengo que modificar el archivo
xml de mi directorio personal
`~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml`
y agregar estas líneas en la sección `<property name="custom"
type="empty">`:

.. code:: xml

   <property name="&lt;Super&gt;t" type="string" value="/home/humitos/bin/change-window terminator"/>
   <property name="&lt;Super&gt;e" type="string" value="/home/humitos/bin/change-window emacs"/>
   <property name="&lt;Super&gt;f" type="string" value="/home/humitos/bin/change-window firefox"/>
   <property name="&lt;Super&gt;a" type="string" value="/home/humitos/bin/change-window thunar"/>
   <property name="&lt;Super&gt;c" type="string" value="/home/humitos/bin/change-window pidgin"/>

Ahora sí, con `Super+t` voy a la terminal de Terminator sin importar
dónde esté en ese momento. Lo mismo para `Super+f`, `Super+c` y
demás. Antes de que pestañés, yo ya cambié 5 veces de ventana y
siempre exactamente a la que quería ;)

Te aseguro que te vas a ahorar milisegundos con esto. Luego segundos,
luego minutos y finalmente unas cuantas horas y puteadas de haberte
pasado por uno con el Alt + TAB y tener que dar toda la vuelta cuando
tenés 15 ventanas abiertas.

¡Ah! Y una cosa que me olvidaba: si el programa del cual presionamos
el hotkey no está abierto, lo abre ;)

Vos, ¿cómo resolvés este *problema*?

.. _wmctrl: http://tomas.styblo.name/wmctrl/
.. _xfce: http://www.xfce.org/
