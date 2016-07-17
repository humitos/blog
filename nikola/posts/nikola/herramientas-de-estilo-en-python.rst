.. title: Herramientas de estilo en Python
.. slug: herramientas-de-estilo-en-python
.. date: 2016-07-17 15:56:30 UTC-03:00
.. tags: python, estilo, herramientas, programación, trabajo, mozio
.. category: 
.. link: 
.. description: 
.. type: text


Hoy se cumplen oficialmente tres meses que hace que trabajo en
Mozio_. El principio fue complicado porque me tuve que adaptar luego
de más de un año de no programar profesionalmente a tiempo
completo. Entre todas las actividades de adaptación, la lectura, el
estudio a día completo, volver a hablar/chatear en inglés y un sin fin
de cosas más; tuve que :doc:`configurar mi editor de texto
<aplicando-rock-a-mi-emacs>`: Emacs.

Una de las cosas que me gustó de Mozio es que tienen una wiki con toda
la guía de estilo de código de cada lenguaje en el que se
programa. Entonces, obviamente, había una para Python. Luego de leerla
y comenzar a seguirla (obviamente sigue PEP8, pero también tiene
algunas particularidades) me di cuenta que "yo no me tengo que
preocupar por eso, yo tengo que codear y lindo". Pero claro, "lindo"
es relativo, está muy ligado a los gustos personales y para eso se
creó la wiki: para ponerse de acuerdo.

Entonces, había decisiones sobre diferentes cosas de PEP8_ y PEP257_
en las que los developer de Mozio tomaron una decisión. Ahí es donde
se empieza a complicar la cosa ya que necesitás recordar cuáles fueron
esas decisiones que incluso pueden ir en contra de tus gustos.

Me puse a investigar cómo seguir todas estas reglas y llegué a una convinación de:

* isort_: ordena los imports
* autopep8_: fuerza al código a cumplir con PEP8
* docformatter_: aplica las reglas de PEP257 sobre los docstrings
* unify_: coherencia entre comillas dobles y simples

¿Qué hice? Como estaba configurando violentamente mi Emacs, busqué un
plugin para cada uno de ellos y para el que no estaba, docformatter,
me lo creé yo mismo copiando en 99% el código de autopep8.

Ahora, cada vez que guardo un archivo en Emacs se me corren todos
estos pequeños programas por detrás y se me formatea todo
automáticamente para cumplir con las reglas específicas de Mozio.

Por otro lado, la convención que se tomó para los docstring (en uno de
los casos) por los desarrolladores no es la que la PEP257 recomienda y
por lo tanto docformatter_ no cubría ese caso. ¿Qué hice? Lo
`implementé en este Pull Request
<https://github.com/myint/docformatter/pull/11>`_ y el autor, que por
cierto trabaja en la NASA, lo mergió a los pocos minutos.

.. admonition:: Nota

   En la `configuración de mi Emacs
   <https://github.com/humitos/emacs-configuration>`_ encontrás los
   archivos de configuración y parámetros que le paso a cada comando
   para realizar lo que yo necesito de forma adecuada.
  
.. include:: links.rst
