.. link:
.. description:
.. tags: internet, python
.. date: 2008/02/27 13:32:16
.. title: Parseando un feed
.. slug: parseando-un-feed


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2008/02/27/parseando-un-feed/


Hace como una hora que llegué a mi casa, me bañe y me puse a buscar algo
para hacer con Python. Le pregunté a
`perrito666 <http://www.perrito666.com.ar/>`__ sobre el
`facundario <http://www.perrito666.com.ar/facundario/facundario.py>`__,
ya que había estado teniendo algunos problemas. Y me dijo que todavía no
lo había visto, asique seguí buscando otra cosa.

Me acordé que mi amigo personal, aunque desconocido, Leo
(leo_rockaway... ups perdón **leo_rockway**) estaba buscando un feed
que le informara como era el cambio entre una moneda a otra de forma
actualizada. Hacía algún tiempo que estaba buscando eso, pero hacía unos
días me había comentado que lo había encontrado. Busqué en los logs de
las conversaciones y no encontré la dirección asique busqué en Google:
"currency feed" y era el **primer link**, lo que me hizo pensar que fue
bastante vago para buscar este pibe.

Como nunca había parseado un archivo de feed, ni sabía que tan
complicado era, o que tan fácil, me puse a ver qué podía hacer. Hacía un
tiempo que yo le había *recomendado* a Leo el módulo
`feedparser <http://www.feedparser.org/>`__\ de Python, aunque nunca lo
había utilizado.

Lo primero que hice fue fijarme si lo tenía instalado. Como lo tenía, me
leí la documentación de ejemplo que hay en esa página web y me fue
suficiente para hacer lo que Leo necesitaba. Busqué cómo estaban
ordenados los cambios del feed de pesos argentinos a alguna otra moneda,
el que *me interesaba*\ era el cambio con respecto a dólares
estadounidenses. Éste aparecía en la antepenúltima ubicación.

Con un par de líneas me dí cuenta que obtenía lo que quería. No puedo
dejar de sorprenderme con Python, no puede ser todo tan fácil. ¿O yo soy
muy inteligente? :) [1]

::

    >>> import feedparser

    >>> import re

    >>> rss = 'http://currencysource.com/RSS/ARS.xml'

    >>> feed = feedparser.parse(rss)

    >>> title = feed['entries'][-3]['title']

    >>> title

    u'1 ARS = USD (0.331388)'

    >>> regex = re.compile('(.+)')

    >>> result = regex.search(title)

    >>> result

    <_sre.SRE_Match object at 0xcc9510>

    >>> title[result.start():result.end()]

    u'(0.331388)'

    >>> title[result.start()+1:result.end()-1]

    u'0.331388'

    >>>

Y ahí sale andando fácil ahora Leo. Ya tenés la equivalencia que
necesitabas. Espero que te sirva de algo. Podés encarar tu problema de
varias forma ahora, esto era lo más fácil de hacer, por eso lo hice
yo... ;)

[1] no lo creo, después se me complicó con la expresión regular y era
una boludés.
