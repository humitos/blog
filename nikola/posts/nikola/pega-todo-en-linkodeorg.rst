.. title: Pegá todo en linkode.org
.. slug: pega-todo-en-linkodeorg
.. date: 2014/04/17 13:48:10
.. tags: python, linkodeit, software libre
.. link: 
.. description: 
.. type: text

Últimamente me encontré que la comunidad de Python Argentina está
trabajando en un montón de proyectos: la nueva página de PyAr [#]_,
preciosa [#]_, nikola [#]_, pyconference [#]_, ninja-ide [#]_ y un
centenar de cosas más (que podés ver en acá_). Entre esas cosas, la
que me interesa mencionar en este post es *el pastebin que
inteligente*, que no es ni más ni menos que un pastebin (como tantos
otros) pero con algunas cositas copadas: http://linkode.org

Como todo buen herramienta de pastebin, tiene que tener un comando de
consola para poder pegar la salida de un comando en el servicio
web. Por eso mismo, me puse a trabajar algunas horas en escribir un
programa de línea de comandos que cumpla con lo básico: "capturar la
entrada estandar y publicarla dentro de linkode.org mostrando la URL
como resultado".

Además, cuenta con algunas otras opciones más que hacen que sea un
poco más útil para otras cosas, aunque lo importante es que *lo
básico* sea confiable y funcione correctamente.

El paquete se llama linkodeit_ y lo podés descargar desde PyPI,
utilizando `easy_install` o `pip` o del repositorio de github_::

  pip install linkodeit

Para usarlo::

  $ echo "Hello world!" | linkodeit
  http://linkode.org/VSSUM59FGMvTjKVsBewT53
  $

.. _acá: http://python.org.ar/Proyectos
.. _linkodeit: https://pypi.python.org/pypi/linkodeit
.. _github: https://github.com/humitos/linkodeit


.. [#] https://github.com/PyAr/pyarweb/
.. [#] http://preciosdeargentina.com.ar/
.. [#] http://getnikola.com/
.. [#] https://github.com/PyConference/PyConference/
.. [#] http://ninja-ide.org/
