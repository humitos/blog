.. link:
.. description:
.. tags: internet, telecom
.. date: 2008/02/27 13:14:42
.. title: Una lucha que nunca va a terminar
.. slug: una-lucha-que-nunca-va-a-terminar

Como comenté en un `post
anterior <http://humitos.wordpress.com/2008/02/22/comunicaciones-un-dolor-de-cabeza/>`__,
una de las veces que llamé a Arnet me dijeron que me iban a cambiar el
modem, pero no me habían dado número de recibo, por lo que pensé que
nunca llegaría.

Cerca de las 11 de la mañana del día de hoy me tocan el portero. Era el
de OCA que me traía el modem. Yo esperando a que sea un modem de lo más
cho\*\* como el Huawei alfajorcito, que sólo tiene conexión USB y a mi
no me sirve, o por lo menos no lo quiero.

Asique lo primero que me fijé era lo que decía en la caja. La primer
línea debajo de "En su interior encontrarás", decía: *Modem ADSL
**Wi-Fi***... Si! Wi-Fi, lo que me pareció bastante raro. Pero igual
firmé todo lo que había que firmar, y cuando empiezo a volver a mi casa,
el tipo me dice que le tenía que dar el modem que yo tenía porque el
comprobante decía "*Cambio de modem*\ ", lo cual no me gustó nada,
porque no me quería llevar ninguna sorpresa después. Pero bueno, no me
quedaba otra. Subí, busqué el modem y lo cambiamos.

Cuando abro la caja, me encuentro con un Modem Wireless, Ethernet con 4
bocas, USB. La verdad muy lindo a simple vista. El transformador
correspondiente, los microfiltros y los cables correspondientes. Ya era
un paso bastante grande. Algunas fotos:

|image0|\ |image1|\ |image2|\ |image3|\ |image4|

Lo primero que hago es conectar todo como se debe, viendo que tenía 4
bocas de ethernet, saqué el switch que tenía antes, ya que no lo iba a
necesitar, si sólo tengo tres máquinas. Entro a la dirección 10.0.0.2
que es dónde se configuraba mi modem anterior. Selecciono que tengo
arnet y demás. Cuando me pregunta el nombre de usuario y contraseña,
pongo lo que me acordaba de haber registrado en la web de Arnet cuando
contraté el servicio *username:* humitos *password:* \*\*\*\*\*\*\* le
doy *Conectar*\ y quedaba mostrando un cartelito que decía
**Conectando...** con una barra de progreso que nunca se modificaba.

Llamo al servicio técnico por primera vez para ver si estaba mal mi
nombre de usuario. Me comunican que estaba fallando la validación de la
contraseña, asique verificamos con otros usuarios de prueba, tampoco
funcionaban. A esta altura ya les había dado mi número de cliente,
nombre del titular, dónde se encuentra vacacionando mi mamá y como se
llama la persona que la estaba acompañando, dónde trabaja y algunos
datos más. En lo más lindo del proceso de comunicación (la musquita) con
el servicio técnico... **¡¡¡SE CORTA!!!** Asique, otra vez a volver a
empezar...

Llamo por segunda vez 0800-555-9999, ingreso todo tipo de datos, hablo
de mi familia y demás, como las quichisientas reiteradas veces
anteriores. Me dicen que ya tengo varios reclamos hechos. Y otra vez
empezamos el proceso de verificación de usuarios de prueba. Mientras
estoy haciendo esto, abro una máquina virtual con virtualbox que tiene
Windows XP y entro a un Internet-Explorer. Le digo que me aguarde un
momento y descubro que la página del modem no es compatible con Firefox
ni con Konqueror, funciona únicamente con IE. El tipo que hizo el driver
del modem un grande, ¡esa esa la gente que necesita el mundo!

Para este momento, el flaco ya me había cambiado la clave. Asique probé
conectarme y funcionó. Le pregunté como era el *password*\ de la sección
de administrador del modem y me dijo que no me lo podía decir, que no
tenía esa información. Llamé de nuevo y me lo dieron (previos 15-20
minutos de espera y charla).

Siguiente paso: *habilitar los puertos para amule, ssh, torrent y
demás.* Como el firmware de este modem es distinto del anterior. Busqué,
busqué, busqué y no encontraba la configuración, hasta que caí en una
`página muy buena <http://wiki.telecomsucks.com/Portada>`__ en la que
hay muchos problemas típicos explicados ahí. El ejemplo de cómo
habilitar puertos era de un firmware viejo, del 2006... Y al parecer
cambió bastante con el del 2007 que es el que tengo yo. Igual logré
hacerlo funcionar sin *demasiadas* complicaciones.

Por el momento, está funcionando como debería... Al menos puedo abrir
páginas, descargar con aMule, y algunas otras cosas más. Vamos a ver
como sigue esto.

.. |image0| image:: http://grulicueva.homelinux.net/~humitos/blog/una-lucha-que-nunca-va-a-terminar/thumbails/HPIM2284.JPG
   :target: http://grulicueva.homelinux.net/~humitos/blog/una-lucha-que-nunca-va-a-terminar/HPIM2284.JPG
.. |image1| image:: http://grulicueva.homelinux.net/~humitos/blog/una-lucha-que-nunca-va-a-terminar/thumbails/HPIM2285.JPG
   :target: http://grulicueva.homelinux.net/~humitos/blog/una-lucha-que-nunca-va-a-terminar/HPIM2285.JPG
.. |image2| image:: http://grulicueva.homelinux.net/~humitos/blog/una-lucha-que-nunca-va-a-terminar/thumbails/HPIM2286.JPG
   :target: http://grulicueva.homelinux.net/~humitos/blog/una-lucha-que-nunca-va-a-terminar/HPIM2286.JPG
.. |image3| image:: http://grulicueva.homelinux.net/~humitos/blog/una-lucha-que-nunca-va-a-terminar/thumbails/HPIM2287.JPG
   :target: http://grulicueva.homelinux.net/~humitos/blog/una-lucha-que-nunca-va-a-terminar/HPIM2287.JPG
.. |image4| image:: http://grulicueva.homelinux.net/~humitos/blog/una-lucha-que-nunca-va-a-terminar/thumbails/HPIM2288.JPG
   :target: http://grulicueva.homelinux.net/~humitos/blog/una-lucha-que-nunca-va-a-terminar/HPIM2288.JPG
