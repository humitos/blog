.. title: Aplicando rock a mi Emacs
.. slug: aplicando-rock-a-mi-emacs
.. date: 2016-02-08 16:47:55 UTC-03:00
.. tags: emacs, perú, las lomas, elpy, software libre
.. category: 
.. link: 
.. description: 
.. type: text

Hace tiempo que uso Emacs. Hace *no tanto* tiempo que lo tengo
configurado como me gusta y eso es porque nunca entendí la lógica de
elisp, que es lo que se necesita saber para poder configurar algunas
variables y hacer unos *hook*. Sin embargo, con el tiempo le fui
agarrando la mano y fui pudiendo instalar *a mano* un montón de
plugins que cada tanto, los actualizaba y alguno de ellos
explotaba. Por eso, con el tiempo, se me fueron pasando las ganas de
ir buscando nuevas cosas para *enchular* mi emacs y me dedicaba a
utilizarlo como lo había dejado hace algunos años (por lo menos 2).

Anoche me dije: "voy a volver a ver qué cosas nuevas hay para Emacs y
actualizar mi entorno de desarrollo". Así fue que llegué a elpy_ y a
un `blogpost de realpython.com que está genial
<https://realpython.com/blog/python/emacs-the-best-python-editor/>`_.

Aunque no uses Emacs ni te guste, te recomiendo pegarle una mirada a
ese post de Real Python ya que te puede dar algunas ideas.

Mucho de lo que cuentan ahí yo ya lo tenía configurado, pero a lo
bestia: utilizando hooks y cosas raras para que funcionen y -como no
sabía casi nada de elisp, estaba todo atado con alambre y a veces
crasheaba como loco. No hay nada peor que estar codeando esa idea que
te llevó días poder llegar a tener y que no te funcione tu editor de
código como vos querés. En esos momentos, iba deshabilitando los
diferentes plugins y así me fui quedando con muy pocos.

Hotkeys
-------

Emacs es *un mundo*, posta. No estoy seguro si estos hotkeys son
específicos de elpy, pero son los que me llamaron la atención y que
voy a empezar a usar:

:M-down:
:M-up: desplaza la región seleccionada una línea hacia arriba o hacia
       abajo
   
:M-left:
:M-right: deplazan la región seleccionada un nivel en la identación
          hacia la izquierda o la derecha

:M-z <char>: borra hasta la primera aparición de <char>

:C-c C-f: busca un archivo dentro del proyecto actual (lo adivina con
          heurística) utilizando un poco de fuzzy

:C-c C-s: hace un `grep -r` en el proyecto actual con lo seleccionado

:M-.: va hacia la definición de la función / método / clase sobre la
      que tenemos el cursor
:M-*: vuelve a donde estábamos antes de presionar `M-.`

:C-c C-z: abre un intérprete de Python en un buffer o bien recupera el
          existente

:C-c C-c: manda el buffer actual al intérprete de Python para que lo
          ejecute

:C-c C-d: abre la documentación de Python de la función / método /
          clase sobre la que tenemos posicionado el cursor

:C-c C-t: ejecuta los tests del proyecto

:C-c C-r f: formatea el código utilizando yapf o autopep8

:C-c C-r i: autoimporta módulos que falten y ordena los que ya están
            importados

Conclusión
----------

Hay mucha información sobre cómo instalar estas cosas, blog posts y
documentación oficial. Yo tengo hecho algo que *no recomiendo* porque
es *oldschool* y ahora es mucho mejor utilizar paquetes de META.

Les recomiendo que cada tanto le peguen una mirada a la configuración
que tienen de su editor de código y vean configuraciones de otros,
pero no las copien así nomás, ya que de esa forma van a tener un
montón de cosas configuradas que no van a saber usar. Sino que la idea
es ir configurando de a poco las cosas que vamos viendo interesante y
tratar de sacarle el jugo.

.. admonition:: Mi configuración de emacs

   Tengo un repositorio en Github con toda la configuración de mi
   emacs, por si te interesa ver algo en particular:
   https://github.com/humitos/emacs-configuration


.. _elpy: https://elpy.readthedocs.org/en/latest/index.html
