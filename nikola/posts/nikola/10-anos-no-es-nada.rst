.. title: 10 años no es nada
.. slug: 10-anos-no-es-nada
.. date: 2017-01-29 22:38:37 UTC-03:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

Ayer tuve uno de mis primeros, "¿Pero esto no es lo mismo que nosotros
hacíamos hace 10 años atrás?"

Cuando estaba en Perú, en uno de los peores hospedajes (¡y ciudades!)
que he estado en mi "corta vida" estuve estudiando un poco de *Docker*
porque ya lo había escuchado mucho y nunca me había puesto de
verdad. Así que *me hice el tiempo* para dedicarle unas cuantas
horas. Aprendí poco la verdad. Hice el tutorial y terminé con muchas
dudas.

Hace 2 semanas lo empecé a mirar un poco más en profundidad ya que en
el trabajo lo empezamos a usar y justamente tuvimos tiempo para
experimentar y jugar un poco con casos reales. ¿Viste como es? Uno
aprende mucho más rápido cuando trabaja sobre un problema real que
cuando estudia *porque sí*.

El fin de semana estuve haciendo mi imagen de Docker para la
configuración de mi emacs y quedó de lujo:

   https://hub.docker.com/r/humitos/emacs-x11-alpine/

Durante los días del fin de semana le estaba contando a Johanna lo
contento que estaba por haber hecho esto (ya que mi primera versión
para compartir la config de emacs fue un script de bash `tryit.sh` que
hacía mucha magia loca y fea). Lo primero que le pregunté era si
conocía Docker, para ver desde dónde empezamos a hablar, y me dijo que
había visto algo pero que lo tenía que estudiar mejor: "Es como meter
pequeñas máquinas dentro de la tuya, ¿no?". Y, sí, generalizando es
exactamente eso.

Entonces, cuando le empecé a explicar porqué estaría bueno que lo
miremos juntos -tener todo instalado para que en los talleres sea
súper fácil y compatible de configurar todos los sistemas
tradicionales, me dije: "¿Pero esto no es lo mismo que nosotros
hacíamos hace 10 años atrás con César y vserver?"

¡Pucha, me estoy poniendo viejo! -pensé

Luego de leer un poco, no mucho la verdad, encontré que la principal
diferencia está en la implementación de "la cosa", digamos. Docker usa
LXC que es una forma nativa por parte del Kernel de Linux de realizar
la virtualización y vserver hace algo parecido pero en su propia
modificación del Kernel.

Por lejos, creo que la mejor explicación que encontré viene de `este
post de reddit
<https://www.reddit.com/r/docker/comments/3bzalq/how_is_dockerlxc_different_from_linuxvservers/>`_
y mi conclusión es que *le pusieron un lindo logo* simpático y con una
sonrisa.

Ah, y ¡mucho marketing!
