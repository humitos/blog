.. title: Proxy web en 3'
.. slug: proxy-web-en-3
.. date: 2015-01-07 19:05:15 UTC-03:00
.. tags: proxy, squid, ubuntu, software, software libre, linux, gnu
.. link: 
.. description: 
.. type: text

Hoy, por alguna razón que desconocemos hasta el momento, la
computadora de Johanna no tiene internet. Se conecta a la red de wifi
de la casa de Pablo y Cindy pero no carga *algunas páginas*.

Tiene resolución de DNS y ping al router y `google.com` entre
otros. Por ejemplo, la página de YouTube la carga sin problemas e
incluso reproduce el video sin cortes. Quise probar con otro navegador
(ella usa Firefox ;)) y, como no tenía ninguno instalado probé
instalar `links2`.

Sin embargo, nunca pudo comenzar a bajar los datos del paquete. Pero,
si le hago un ping a `ar.archive.ubuntu.com` (que es la dirección a la
que se conecta) anda bien. ¿Qué onda?

Así que, como necesitaba una solución rápida y no quería investigar
mucho sobre un problema de networking (que entiendo poco), fui a lo
fácil e instalé un proxy Squid en mi máquina (que sí tiene internet y
anda bien -usando la misma red).

¿Cómo lo hice? Siguiendo esta guía_...

.. _guía: http://en.kioskea.net/faq/804-installing-an-http-proxy-server-squid

... que básicamente son estos comandos:

.. code:: bash

   sudo apt-get install squid
   sudo su -
   echo "visible_hostname humitos" >> /etc/squid3/squid.conf
   echo "http_port 192.168.1.104:3128" >> /etc/squid3/squid.conf
   echo "acl lanhome src 192.168.1.0/255.255.255.0" >> /etc/squid3/squid.conf
   echo "http_access allow lanhome" >> /etc/squid3/squid.conf
   squid3 -k reconfigure
   exit

Ir al Firefox de ella y configurar el proxy ahí.

  Me llevó más tiempo escribir el post que configurar el proxy...

.. admonition:: Nota

   No es *ni ahí* la mejor solución para esto, pero es rápida y lo
   *suficientemente insegura* como para no tener ningún
   problema. Además, por el mismo precio, tenés un upgrade en la
   velocidad de tu conexión a internet :)
