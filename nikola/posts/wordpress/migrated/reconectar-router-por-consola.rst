.. link:
.. description:
.. tags: debian, internet, software libre
.. date: 2010/08/20 18:07:16
.. title: Reconectar router por consola
.. slug: reconectar-router-por-consola


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2010/08/20/reconectar-router-por-consola/


En realidad esto me surgió cuando estaba configurando el JDownloader
para que se reconecte automáticamente cuando
`rapidshare.com <http://rapidshare.com>`__\ o algunos similares, dicen
que tenemos que esperar unos cuantos minutos para poder bajar otro
archivo. Como normalmente las cosas que queremos bajar son más pesadas
de la capacidad máxima que estos servidores te dejan bajar, el archivo
que queremos está subdividido en varias partes y entonces es aquí cuando
tenemos este problema.

Como yo tengo Arnet y éste proveedor te da una IP nueva cada vez que te
reconectás, me hice un script para **solucionar** esto. El script se
desconecta y se conecta nuevamente :)

Lo que necesitamos para hacer el script es usar el comando **curl** y
tener el add on del Firefox que se llama `Live HTTP
Headers <https://addons.mozilla.org/es-ES/firefox/addon/3829/>`__, y con
este plugin podemos ver cuál es la información que se le manda al router
para que realice la desconexión/conexión.

Una vez que tenemos instalado el plugin debemos activarlo yendo a
*Herramientas -> Live HTTP Headers* y asegurarnos que el checkbox
"Capturar" esté activado. Una vez que tenemos esto, vamos a la página de
nuestro router (en mi caso 192.168.1.1) y luego a la página dónde nos
muestra el botón para desconectar de internet.

Una vez que estamos ahí, vamos al Live HTTP Headers y nos fijamos si
realmente está capturando los POST, GET, etc; de ser así presionamos el
botón "Limpiar" ya que eso que se muestra ahí no nos interesa y nos
dificultará la lectura posterior.

Ahora ya tenemos todo listo, nos falta presionar el botón y buscar el
POST que se envía al presionar ese botón al router, y copiamos la URL a
la que se envía y también los datos que se envían. En mi caso fue así:

|image0|

Una vez que tenemos esos datos, sólo basta ejecutar el comando **curl**
con los datos obtenidos:

::

    curl "http://<user>:<password>@192.168.1.1/rstatus.tri" \
         -d "action=Disconnect&wan_pro=2&conn_stats=300&layout=en"

    curl "http://<user>:<password>@192.168.1.1/rstatus.tri" \
         -d "action=Connect&wan_pro=2&conn_stats=-1&layout=en"

El primer ejemplo es para desconectar el router y el segundo para
conectar, así funciona la reconexión :) . Ahora sólo falta poner esto en
un script e indicarle al JDownloader que use éste cuando lo necesite.
Para esto, copiamos esos dos comandos en un archivo de texto, lo
marcamos como ejecutable y le agregamos la siguiente línea al principio
para decile que lo ejecute con **bash**:

::

    #!/bin/bash

Luego en el JDownloader, en la pestaña de\ *Ajustes* vamos a *Módulos ->
Reconexión y Router -> Externo* y ahí seleccionamos el script que
acabamos de crear. Luego podemos probar esto con el botón *Cambiar IP*.

Nada más :) , es útil, funciona para cualquier router ya que podemos ver
exactamente la información que se le manda al mismo. Este ejemplo está
basado en el router **Linksys WRT54G v8.0** con el firmware original y
el concepto de estas instrucciones me lo chorié de
`acá <http://www.taringa.net/posts/info/4464454/Tutorial-para-configurar-la-reconexi%C3%B3n-en-jDownloader.html>`__.

.. |image0| image:: http://humitos.files.wordpress.com/2010/08/http-live-headers.jpeg
   :target: http://humitos.files.wordpress.com/2010/08/http-live-headers.jpeg
