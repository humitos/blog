.. title: Actualizar a una versión nueva de Nikola
.. slug: actualizar-a-una-version-nueva-de-nikola
.. date: 2016-02-11 18:26:31 UTC-03:00
.. tags: nikola, perú, las lomas, python, blog, software libre
.. category: 
.. link: 
.. description: 
.. type: text

Nikola_ es un generador de sitios web estáticos que está
buenísimo. Además, es el que uso para mantener este blog y el sitio
web de `Argentina en Python`_ de una forma sencilla y sin mucho
esfuerzo, que me permite focalizarme en el contenido sin molestarme en
recursos de máquina, base de datos y otros dolores de cabeza. Además,
como trabaja con reStructuredText_ me permite aprovechar todo su
poder.

Como decía, es muy simple. Y así también lo es su actualización:

.. code::

   pip install -U nikola

Sin embargo, si tenés un custom theme y querés beneficiarte de los
cambios en el tema del que heredás (yo me baso en `bootstrap3`) es
necesario hacer un paso extra. Ese paso extra consiste en ver las
diferencias de los templates que nosotros hemos modificado con
respecto al tema heredado contra los originales y agregar los cambios
que sean necesarios/compatibles. Para eso yo uso meld_:

.. code::

   meld nikola-git-repo/nikola/data/themes/bootstrap3/templates themes/elblogdehumitos/templates

Y luego contra el theme del que hereda `bootstrap3` que es `base`:

.. code::

   meld nikola-git-repo/nikola/data/themes/base/templates themes/elblogdehumitos/templates

De esa forma controlo las diferencias que haga falta y voy copiando
hacia mis templates las que me benefician.

Por último, es posible que hayan agregado algunas características
nuevas que requieran alguna configuración extra. Para saber cuáles son
esas configuraciones podemos leer el `CHANGES.txt`_ para buscar algo
puntal y agregar la que necesitemos, o bien podemos hacer un proyecto
demo (con la última versión de Nikola instalada) y comparar su archivo
`conf.py`:

.. code::

  nikola version
  nikola init --demo -q /tmp/nikola-demo
  meld /tmp/nikola-demo/conf.py conf.py

¡Ahora sí! Tenemos nuestro sitio Nikola actualizado a la última
versión disponible.

.. _CHANGES.txt: https://github.com/getnikola/nikola/blob/master/CHANGES.txt

.. include:: links.rst
