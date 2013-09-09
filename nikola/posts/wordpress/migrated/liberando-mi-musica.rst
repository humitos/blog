.. link:
.. description:
.. tags: musica, ubuntu
.. date: 2007/09/17 13:04:05
.. title: Liberando mi música
.. slug: liberando-mi-musica

 

Luego de mi instalación de Fedora, que he comentado anteriormente, me
encuentro que al abrir el reproductor de música que trae por defecto
(`Rythmbox <http://www.gnome.org/projects/rhythmbox/>`__) e importar mi
música; éste me informa que no tiene el soporte para .mp3 y que debía
instalarlo. Cómo no estoy muy entendido en el manejo del yum (gestor de
paquetes estilo apt-get) todavía.

En la `página oficial <http://fedoraproject.org/wiki/Multimedia>`__ de
Fedora dice que no incluyen el soporte para mp3, dvd y otros formatos
multimedia ya que estos no están liberados bajo patentes libres y por lo
tanto no cumple algunas reglas de la filosofía del proyecto.

Después de quejarme un rato (al igual que cuando instalé Kubuntu y
tampoco traía soporte para estos archivos) lo pensé y me puse a
investiga y econtré que el Proyecto Fedora alienta el uso de `Ogg
Vorbis <http://es.wikipedia.org/wiki/Ogg>`__ como alternativa a los mp3.
Ogg es un formato libre desarrollado por la `Fundación
Xiph.org. <http://es.wikipedia.org/wiki/Fundaci%C3%B3n_Xiph.org>`__

Incluso, investigando, encontré decir que Ogg es superior en cuanto a la
calidad de los mp3 y encima ocupa menos espacio con las mismas
características. Entonces ni lo dudé y me puse a **liberar mi música** a
un formato superior, de código abiert, multiplataforma, etc... Varias
razones por las cuales hacerlo.

Encontré en Google que existía un comando para convertir de mp3 a og,
¿Cómo se podía llamar si no **mp32ogg**?. Asique lo busqué con
*apt-cache search mp32ogg* y dí en la tecla, estaba en mis repositorios,
lo instalé con *apt-get install mp32ogg* y convertí **toda** mi música a
un formato libre:

    *$ mp32ogg toda-mi-musica/* *--delete$ mp32ogg --delete
    toda-mi-musica/*

Con esto estoy diciendo que me convierta **todos** los archivos que
están dentro de esa carpeta de las que están dentro de éstas de forma
recursiva y que además cuando la conversión halla terminado borre el
arhivo .mp3.

Listo! Ahora soy un poco más libre que antes... Comenzaré a grabar todos
mis dvd's con la música en este formato.
