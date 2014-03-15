.. title: Configurar HDMI (video/audio) en Xubuntu
.. slug: configurar-hdmi-videoaudio-en-xubuntu
.. date: 2014/03/14 21:08:29
.. tags: linux, xubuntu, ubuntu, hdmi, audio, video, notebook
.. link: 
.. description: 
.. type: text

Encontré que Xubuntu trae soporte mandar el audio y el video por la
salida HDMI de la placa Intel HD.

Una vez conectado el adaptador de Mini DisplayPort y el cable HDMI a
este, podemos ir al *Administrador de configuración > Pantalla* y ahí
seleccionar la salida HDMI como activa.

Eso nos habilita la salida en nuestro televisor pero con las pantallas
solapadas (al menos en mi caso). Me mostraba como la pantalla de la
notebook estirada (faltaba un pedazo a la derecha) y lo mismo en el
televisor; aunque en este faltaba un pedazo arriba y abajo.

Lo que hice fue instalar el programa **arandr** desde los repositorios
y mover la pantalla HDMI a la posición que quería que esté con
respecto de la pantalla de mi notebook. ¡Muy fácil: solo arrastrar y
soltar!

.. image:: arandr.png

Ahora me quedaron dos pantallas independientes, en dónde puedo poner
un video en una y escribir un post en la otra. También las puedo
solapar y hacer que se vea "casi" lo mismo en ambas. No es exactamente
lo mismo porque en la notebook no entra toda la pantalla del televisor
(al menos la de este que es como de 42'')

Para el sonido, lo único que hice fue hacer click izquierdo en el
ícono del parlante en la barra de tareas y luego seleccionar
*Configuración* y en Perfil, poner "Digital Stereo (HDMI) Salida".

.. image:: hdmi-sound-conf.png

*Seleccionar que queremos usar la salida HDMI*

.. image:: hdmi-sound-output.png

*Comprobar que efectivamente está saliendo lo que queremos que salga por HDMI*
