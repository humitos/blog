.. link: 
.. description: 
.. tags: wordpress, nikola, blog, migración
.. date: 2013/09/09 02:19:08
.. title: Migrar post de Wordpress.com a Nikola
.. slug: migrar-post-de-wordpresscom-a-nikola

Ahora sí. Pasé todos los posts que tenía en Wordpress.com a mi nuevo
blog de Nikola. Si bien ya había probado varias veces hacer esto, hace
un tiempo el importador de Wordpress estaba un poco más verde y yo
tampoco le quería dedicar tanto tiempo a la migración.

Hoy dejé de lado algunos prejuicios y tomé algunas decisiones de las
cuales antes no estaba seguro y finalmente decidí empezar al
revés. Primero, antes de migrar, creo el sitio con Nikola, hago que
funcione y escribo un post que diga que me fui de
Wordpress.com. Después de eso, cuando todo esté funcionando me voy a
preocupar por migrar los posts viejos. Y finalmente, acá lo
hice. Mucho antes de lo que pensaba.

.. note::

   Utilicé este commit de Nikola
   `e14a5244fb3596c2c89f228cec39c9233b226e64
   <https://github.com/ralsina/nikola/tree/e14a5244fb3596c2c89f228cec39c9233b226e64>`_

Estos son los pasos que seguí para hacer una migración lo más sana
posible de esos posts viejos. Todavía me falta arreglar algunas
cositas a mano (como algunos videos de YouTube o algunas cositas de
estilo), pero el trabajo que pude automatizar es demasiado.

#. Instalar Nikola_

#. Aplicar este `parche`_ que:

   - Elimina la fecha del post del slug de la url (por ejemplo:
     20120907mi-casa.html -> mi-casa.html)

   - Corrige los `^M` que agrega Wordpress.com para generar un nuevo
     párrafo y al importar quedan juntos (agrega un `</p>\\n\\n<p>` por
     cada ^M que encuentra para que realmente funcione como un
     párrafo finalmente)

   .. listing:: import_wordpress.py.diff diff

#. Exportar el dump (y bajar el archivo .xml) desde Wordpress.com

#. Crear un nuevo blog importando el dump de Wordpress.com

   .. code:: bash

      nikola import_wordpress --no-downloads --no-drafts --squash-newlines Downloads/humitos.wordpress.2013-09-09.xml temp-blog

#. Copiar los posts importados de nikola a nuestro blog. Yo los puse
   dentro `wordpress`, para hacer una diferencia.

   .. code:: bash

      cd temp-blog
      cp -r posts/ ~/blog/posts/wordpress

#. Instalar `pandoc`

   .. code:: bash

      sudo yum install pandoc

#. Convertir los `.html` a `.rst` utilizando *pandoc*. Lo hice con este script:

   .. listing:: migrate_with_pandoc.sh bash

#. Meter la información del `.meta` dentro del `.rst`. Yo usé este script:

   .. listing:: migrate_meta.py python

#. Tuve algunos problemas con las imágenes ya que por algún motivo
   escapaba los "_"; así que escribí otro script para reemplazarlos

   .. listing:: replace_bars.py python

#. Para migrar los comentarios tuve que:

   - Subir mi archivo `.xml` que bajé de Wordpres.com a disqus.com en
     la sección "Discussions" y luego en "Import", seleccionando
     Wordpress y luego eligiendo el .xml (demora un rato)

   - Edité el .csv generado por el comando "nikola import_wordpress"
     para que apunte a mi nueva dirección.

   - Luego en "Tools" utilizé la herramienta "Upload a URL map" y subí
     ese archivo.

   .. warning::

      Sin embargo, esto no fue suficiente. Wordpress estaba usando el
      ID de cada uno de los blog post como valor para la variable
      "disqus_identifier" y Nikola está usando el path de la carpeta
      "cache/" dónde se encuentra el post

      ¿Se puede decirle a Nikola que use otro ID para los posts?
      ¿Quizás con uno de los metadatos del principio del archivo .rst?

Por el momento, estoy contento con los resultados. Vamos a ver cómo sigue todo.

**UPDATE 10-09-2013**

#. Utilicé este script para cambiar el plugin de wordpress de YouTube
   para en cambio usar la directiva `.. media::` de Nikola

   .. listing:: replace_youtube.py python

.. _parche: import_wordpress.py.diff
.. _Nikola: http://getnikola.com
