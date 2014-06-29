.. title: Modulos Python
.. slug: modulos-python
.. date: 2014/04/16 17:26:39
.. tags: python, software libre
.. link: 
.. description: 
.. type: text

En esta página describo brevemente cuáles son los módulos de Python
que he encontrado interesante a lo largo de los años.

.. note::

   Esta página es relativamente nueva, por lo que todavía no cuenta
   con mucha información

Python
======

`jedi <http://jedi.jedidjah.ch/en/latest/>`_ una librería de
    autocompletado muy copada, la podés usar en el intérprete
    interactivo común para sugerencias con TAB. También está su
    `plugin para Emacs <https://github.com/tkf/emacs-jedi>`_

`docopt <http://docopt.org/>`_
    librería para crear programas de línea de comandos utilizando un
    docstring (POSIX) como entrada para el parser.

`BeautifulSoup <http://www.crummy.com/software/BeautifulSoup/>`_
    librería para manejar de una forma cómoda archivos HTML y XML sin
    volverse loco!

`six <https://pypi.python.org/pypi/six>`_
    utilidad para hacer compatible un programa con Python 2 y 3

`pudb <https://pypi.python.org/pypi/pudb>`_
    un pdb/ipdb super pulenta con una GUI hecha en ncurses

`wdb <https://github.com/Kozea/wdb>`_
    increíble debugger basado en la web

Django
======

`django-localdevstorage <https://github.com/piquadrat/django-localdevstorage>`_
    descarga (por demanda) las imágenes que están en el servidor de
    producción y que no tenemos en nuestro disco.

`django-rest-framework <http://www.django-rest-framework.org/>`_
    permite crear APIs REST muy fácilmente, con buena documentación y
    fácil de testear.

`django-extensions <https://github.com/django-extensions/django-extensions>`_
    montón de utilidades para django: comandos, model fields y mucho
    más.

`dj-cmd <https://github.com/nigma/dj-cmd>`_
    un simple comando que nos permite ejecutar `python manage.py
    subcomando` desde cualquier directorio del proyecto

`django-debug-toolbar <https://github.com/django-debug-toolbar/django-debug-toolbar>`_
    utilidad para hacer debug de los sitios mientras se está
    desarrollando. ¡Utilísimo! :)

`django-impersonate <https://bitbucket.org/petersanchez/django-impersonate/overview>`_
    permite loguearse con cualquier usuario del sistema siendo un
    usuario con permisos de administrador.

`easy-thumbnails <https://github.com/SmileyChris/easy-thumbnails>`_
    para crear thumbnails automáticamente y forma sencilla.

`dogslow <https://bitbucket.org/evzijst/dogslow>`_
    informa por email sobre requests que toman mucho tiempo

Comandos
========

`linkodeit <https://github.com/humitos/linkodeit>`_
    programa de línea de comando para crear *pastebins* en http://linkode.org

`fabric <https://github.com/fabric/fabric/>`_
    permite hacer todas las tareas de deployment muy facilmente

`fabric-virtualenv <https://pypi.python.org/pypi/fabric-virtualenv>`_
    shortcuts para utilizar fabric con virtualenvs

`virtualenvwrapper <https://bitbucket.org/dhellmann/virtualenvwrapper>`_
    herramienta para manejar muchos entornos virtuales (virtualenv) en
    la misma máquina de manera sencilla


.. note::

   Por favor, si sabés de alguna herramienta que me estoy perdiendo y
   que considerás que es muy buena por algún motivo, no dejes de
   decírmelo escribiendo un comentario en esta página.
