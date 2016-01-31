.. title: Crear lista de thumbnails bonitas
.. slug: crear-lista-de-thumbnails-bonitas
.. date: 2016-01-05 23:05:26 UTC-03:00
.. tags: nikola, thumbnails, galería, plugins, argentina en python, prensa
.. category: 
.. link: 
.. description: 
.. type: text


Tenía ganas de cambiar la presentación de los artículos de la sección
de prensa en el sitio de "Argentina en Python" ya que eran simplemente
una lista con la fecha y los links a la página y se veía horrible.

Esto tenía dos objetivos claros:

#. Que se vea bonito, claro
#. Tener un backup en imágenes de los sitios donde salió la nota

¿Qué pasa? Muchas veces esos sitios, blogs, links, lo que fuere; se
caen o cualquier cosa y yo pierdo un material que *para mí* es
importante. Entonces, quería tener una imagen completa del sitio web
en dónde salió publicado. Para esto utilicé la extensión `Full Page
Screen Capture
<https://chrome.google.com/webstore/detail/full-page-screen-capture/fdpohaocaechififmbbbbbknoalclacl>`_
en cada uno de los sitios web.

Luego necesitaba hacer un thumbnail pequeño, pero que también se note
algo de lo que era el sitio web. Aquí robé la idea de la presentación
del `sitio web de donaciones de Joac
<http://joac.github.io/donations/>`_ que no muestra el sitio web
completo, sino solo la primera parte. Para hacer *resize* y *cortar*
la imágen utilicé, obviamente, `convert` de ImageMagick:

.. code:: bash

   for F in `ls *.png`; do {
       convert -resize 340x -crop 340x255+0 ${F} `basename ${F} .png`-340x255.png
   }; done

Ese comando achica la imagen a 340px de ancho y a su correpondiente de
alto, manteniendo el aspecto. Además, luego la corta a 340px x 255px y
guarda el resultado con el mismo nombre que el archivo original pero
le agrega `-340x255` antes del `.png`

Una vez que tenía esto, utilicé el plugin `meta_template
<https://github.com/getnikola/plugins/pull/126>`_ de Nikola que hice
hace unos días para incrustar los divs de Bootstrap3 como
deseaba. Este es el template que utilicé:

.. code:: html

   <div class="col-md-4 col-sm-6 col-xs-12" style="min-height: 435px;">
    <div class="thumbnail">
      <a href="${href}">
       <img src="${src}" style="width: 340px; height: 255px;">
      </a>
      <div class="caption">
       <h3><strong>${title|h}</strong></h3>
       <p>${description}</p>
      </div>
    </div>
   </div>

Y luego, dentro de mi archivo `.rst` de la página de Nikola:

.. code:: rst

   .. template:: prensa-image
      :title: Blog de La Nación
      :description: Sexto encuentro nacional de Python Argentina
      :src: 2014_noviembre_1-340x255.png
      :href: http://blogs.lanacion.com.ar/data/argentina/sexto-encuentro-nacional-de-python-argentina/


El resultado en vivo: http://argentinaenpython.com.ar/historia/prensa/

.. figure:: prensa-section.thumbnail.png
   :target: prensa-section.png

   Sección de prensa de Argentina en Python
