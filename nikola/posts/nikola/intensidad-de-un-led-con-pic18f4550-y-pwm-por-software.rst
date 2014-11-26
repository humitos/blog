.. link: 
.. description: 
.. tags: icaro, pic, electrónica
.. date: 2013/11/23 00:46:03
.. title: Intensidad de un LED con PIC18F4550 y PWM por Software
.. slug: intensidad-de-un-led-con-pic18f4550-y-pwm-por-software

.. sidebar:: Referencias

   * `Modulación por ancho de pulsos en Wikipedia <http://es.wikipedia.org/wiki/Modulaci%C3%B3n_por_ancho_de_pulsos>`_
   * `Modulación PWM (Pulse Width Modulation) <http://picfernalia.blogspot.com.ar/2012/06/modulacion-pwm-pulse-width-modulation.html>`_
   * `Interrupciones (conceptos básicos) <http://picfernalia.blogspot.com.ar/2012/06/interrupciones-conceptos-basicos.html>`_
   * `Uso de temporizadores (timers) <http://picfernalia.blogspot.com.ar/2012/06/uso-de-temporizadores-timers.html>`_
   * `Microchip Datasheet <http://ww1.microchip.com/downloads/en/devicedoc/39632c.pdf>`_
   * `Manual PIC 18F4550 en Español <http://www.joseapicon.com.ve/descargas/pic/Manual%20PIC%2018F4550.pdf>`_

Estuve toda la semana leyendo las librerías que usa ICARO_ para
manejar los servos y trantando de entender cómo funcionan. La verdad
que no es nada sencillo ponerse a leer código C después de más de 10
años de no tocar una línea de éste. Además, por otro lado, nunca había
trabajado a tan bajo nivel y con el manual de un microcontrolador en
la mano. ¡Toda una aventura!

Por suerte encontré en Internet miles de manuales y post relacionado
con lo que yo quería hacer: utilizar señales PWM. Si bien el PIC que
estoy usando (18F4550) ya trae incorpado por hardware 2 pines que se
pueden usar para crear señales PWM fácilmente, yo quería hacerlo por
software ya que de esa manera me permitiría controlar unas cuántas
más. Si no me equivoco, por lo menos 18. Entonces, como yo quería
manejar al menos 5 señales PWM, decidí encarar el camino complicado y
hacerlo por software.

Me encontré con que no era nada fácil. Pero no es que no era fácil de
programar, sino que no era fácil de entender. Hay muchos conceptos que
no manejo y muchos otros que los he visto pero que no los tengo muy
fresquitos que digamos, así que le dediqué su tiempo a leer y entender
los post que estaba leyendo. No es lo mismo pegarle una leída para ver
cómo viene la mano, que ponerse uno a hacer los cálculos para que los
números coincidan.

Hasta el momento llegué a generar 1 sola señal PWM que controla todas
las salidas del PUERTO B (8 bits) con el mismo ciclo de trabajo
(porcentaje del período que la señal está en ALTO) utilizando el TIMER
0 y la interrupción que este genera una vez que desborda su
contador. Sin embargo, la idea es tunear un poquito más el código cosa
de mantener un valor diferente para cada una de los pines del PUERTO
B. Quizás mañana... Ya veremos...

Ese ciclo de trabajo se puede cambiar modificando ON_PERCENT en la
escala de 0 a 100, con 0 totalmente apagado y 100 totalmente prendido.

Luego de cargar el código en el PIC, conectamos cualquier pin del
PUERTO B a una resistencia de 250 ohms, un LED y finalmente la tierra
de vuelta a la placa en el pin del medio de ("K2" en la placa) los que
están (hay 3) adelante del transistor grande.

El código fuente que se debería poner en `user.c` es éste:

.. listing:: simple_pwm_icaro.c c

.. _ICARO: http://roboticaro.org/
