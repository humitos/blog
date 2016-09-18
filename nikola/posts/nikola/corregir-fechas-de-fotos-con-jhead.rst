.. title: Corregir fechas de fotos con jhead
.. slug: corregir-fechas-de-fotos-con-jhead
.. date: 2015-12-31 19:18:45 UTC-03:00
.. tags: jhead, foto, django girls, mendoza, galería
.. category: 
.. link: 
.. description: 
.. type: text

Una de las peores cosas que te puede pasar en la vida es que te
olvides de setear la fecha en la cámara de fotos *antes* de comenzar a
tomarlas. Bueno, en realidad no es tan grave, pero cuando el error lo
comete otro hay que hacérselo saber de la forma que más lo impacte
para que no lo vuelva a cometer :D

La cuestión es que sacamos fotos con varias cámaras de fotos en el
taller de `Django Girls Mendoza
<https://argentinaenpython.com/galeria/django-girls-mendoza/>`_ y
luego, a la hora de mostrarlas, está bueno que estén ordenadas de
forma ascendente de la primera que se tomó hasta la última
intercalando las diferentes cámaras. Esto te permite ver cómo fue
evolucionando el evento y desde diferentes puntos de vistas (los
distintos camarógrafos).

Dicho de otra forma, lo que evitamos es comenzar viendo el evento por
el almuerzo, luego el desayuno y finalmente la foto de cierre
siguiendo de cuando inició la charla por la mañana temprano. ¿Se
entiende? Claro, es un quilombo para seguirlo.

Para resolver esto, utilicé `jhead
<http://www.sentex.net/~mwandel/jhead/>`_ que te permite manipular la
información EXIF de las fotos de una manera sencilla:

.. code:: bash

   sudo apt-get install jhead

Una vez instalado, me vastó con el leer el manpage: `man jhead` y
algunos argumentos. Finalmente terminé utilizando estos dos comandos.

.. code:: bash

   jhead -ds2015:11:12 DSCF*.JPG
   jhead -ta+2:00 DSCF*.JPG

:-ds: Sets the date stored in the Exif header to what is specified on
      the command line.
:-ta: Adjust time stored in the Exif header by h:mm forwards or
      backwards.

El primer comando le indica que la fecha de todas las fotos es el 12
de Noviembre de 2015 (cuando fue el taller) y el segundo comando le
dice que sume 2 horas a la fecha de cada una de las fotos. Ese número
de 2 horas *lo deduje* mirando las fotos que habíamos tomado con la
cámara que no tenía correctamente seteada la fecha y comparándolas con
una que sí: mi celular.

Si leiste este post *antes* de las fiestas, vas a configurar
correctamente la fecha de la cámara antes de empezar a tomar fotos. Y
sino, vas a llegar aquí gracias a Google cuando estés desesperado por
querer organizarlas de forma cronológica.

¡Salud!
