.. link:
.. description:
.. tags: python, turbogears
.. date: 2007/08/31 03:54:44
.. title: Proyecto de página web
.. slug: proyecto-de-pagina-web

Hace una semana con unos amigos (Juan y Guillermo), empezamos a diseñar,
o intentar a hacerlo, una página web para desarrollarla en Python con
`TurboGears <http://www.turbogears.org/>`__. Con el fin de aprender
TurboGears y si queda buena/usable subirla.

Para esto empecé a leer el libro *"Rapid Web Applications with
TurboGears: Using Python to Create Ajax-Powered Sites"* para poder
comenzar con lo que es TG, ya que nunca antes ninguno de los tres
habíamos hecho nada con este
`framework <http://es.wikipedia.org/wiki/Framework>`__. Cada uno estuvo
leyendo por su parte algunos capítulos de este libro y otros tutoriales
sobre `estilo de programación en
Python, <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html>`__
así ponernos de acuerdo y matener entre todos un estilo para no tener
problemas en el
futuro.\ ` <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html>`__

El tema de la página es *"La movida nocturna en la ciudad de Paraná"*,
pretendiendo mostrar fotos de boliches, pubs, etc de esta ciudad, además
de noticias sobre recitales, fiestas y algunas cosas más.

Para hacer las primeras pruebas sobre la página nos juntamos un fin de
semana a hablar sobre el proyecto y empezar a tirar algo de código.
Diseñamos la estructura de la base de datos, y empezamos a hacer los
primero métodos para actualizar esta. Pensamos el sistema de noticas
para que sea lo más
`automágico <http://es.wikipedia.org/wiki/Autom%C3%A1gicamente>`__
posible y fácil de usar.

El proyecto lo alojamos en Google Code ya que es de código libre y
además nos resulta fácil llevarlo adelante gracias al sistema de
`SVN <http://es.wikipedia.org/wiki/SVN>`__ que Google posee. El proyecto
se encuentra en esta dirección http://code.google.com/p/www-payaso/ y al
código lo pueden descargar desde una consola con el comando:

    *$
    ``svn checkout http://www-payaso.googlecode.com/svn/trunk/ www-payaso``*

Actualmente se encuentra en desarrollo y tiene un avance bastante lento,
debido a que cada uno de nosotros no tenemos los conocimientos sufientes
como para avanzar rápido y ademas estamos programando en otros proyectos
también.

Tengo pensado, a medida que vaya haciendo algo en el proyecto, ir
explicando cómo funciona TurboGears, o en realidad, cómo lo hago
funcionar yo :) en *post posteriores.*\ En la carpeta */doc* del
proyecto se puede ver todo lo que vamos escribiendo sobre convenciones y
forma de funcionamiento de este sistema, por lo cual quizás los post
sean de este manual.
