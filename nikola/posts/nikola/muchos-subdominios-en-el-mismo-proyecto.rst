.. title: Muchos subdominios en el mismo proyecto
.. slug: muchos-subdominios-en-el-mismo-proyecto
.. date: 2014/04/22 23:24:38
.. tags: python, django, software libre, dns
.. link: 
.. description: 
.. type: text

Muchas veces me he encontrado con proyectos, en general Django, que
requieren la configuración de varios subdominios para el mismo
proyecto. Por ejemplo, en el proyecto que estoy trabajando ahora, la
idea es que uno pueda crear torneos dentro del sitio, para el cual el
sistema le asigna un subdominio a cada torneo. Entonces, si el sitio
lo tengo alojado en http://example.com y creo un torneo con el nombre
*Torneo de verano*, la URL generada para mi torneo sería
http://torneo-de-verano.example.com. Una vez que ingreso a esa URL, se
usa el nombre del subdominio (torneo-de-verano) para mostrar el torneo
correspondiente.

¿Qué pasa? Cuando estamos desarollando, el problema con el que nos
encontramos acá, es que en general corremos el servidor de desarrollo
en la misma máquina que trabajamos: *localhost* (puerto 8000), por lo
que el ejemplo anterior sería similar pero en vez de example.com se
crea bajo localhost: http://torneo-de-verano.localhost:8000. El
problema que tenemos acá es que el DNS que usualmente consultamos (el
que nos viene de nuestro ISP) no sabe nada sobre localhost y es por
eso que Linux por lo general busca si está *hardcodeado* en nuestro
`/etc/hosts` para saber a dónde redireccionar, pero ahí no dice nada
sobre los subdominios de localhost, así que no sabe a dónde mandarlo y
es por eso que dice que no encuentra nada.

.. sidebar:: Solución manual

   Esto se puede resolver fácilmente agregando a nuestro `/etc/hosts`
   la URL completa del torneo y apuntando a 127.0.0.1, pero la
   desventaja es que lo tenemos que hacer cada vez que creamos un
   torneo.

¿La solución a este problema?: dnsmasq_. Gracias a este servidor de
DNS podemos hacer que todos los subdominios que creamos bajo localhost
apunten a localhost (127.0.0.1) sin trabajo extra cada vez que creamos
un nuevo torneo.

#. Instalación de dnsmasq::

     sudo apt-get install dnsmasq

#. Comentar esta línea en /etc/NetworkManager/NetworkManager.conf::

     dns=dnsmasq

#. Reiniciar NetworkManager::

     sudo restart network-manager

#. Agregar estas líneas a `/etc/dnsmasq.conf`::

     listen-address=127.0.0.1
     address=/localhost/127.0.0.1

#. Reiniciar dnsmasq::

     sudo /etc/init.d/dnsmasq restart

Esto nos permite despreocuparnos de todos los subdominios de
`localhost` ya que siempre van a apuntar a nuestra máquina sea cual
sea. Además de en este proyecto en particular, lo estoy usando para
todos los proyectos ya que me es más práctico levantar un server de
django en <nombre-de-proyecto>.localhost:8000 y así me quedan las
claves, nombres de usuario y demás guardadas en el Firefox para esa
URL específica. Sino, a veces me quiere poner la clave de *admin* de
otro proyecto por ejemplo (que también tiene el usuario admin)

.. _dnsmasq: http://www.thekelleys.org.uk/dnsmasq/doc.html

