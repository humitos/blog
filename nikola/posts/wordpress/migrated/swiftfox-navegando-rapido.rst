.. link:
.. description:
.. tags: ubuntu
.. date: 2007/09/16 23:36:51
.. title: Swiftfox: navegando rápido
.. slug: swiftfox-navegando-rapido

Hace tiempo que me venía quejándo que el navegador que actualmente estoy
usando, `Firefox <http://www.mozilla.com/en-US/>`__, me andaba bastante
lento. Aunque en realidad el navegador que más me gusta a mí es
`Konqueror <http://www.konqueror.org/>`__, decidí cambiarme porque hasta
ahora no he encontrado el plugin para los Bookmarks de
`del.icio.us <http://del.icio.us/>`__, simplemente por esto es que he
dejado de utilizar el Konqueror y muchas veces lo extraño.

Luego de varias búsquedas en Google caí con
`Swiftfox, <http://getswiftfox.com/>`__ navegador basado en Firefox,
pero *optimizado* para los microprocesadores AMD e Intel. La versión
2.0.0.6 de Swiftfox está basada en la versión 2.0.0.6 de Mozilla
Firefox.

Hace como una semana que estoy usando éste, aunque ya lo había probado
en otra oportunida pero no me había gustado mucho como quedaba la
interfaz gráfica sobre KDE. Ésta vez le dí otra oportunidad y dejé de
lado la apariencia del navegador para probar si realmente es un poco más
rápido y si se notaba la optimización de la que se habla. La experiencia
es positiva ya que este ***vuela*** a comparación con Firefox, por lo
menos en mi máquina. Además levanta todas las configuraciones, plugins,
add-ons y demás que teníamos en el Firefox sin hacer absolutamente
nada...

Para la instalación de Swiftfox debemos agregar a nuestros repositorios
*(/etc/apt/sources.list)* la línea:

    *deb http://getswiftfox.com/builds/debian unstable non-free*

Luego hacemos un *apt-get update*\ seguido de *apt-get install
swiftfox-athlon64* en el caso de mi procesador. Para saber que paquete
instalar podés hacer *apt-cache search swiftfox* para ver la lista de
los paquetes posibles.

Algunos screenshots:

|image0|\ |image1|

.. |image0| image:: http://img260.imageshack.us/img260/8586/swiftfox1ho4.th.jpg
   :target: http://img260.imageshack.us/img260/8586/swiftfox1ho4.jpg
.. |image1| image:: http://img518.imageshack.us/img518/9793/swiftfoxwe5.th.jpg
   :target: http://img518.imageshack.us/img518/9793/swiftfoxwe5.jpg
