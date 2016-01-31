.. title: Python en el Machupicchu
.. slug: python-en-el-machupicchu
.. date: 2016-01-19 13:54:14 UTC-03:00
.. tags: argentina en python, perú, machupicchu, cusco, whatsapp, python
.. category: 
.. link: 
.. description: 
.. type: text

¿Qué tendrá que ver batata con luz eléctrica? -me decía mi mamá. Y
bueno, tan errado no estábamos ya que unos años más tarde descubrí que
con la papa uno puede encender un LED de un par de Volts.

Así mismo te podés estar preguntando vos: *¿Python y el Machupicchu?
¿Qué carajo tiene que ver?*. Si estás siguiendo nuestro viaje con
`Argentina en Python <http://argentinaenpython.com.ar/>`_ sabrás que
hace unos meses estuvimos en la *cresta* del Machupicchu y el
Huaynapicchu, y, si has subido hasta allá, sabrás que no es una tarea
fácil para hacer si lo hacés de la forma económica.

Allá arriba nos sacamos unas fotitos con la remera de Django y también
de Argentina en Python, pero no por eso te voy a decir que Python
estuvo ahí. Sino que, además, cuando bajamos nuevamente hacia
Machupicchu Pueblo, veo que pasa un tipo con una remera de un Tux y le
digo: "Hey, ¿usás Linux?". El tipo me mira como diciento "Este flaco
está del tomate" y me pregunta: "Eh?". "Tu Tux, en la remera". "Ah,
Linux, sí, sí. N~ao hablo españole. I'm from Brasil". "Oh, amazing and
are you a software developer or so? I love Python".

"Python, ah? I've worked on `yowsup
<https://github.com/tgalal/yowsup>`_. A Python client for Whatsapp. I
recommend it to you."

Hoy, unos meses más tarde, necesitaba algo para enviar mensajes a
muchos teléfonos de Whatsapp y me fui a buscar esa herramienta y "Oh,
my god! It just works!". ¡Qué buena onda! Me resolvió mucho la forma
de ponerme en contacto con las personas que se inscriben a nuestros
talleres cuando no responden vía email.

Así lo estoy utilizando. Primero, nos registramos:

.. code:: bash

   yowsup-cli registration --mcc 716 --mnc 06 --phone <YOUR-PHONE-NUMBER> --cc 51 --requestcode sms

Validamos nuestro número con el código que nos llega:

.. code:: bash

   yowsup-cli registration --mcc 716 --mnc 06 --phone <YOUR-PHONE-NUMBER> --cc 51 --register <REGISTRATION-CODE>

Y luego, enviamos el mensaje:

.. code:: bash

   yowsup-cli demos -l <YOUR-PHONE-NUMBER>:<PASSWORD-FROM-LAST-STEP> --send <DESTINATION-PHONE-NUMBER> "Hola"

FUCKING AWESOME!
