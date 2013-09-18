.. link: 
.. description: 
.. tags: python, software libre, documentación
.. date: 2013/09/17 23:58:01
.. title: Tutorial de Python en Español
.. slug: tutorial-de-python-en-espanol

La comunidad de `Python Argentina`_ hace tiempo que viene traduciendo el
`Tutorial de Python (en inglés)`_ a su versión en Español. Hoy en día mantiene
dos versiones activas: 2.7 y 3.3.0.

Ayer estuve mirando algunas características que no conocía entre esas
versiones, como para actualizarme un poco y mirar qué hay de nuevo en todo
ésto. También para ver si Python va en una dirección que me gusta o no. Siempre
uno está a tiempo de cambiar de lenguaje favorito por el que más se adapte a
los gustos de uno, ¿no?

Lo estuve mirando un rato, leyendo a consciencia y encontrando algunos que
otros errores de tipeo, sobre todo. Pero en un momento, me surgió una duda
sobre una diferencia entre 2.7 y 3.3, entonces me fui diréctamente al tutorial
en inglés (donde en general está la posta posta) y veo que lo que yo estaba
leyendo en la traducción ni aparecía. Entonces, me fijé a qué versiones
correspondía cada uno y nuestra traducción estaba bastante atrasada. Así que,
me puse *manos a la obra* para actualizarla.

Así, me bajé el código fuente de la documentación que está hoy día en vigencia
(3.4.0a2), me fijé las diferencias con la versión que teníamos traducida y
traduje solamente eso.

Se puede leer la versión actualizada del tutorial aquí_.

.. admonition:: Migrar de SVN a github.com

    El repositorio dónde teníamos el código del tutorial estaba hosteado en
    USLA en un controlador de versiones SVN (que ya está bastante -más que
    suficiente- obsoleto), así que por eso y porque tuvimos problemas para
    hacer *commits* decidimos migrarlo a github.com.

    Como buen programador, quería mantener la historia de los cambios
    conservando sus autores y demás, así que me puse a investigar un poco sobre
    eso y llegué a este link_.

    Finalmente, los pasos que seguí fueron:

    .. code:: bash

       $ mkdir python-tutorial

       $ cd python-tutorial

       $ svn2git http://trac.usla.org.ar/svn/python-tutorial \
           --verbose --username humitos --authors ../authors.txt

       $ git remote add origin git@github.com:PyAr/tutorial.git

       $ git pull origin master

       $ git commit -a

       $ git push origin master

    Ahora el nuevo código está en https://github.com/PyAr/tutorial

.. admonition:: Cambiar autor / email de los commits de git en github.com

    Como buen pelotudo, metí mal el dedo cuando creé el archivo `authors.txt` y
    agregué una "s" de más al email de uno de los traductores. Y... "Oh, qué
    casualidad" era uno de los que más había colaborado. Así que, me parecía
    bastante flojo de mi parte dejarlo así nomás.

    Estuve buscando un poco en Google y caí en diferentes lugares (ser
    programador en el 2013 es una pelotudés) con muchas soluciones distintas.
    Yo usé `éste script`_ para re-escribir todos los commits de ese usuario y
    cambiar su dirección de email para que sea la correcta y quede `asociada a
    su cuenta de usuario`_.

    Por último, cuando hice `git push` me encontré con un error y tuve que
    investigar un poquito más hasta llegar a `este post`_ y encontrar el comando
    mágico que forza el push de todos modos:

    .. code:: bash

       $ git push origin +master:master

    .. warning::

       OJO! Yo hice este maneje *únicamente* porque el repositorio fue creado
       hoy y no hay nadie trabajando en él aún, pero hacer cambios en el
       historial de commits no está recomendado.

.. _Python Argentina: http://python.org.ar
.. _link: https://help.github.com/articles/importing-from-subversion
.. _Tutorial de Python (en inglés): http://docs.python.org/3.4/tutorial/index.html
.. _aquí: http://tutorialpython.com.ar

.. _éste script: https://help.github.com/articles/changing-author-info
.. _asociada a su cuenta de usuario: https://help.github.com/articles/why-are-my-commits-linked-to-the-wrong-user
.. _este post: http://kevin.deldycke.com/2010/05/how-to-fix-bad-commit-authorship-git/
