.. title: Obfuscar emails en tu sitio
.. slug: obfuscar-emails-en-tu-sitio
.. date: 2016-01-25 23:37:22 UTC-03:00
.. tags: nikola, blog, argentina en python, javascript, rpl
.. category: 
.. link: 
.. description: 
.. type: text

Hace un tiempo ví en el sitio de `Renzo Carbonara <http://ren.zone/>`_
una forma súper facil para obfuscar los emails de su página: una
simple función de javascript que reemplaza un caracter raro por la "@"
(arroba) y otro por el "." (punto)

.. code:: javascript

   window.onload = function() {
     var e = document.getElementById("xyz2");
     e.textContent = e.textContent.replace(/ð/, "@").replace(/ø/, ".");
   };

Quería buscar una forma de llevar eso *automáticamente* a Nikola. Y
hoy llegó el día.

Lo primero que hice fue crear un filtro en Nikola que me reemplaza el
`BLOG_EMAIL` con los caracteres raros:

.. code:: python

   FILTERS = {
       ".html": ["rpl {old_email} {new_email} %s".format(
           old_email=BLOG_EMAIL,
           new_email=BLOG_EMAIL.replace('@', 'ð').replace('.', 'ø')
       )],
   }

Luego agregué la función Javascript de Renzo (con algunas
modificaciones para reemplazar todos los links con *mailto:*) en el
`BODY_END` de la configuración de mi Nikola:

.. code:: javascript

   // de-obfuscate emails
   window.onload = function() {
     var e = document.getElementsByClassName('reference external');
     for (i=0; i < e.length; i++) {
       if (e[i].href.indexOf("mailto:") == 0) {
         e[i].href = e[i].href.replace("%C3%B0", "@").replace("%C3%B8", ".");
         e[i].text = e[i].text.replace(/ð/, "@").replace(/ø/, ".");
       }
     }
   };

Ahora, en teoría, en ninguna página del sitio debería aparecer el
email del autor de forma plana, sino más bien obfuscada.

Como tarea para el lector le dejo la versión que obfusca cualquier
email que uno escriba, sin importar de quién sea.
