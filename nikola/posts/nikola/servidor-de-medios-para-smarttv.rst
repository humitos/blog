.. link: 
.. description: 
.. tags: software libre, sysadmin
.. date: 2013/09/14 03:01:58
.. title: Servidor de medios para SmartTv
.. slug: servidor-de-medios-para-smarttv

En casa tengo un televisor `Panasonic SmartTv Viera`__ y tiene la opción de
Viera Connect, que básicamente sirve para conectarse a internet utilizando
alguna de las aplicaciones que trae instadas. Como ser, Netflix, YouTube,
Vimeo, Skype y otras.

Lamentablemente, muchas de esas aplicaciones tildan el televisor cuando lo
exigís mucho. Por ejemplo, entrar a un video, poner pausa, volver hacia atrás,
resumir el video y... Finalmente, lo tenés que apagar y prender. Es malísimo el
software que trae.

Sin embargo, hoy encontré una cosa muy útil y que por el momento está
funcionando bastante bien aunque por ahí laggea un poco la red. La función que
encontré hoy (que en realidad ya la conocía pero no sabía cómo se usaba) es
*Viera Connect - Servidor de archivos* y sirve para reproducir archivos a
través de la red. Por ejemplo, los que están en una computadora o en un
SmartPhone.

Como yo SmartPhone no tengo, configuré mi Ubuntu 13.04 para que sirva los
archivos que yo quiero mediante `minidlna`_ que utiliza *DLNA/UPnP-AV* para
servir los archivos.

Los pasos fueron bastante simples, pero tuve unos problemas con los permisos de
archivos.

#. Instalar minidlna

   .. code:: bash

      sudo apt-get install minidlna

#. Configurar qué archivos servir mediante la variable `media_dir` del archivo
   `/etc/minidlna.conf`

   .. code:: bash

      sudo vim /etc/minidlna.conf

#. Arreglar los problemas de permisos

   - utilizar `/var/cache/minidlna` para `db_dir`
   - ejecutar minidlna como tu usuario y grupo editando el archivo
     `/etc/default/minidlna`
   - detener el servidor

     .. code:: bash

        sudo service minidlna stop

   - cambiar los permisos de la base de datos

     .. code:: bash

        sudo chown -R humitos:humitos /var/cache/minidlna
         
   - escanear las carpetas compartidas

     .. code:: bash

        minidlna -R

La mayoría de la información la saqué de `este post`__. Espero que sea útil, y
si hay algún error o falta hacer alguna modificación, podés sugerirlo en los
comentarios así lo actualizo.

__ http://www.panasonic.es/html/es_ES/Productos/Televisores+VIERA/32+pulgadas/TX-L32E6/Ficha/12284331/index.html
.. _minidlna: http://sourceforge.net/projects/minidlna/
__ http://linuxforums.org.uk/index.php?topic=9822.15

