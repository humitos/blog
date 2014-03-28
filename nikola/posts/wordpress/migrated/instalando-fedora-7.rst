.. link:
.. description:
.. tags: ubuntu
.. date: 2007/09/15 19:29:41
.. title: Instalando Fedora 7
.. slug: instalando-fedora-7


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/09/15/instalando-fedora-7/


Recién termino de instalar y a penas comenzar a configurar mi nueva
instalación de `Fedora 7 <http://fedoraproject.org/>`__. Me decidí a
instalar Fedora por varios motivos. Principalmente porque tengo Kubuntu
en la otra partición pero en la versión Gutsy en la rama *development* y
algunas cosas me andan a **medias.** También porque una vez quise probar
el `Gnome <http://www.es.gnome.org/>`__ y lo instalé sobre el Kubuntu
que tenía y se me armó un quilombo de aquellos. Y por último la versión
de Kubuntu que tengo es la de 64 bits por lo que el Flash no funcionaba,
aunque he probado hacerlo andar leyendo muchos blogs que andan
deambulando por ahí, pero nunca quedó funcionando bien entre una sesión
y otra. A veces me andaba pero cuando reiniciaba la máquina no se veían
más las páginas con flash.

Asique supuse que al instalar Fedora iba a tener algunos problemas
resueltos. Elegí esta distribución porque yo ya la había probado
anteriormente (hace como 1 año) y no tuve una mala experiencia, me había
gustado mucho. Y me dije ¿Y porqué no Fedora?.

Lo más importante para mí al instalar esta distro era poder compartir
los archivos de un sistema en el otro, entonces se me ocurrió compartir
la partición /home y crear el mismo nombre de usuario que tengo en
Kubuntu en la nueva instalación de Fedora.

Lo primero que hice fué bajarme la versión de Fedora 7 desde la
`ésta <http://torrent.fedoraproject.org/>`__ página con el
`KTorrent <http://ktorrent.org/>`__, me sorprendió lo rápido que bajó,
ya que bajaba al máximo de mi conexión. Lo que indica que la gente que
lo compartía no tenía restringido el límite de subida como siempre pasa
con otros torrents. Luego de terminar de bajar (2.7 Gb) lo grabé en un
DVD y al día siguiente empecé a instalarlo.

Configuré el BIOS para poder bootear desde el DVD y funcionó bien, me
mostró las opciones iniciales; elegí *Instalar Fedora en modo gráfico* o
algo similar a eso. Me preguntó el idioma y la distribución de mi
teclado (en modo gráfico de consola) y luego cargó el modo gráfico mucho
más amigable estilo Gnome.

Comenzó el asistente de la instalación, lo primero que noté es que no se
puede hacer **nada** mientras instalás Fedora, como sí por ejemplo
cuando instalás un Ubuntu. Que mientras estás instalando podés usar la
distribución Live-CD tranquilamente. Ese fué el primer punto en contra
que noté. Bueno llegado al punto del particionado, elegí manual y
**borré**\ la partición de Win que tenía (ya que no la usaba para nada y
aparte nunca me anduvo ;) el Vista), creé la partición para el '/' dejé
un poco de espacio por si algún día necesito Win para la facu o algo por
el estilo. También elegí que quería que el '/home' fuera la partición
que yo ya tenía con el '/home' de Kubuntu. Y asigné la partición de Swap
también que tenía. Al darle siguiente, me salta un error que decía:

    *"Ha asignado menos espacio swap (486 MB) de la RAM que tiene a su
    disposición (512 MB) en el sistema. Esto podría afectar
    negativamente al rendimiento."*

Le dí aceptar para que continue con la instalación, no le dí mucha
importancia a eso, no sé si estuve bien o no. Por ahora no se nota
ninguna diferencia. Luego de otros pasos de menor importancia llegué al
momento de configurar el Grub. La instalación de Fedora no me detectó
que tenía otro sistema operativo instalado, por lo que tuve que
agregarlo manualmente con una opción que hay ahí, para que luego de
instalar todo cuando quiera bootear con mi viejo sistema este me informe
de un error diciendo que no encuentra el archivo para bootear :( .

Al terminar la instalación de Fedora, que demoró algo así como 30 min
entre que leía los informes, mensajes y demás, inicié este, puse mi
nombre de usuario y mi clave y me salió un mensaje de error diciendo que
no encontraba un archivo *~/.dmrc* y que no lo único que iba a pasar es
que no se iban a guardar correctamente mis configuraciones. Asique le dí
aceptar y listo.

En este momento me salta otro mensaje de error informándome que no se
podía crear la carpeta *~/gnome2/accels* porque no tenía permisos de
escritura en esa carpeta. ¿Cómo no voy a terner permisos en la carpeta
de mi usuario? Asique reinicié para entrar a Kubuntu y buscar
información en Google de qué podía llegar a ser ese problema y cómo
solucionarlo. En este momento me entero de lo que comenté arriba, en las
opciones del Grub la opción de Kubuntu no funcionaba. Think, think...

Bueno, entonces busqué mi Live-CD de Kubuntu 6.04 y bootié desde este
para restaurar mi Grub que encima no me acordaba como era. Pero la
primer
`página <http://www.guia-ubuntu.org/index.php?title=Recuperar_GRUB>`__
al buscar en google *"recuperar grub"*\ fué la que solucionó el
problema. Entré a mi sistema y pregunté varias cosas en el canal de irc
#ubuntu-es para ver si podíamos solucionar el problema de los permisos
de los archivos. Reciví buenos consejos y me puse a investigar sobre
eso, hasta que caí con el comando ***chmod***, que ya conocía y
***chown*** que no, y que me sirvió para luego bootear con el DVD de
Fedora en la opción Rescue y decirle al sistema que esa carpeta
*/home/manuel* le pertenece al usuario *manuel* y tiene que tener
permisos para hacer lo que quiera. Así fué como se lo dije (logueado
como root):

    *$ chmod 744 /home/manuel -R* *$ chown manuel:manuel /home/manuel
    -R*

Luego configuré el Grub (menu.list) agregando la opción de boteo para el
Fedora 7 que en archivo que estaba levantando (el de Kubuntu), esta
opción no existía. Reinicié y funcionó todo correctamente, me anduvo el
Fedora y Kubuntu a la perfección. El Fedora automáticamente me informó
de que existían unas actualizaciones del sistema asique las puse a bajar
y estoy esperando actualmente que termine para empezar a instalar
algunos programas que quiero usar.

Vamos a ver como me va con Gnome, Fedora y demás *yerbas* nuevas que
estoy probando ;) . Algunos screenshots de cómo es el sistema *"a
secas".*

*|image0|*

.. |image0| image:: http://humitos.files.wordpress.com/2007/09/pantallazoho7.png?w=150
   :target: http://humitos.files.wordpress.com/2007/09/pantallazoho7.png
