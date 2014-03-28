.. link:
.. description:
.. tags: python, ubuntu
.. date: 2007/10/24 19:04:13
.. title: chmtopdf: conversor de archivos chm
.. slug: chmtopdf-conversor-de-archivos-chm


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2007/10/24/chmtopdf-conversor-de-archivos-chm/


¿Qué es esto? Lo mismo digo. Hace como mucho una semana empezamos un
`proyecto <http://humitos.wordpress.com/proyectos/>`__ con el
`Guille <http://nercof.wordpress.com>`__, para hacer un programa que
convierta los archivos
`CHM <http://es.wikipedia.org/wiki/Microsoft_Compiled_HTML_Help>`__
(formato de ayuda `HTML <http://es.wikipedia.org/wiki/HTML>`__
comprimido de Microsoft) a cualquier otro formato que sea imprimible. Ya
que algunas editoriales ofrecen en internet libros en este formato, o
incluso directamente en HTML, de forma gratuita.

La idea salió cuando estaba en mi casa con ganas de leer algo nuevo de
Python y seguir estudiando inglés. Busqué algunos libros en internet y
encontré. Pero otra vez lo mismo que cuando quise leer uno de
`TurboGears <http://www.turbogears.org/index.html>`__, **es muy pesado
leer desde el monitor**, al menos para mí. Entonces dije: ¿Y porque no
hacer un programa que descomprima el CHM y lo pase a formato
`PDF <http://es.wikipedia.org/wiki/Portable_Document_Format>`__ con lo
que aprendí de `LaTeX <http://es.wikipedia.org/wiki/LaTeX>`__? Si esto
se cumpliera me quedaría un libro de primera calidad, igual a cualquiera
de una editorial o **muy** similar al menos.

En ese momento, levanté el teléfono y llamé al Guille. Le comenté la
idea y me dijo que en cuanto pueda se venía para casa a empezar a pensar
el *sistema*. Así fue como comenzó el desarrollo de esta aplicación,
revolviendo viejos conceptos que alguna vez había manejado con el módulo
`BeautifulSoup <http://www.crummy.com/software/BeautifulSoup/>`__ para
parsear los HTML (de hecho, excelente módulo) empezamos a ver qué
podíamos hacer y cómo encarábamos el problema. También hubo que hacer
memoria de HTML,
`CSS <http://es.wikipedia.org/wiki/Hojas_de_estilo_en_cascada>`__, y
demás conceptos que estaban bastante olvidados.

Así y todo, programando dos días seguidos, con varias ilusiones y
desilusiones en el medio, llegamos a **algo** muy crudo esos dos días
que estuvimos. Pero ya se acercaba a lo que estábamos buscando. El
problema era que sólo funcionaba para un archivo chm y no se podía
configurar desde ningún punto de vista.

Los principales problemas fueron la inserción de los caracteres
correctos en LaTeX, las tablas HTML, las viñetas, y otas cosas raras de
HTML y CSS que muchas no son tan estándares como parece al principio. O
mejor dicho quizás son estándares pero bastante bien mezclados y *rompe
coco* :P .

Nos juntamos una vez más (sólo medio día) y terminamos sacando la primer
versión **configurable** del programa. Bastante **cruda** y difícil de
llevar a cabo la configuración, pero configurable al fin. Incluso hasta
ahora no sabemos bien cómo hacer para que cualquier usuario con
desconocimiento de todos los conceptos mencionados pueda convertir su
chm a pdf.

Actualmente el proyecto está disponible en internet, se puede descargar
el código fuente y realizar cualquier tipo de pruebas con él. Proponer
ideas, correción de bugs, y demás. Estamos abierto a cualquier
sugerencia que sea.

En la `Página Oficial del
proyecto <http://code.google.com/p/chmtopdf/>`__ está una explicación de
cómo se usa, hay un ejemplo de los resultados que se obtienen y
demás.\ ` <http://code.google.com/p/chmtopdf/>`__
