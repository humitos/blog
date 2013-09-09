.. link:
.. description:
.. tags: olpc, python, software libre, sugar
.. date: 2012/03/26 15:02:26
.. title: Mi primer commit en OLPC
.. slug: mi-primer-commit-en-olpc

Estas últimas dos semanas se las estuve dedicando casi de lleno al
proyecto `OLPC <http://one.laptop.org/>`__. Sinceramente, perdí mucho
tiempo en compilar Sugar con JHBuild. Personalmente creo que al proyecto
le falta *aliviar*\ la puerta de entrada a los programadores. Incluso,
hubo varias cosas que pude resolver por mi sólo (siendo un programador
Python con experiencia) pero así y todo no pude terminar de compilarlo
sin la ayuda que me brindaron en el canal de irc en *FreeNode:
**#sugar***

Con esto quiero decir que, el programador Python que simplemente quiere
hacer una nueva actividad concreta y sencilla, antes de poder programar
va a tener que luchar intentando abrir esa puerta de entrada y puede
pasar que termine frustrándose y dejando su idea original de lado. Es
por esto último que intenté aliviarle este trabajo a los programadores
que trabajen en Debian con el `post
anterior <http://humitos.wordpress.com/2012/03/19/compile-sugar-on-debian-testing-wheezy/>`__.

En lo personal, el proyecto OLPC siempre interesó debido a que es algo
completamente revolucionario e innovador. Muchos proyectos nacieron a
raíz del proyecto OLPC. Además, es una propuesta ambiciosa, dónde se
quieren **hacer bien las cosas**. Con esto quiero decir que si hay un
bug que resolver, no estás peleando con el cliente para explicarle que
"no hay que resolverlo así nomás" sino que hay que hacerlo bien.

Otra cosa que me gusta, y mucho, es que es Software Libre. El código que
todos escriben (y ahora puedo decir: escribimos :P) está disponible en
internet para que todos los vean, hagan correcciones y aprendan de lo
que otro escribió. Además, las conversaciones de las listas de correo,
las del IRC y demás. Eso es genial!

Una vez fui a Buenos Aires a una reunión de OLCP en La Tribu y me volví
*shockeado*\ porque habíamos estado hablando un grupo de 20 personas,
entre ellas maestras jardineras, psicopedagogos, maestras de primaria,
psicólogos, y demás. Era buenísimo, mucha gente de diferentes ámbitos
todos juntos para participar en un proyecto de Educación Innovador.
¡Espectacular!

Hoy, estoy orgulloso de haber hecho `mi primer
commit <http://git.sugarlabs.org/terminal/mainline/commit/f88b809dfb7c8f237ab7735f50ec4b8546ac4471>`__
y... ni más ni menos que en la actividad
`Terminal <http://wiki.laptop.org/go/Terminal_Activity>`__ (la consola
de Sugar). Incluso era un
`ticket <http://bugs.sugarlabs.org/ticket/440>`__ con historia, hacía
más de 3 años que estaba abierto y aunque ya había un parche este no
funcionaba correctamente. El problema básicamente era que cuando usabas
la actividad en Full Screen (pantalla completa) y en la consola
ejecutabas una aplicación que requiera el uso de la tecla Esc (escape),
la señal nunca le llegaba a la aplicación ya que Esc se utilizaba para
salir del modo Full Screen. Lo que se hizo fue deshabilitar el uso de la
tecla Esc para salir del modo Full Screen y en cambio, enviarle esta
señal a la terminal Linux en sí. Esto permitió utilizar aplicaciones
como Vim en pantalla completa :)

Todo muy lindo, pero tengo que agradecer a Manuel Quiñones, Python
Argentina, Gonzalo Odiard y Rafael Ortiz que me dieron una gran mano
para poder hacer esto.

¡Estoy muy contento! :D
