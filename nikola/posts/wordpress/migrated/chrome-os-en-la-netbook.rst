.. link:
.. description:
.. tags: google
.. date: 2011/04/15 10:27:38
.. title: Chrome OS en la Netbook
.. slug: chrome-os-en-la-netbook


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2011/04/15/chrome-os-en-la-netbook/


`Chrome OS <http://www.google.com/chromeos/>`__ es el sistema operativo
de Google, que probablemente muchos conozcan de nombre, pero quizás no
lo hayan visto funcionando o ni siquiera un screenshot de cómo luce.

Si bien hace un tiempo que tenía ganas de instalarlo y probar qué tal
funcionaba, nunca tuve el suficiente tiempo como para compilarlo y
ponerme a investigar cómo **hay que hacer las cosas**. Antes de ayer,
caí sobre esta misma inquietud y encontré un pibe (tiene 17 años el
loquito) `que lo compiló <http://chromeos.hexxeh.net/>`__ y creó una
*.img* para que lo descargues y lo uses onda LiveUSB :D

Me puse manos a la obra (dijo el mosquito, ya no hice nada), bajé la
imagen y la metí en un Pen Drive (tiene que se de 2GB al menos) con este
comando:

``  $ dd if=ChromeOS-Flow.img of=/dev/sdd ``

**¡Tené en cuenta que tendrás que cambiar el valor del argumento "of" a
lo que corresponda!**

Luego, puse el PenDrive en la Netbook y en 30 segundos (sí, posta, 30
segundos) ya tenía la pantalla de Login y en 1 minuto (incluído el
tiempo para tipear el `ususario y
password <http://chromeos.hexxeh.net/wiki/doku.php?id=faq#what_are_the_default_username_passwords_for_this_build>`__
-que de hecho es *facepunch/facepunch-*) tenía una página de Google ya
cargada en el navegador Chrome. Groso!

Por suerte, todo me funciona a la perfección: suspende bien, anda
internet, el sonido, la aceleración 3D (o al menos los efectitos los
tira bien), etc. Una cosa que me gustó, es que tiene un Ubuntu Karmic,
entonces podés instalar las cosas que se te canten: yo me instalé el VIM
;)

[gallery link="file" columns="4"]

Lo único que tuve que configurar es el teclado, ya que no pude cambiarlo
desde la interfaz gráfica a Español, así que usé este comando:

``  $ setxkbmap latam``

`Aquí <http://chromeos-blog.com/chrome-os-keyboard-shortcuts/>`__ pueden
encontrar una serie de comandos muy útiles para, por ejemplo, abrir la
terminal dónde tienen que tipear eso :D

... el próximo paso va a ser compilarlo desde 0...
