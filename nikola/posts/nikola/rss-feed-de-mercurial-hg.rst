.. link: 
.. description: 
.. tags: mercurial, python, rss
.. date: 2013/09/18 10:28:29
.. title: RSS Feed de Mercurial (hg)
.. slug: rss-feed-de-mercurial-hg

Se me ocurrió mantener la traducción del Tutorial de Python actualizada. Pero
claro, para eso tengo que chequear periódicamente para ver si hubo algunos
cambios en los originales. Entonces, el primer paso para cualquier cosa que sea
periódica es un Google Calendar. El segundo: un script.

    ... luego de crear el evento de Google Calendar ...

Me puse a ver como funcionaba el `repositorio de Python`_ de Mercurial y veo
que tiene una opción de RSS_, entonces la cosa se empieza a simplificar. Ya que
teniendo un RSS era más fácil informarse de los cambios. Lo siguiente que hice,
fue buscar el RSS para una carpeta en particular, pero a eso no lo encontré.
Entonces, me fui directamente a la `documentación de Mercurial`_ y encontré que
tiene el RSS Global y el particular para un archivo, nada más :(

Bueno, "Me bajo el global y lo parseo buscando el nombre de la carpeta que
estoy interesado" -me dije. Y... ¿Vos podés creer? El feed RSS solo tiene la
fecha, el título, el autor y mail, el link y el mensaje del commit. ¡Son unos muertos! Ese feed no me
sirve para nada.

Así que, ¿se te ocurre una forma de hacer ésto sin hacer "hg pull" y comparar
eso contra mis archivos de traducciones?

.. admonition:: Solución

    Finalmente, usé el `RSS de tags`_ del repositorio de Mercurial. Ya que cada
    nueva versión, viene con su documentación correspondiente. El problema que
    tiene esto es que quizás entre una versión y otra la documentación varie lo
    suficiente como para que sea tedioso actualizarla (espero que esto no
    pase).

    Utilicé este script para hacer el chequeo:

    .. listing:: check_python_tags.py python

    Finalmente configuré un cron para que lo ejecute una vez al mes.

    .. code::

      0 11 1 * * /home/humitos/.virtualenvs/python-rss/bin/python3 /home/humitos/Source/scripts/check_python_tags.py

.. _repositorio de Python: http://hg.python.org/cpython/
.. _RSS: http://hg.python.org/cpython/atom-log
.. _documentación de Mercurial: http://mercurial.selenic.com/wiki/TipsAndTricks#Track_changes_to_a_repository_with_RSS
.. _RSS de tags: http://hg.python.org/cpython/atom-tags
