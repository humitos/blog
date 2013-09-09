.. link:
.. description:
.. tags: python, ubuntu
.. date: 2007/09/10 22:03:17
.. title: Programando con Kate
.. slug: programando-con-kate

Hace bastante que estoy buscando un editor de texto en el cuál me sienta
cómodo para programar. Probé varios, `Vim <http://www.vim.org/>`__,
`Scribes <http://scribes.sourceforge.net/>`__,
`Eclipse <http://www.eclipse.org/>`__, etc... Ninguno terminó de
satisfacerme, ni siquiera el `Kate <http://kate-editor.org/>`__ en su
momento.

Pero después de un tiempo encontré varias cosas interesantes en este
editor que algunas ya las había visto en Scribes y me gustaban. Por
ejemplo abrír un paréntesis y que automáticamente te escriba el que
cierra; cuando pasás por encima de un paréntesis te indica con color
dónde este cierra, lo mismo pasa con las llaves (muy útil para programar
en Scheme :) ). También el identado automático cuando presionás *ENTER*
luego de una línea que finaliza con ":" (dos punto) en python por
ejemplo.

Muchas veces me pasa que borro una función (o parte de esta) definida en
una clase y me queda el código con una identación incorrecta, para lo
que tengo que volver toda esa parte 4 espacios hacia atrás o hacia
delante. Para solucionar esta tediosa tarea con el Kate se puede
seleccionar todo el texto al cuál queramos modificar la identación y
presionamos *TAB* para agregar 4 espacios o *SHIFT+TAB* para quitar 4
espacios. Esto siempre me resultó **muy** útil.

También nos permite crear y administrar *"Herramientas externas"* (esta
opción se encuentra en Preferencias -> Configurar Kate -> Herramientas
externas") que yo utilicé para ejecutar la órden **python** y pasarle el
archivo actual de trabajo, así tenemos un acceso rápido a nuestro
programa. Ésta es la órden que actualmente tengo:

    *cd "%directory" && python "./%filename"*

Lo dicho anteriormente unido con que este editor al ser de *KDE* permite
la configuración de accesos rápidos por el teclado, como casi todos los
programas de *KDE*. Lo que yo utilicé para configurar la órden de la
herramienta externa creada anteriormente asignándole la tecla F2. Para
esto hay que ir a Preferencias -> Configurar accesos rápidos. Así
entonces al presionar dicha tecla me ejecuta el archivo que actualmente
tengo en la vista del Kate.

Este editor tiene muchas otras cosas interesantes también. Si
necesitamos editar dos archivos al mismo tiempo, o dos partes del mismo
archivo, podemos partir la vista del editor en dos o más partes con la
opción Ventana -> Dividir vertical/horizontalmente. Posee en la parte
izquierda un *"Navegador del sistema de archivos"* y *"Documentos"*, en
el cual se muestran los archivos de nuestro disco y los que tenemos
abiertos, respectivamente.

Un aspecto **muy** importante que me estaba olvidando, en la parte
inferior de la pantalla tiene varias solapas, *"Encontrar en archivos",
"Terminal", "Salida del make",*\ y se pueden tener más, dependiendo de
los plugins instalados. La primera nos permite buscar un patrón en los
arhivos con la extensión que indiquemos dentro de un directorio. Se
pueden utilizar expresiones regulares. Esto es útil cuando queremos
saber dónde definimos una función por ejemplo, o buscar una variable
para cambiarle el nombre en todos los arhivos, etc. La segunda
(Terminal), es una terminal común y corriente que yo la utilizo mucho
para tener un intérprete python en esta. Se puede minimizar y restaurar;
ésta guarda todo lo que hallamos hecho en el intérprete hasta ese
momento. Interesante.

Posee una cantidad importante de *reglas de resaltado* por lo que lo uso
para programar en cualquier lenguaje y éste respeta distíntas reglas
entre estos.

Existen diversos plugins para este editor, instalando el paquete
*kate-plugins*\ en Kubuntu tenemos unos cuantos, de los cuales lo que
más uso son: *"Extensión del navegador Python de Kate"* que sirve para
ver a la izquierda las funciones, clases, métodos y atibutos de éstas y
localizarlos rápidamente. El otro que más utilizo es *"Herramientas HTML
de Kate"* el cuál nos facilita la inserción de etiquetas HTML
presionando *CTRL+ENTER* y escribiendo el nombre de la etiqueta. Éste
inserta la etiqueta abierta y cerrada poniendo el cursor en medio de
éstas.

Dejo algunos screenshot de éste para que se vea lo práctico y cómodo que
es programar con este editor. Son imágenes de cuando estaba haciendo el
juego para PyWeek: `Twisted
Zombie <http://humitos.wordpress.com/2007/09/08/twisted-zombie/>`__.

|image0| |image1| |image2|

.. |image0| image:: http://humitos.files.wordpress.com/2007/09/katedt3.jpg?w=150
   :target: http://humitos.files.wordpress.com/2007/09/katedt3.jpg
.. |image1| image:: http://humitos.files.wordpress.com/2007/09/kate3aj7.jpg?w=150
   :target: http://humitos.files.wordpress.com/2007/09/kate3aj7.jpg
.. |image2| image:: http://humitos.files.wordpress.com/2007/09/kate1px3.jpg?w=150
   :target: http://humitos.files.wordpress.com/2007/09/kate1px3.jpg
