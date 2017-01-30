.. title: Emacs fácil
.. slug: emacs-facil
.. date: 2017-01-27 21:34:54 UTC-03:00
.. tags: emacs python programación cuenca ecuador
.. category: 
.. link: 
.. description: Bajá una imágen de Docker y probá emacs
.. type: text

Lo primero que hay que preguntarse es, ¿se puede?

Sí, hay una forma de configurar emacs y que sea sencillo. ¿Cómo?
Usando el trabajo que los otros han estado haciendo :) . El mismísimo
mundo se basa en eso, entonces, ¿porqué no hacerlo nosotros también?

Una de mis preocupaciones con Emacs era encontrar una forma fácil de
compartir mi configuración para que otro la pruebe sin que re rompa la
cabeza. En principio creé un repo git para eso, pero no fue
suficiente. Es cierto que yo demoré bastante hasta entender cómo
funcionan estas cosas.

Luego pensé en hacer un paquete con mi config, pero al final de cuenta
también ya necesitás un nivel de conocimiento de emacs.

Después escribí un script `tryit.sh` basándome en la idea de los que
escribieron `helm` (un plugin de emacs). Básicamente, bajás el repo
mio de git, ejecutás `tryit.sh` y ya haría todo lo necesario para que
funcione. Sin embargo, mantenerlo y hacer que funcione en diferentes
versiones de Linux fue complicado. Abandoné rápido por no tener una
forma fácil de probarlo.

Hoy está de moda Docker, así, ¿porqué no dockerizarlo?

Hice una primera prueba con Ubuntu y la imagen terminó pesando 1.2 GB,
lo cuál no tiene sentido para mí. Así que busqué otras alternativas y
llegué a Alpine Linux (3.8 MB).

Luego de probar algunas cositas, llegué a la primera configuración e
imagen lista para ser corrida (~350 MB). Entonces, si tenés docker
instalado en tu máquina hacé::

    docker run --rm -it -e DISPLAY -v $(pwd):/src -v /tmp/.X11-unix:/tmp/.X11-unix:ro -v $XAUTHORITY:/root/.Xauthority --net=host humitos/emacs-x11-alpine

Esperá unos 5 minutos que baje la imagen y probalo!

Referencia: https://github.com/humitos/emacs-configuration
