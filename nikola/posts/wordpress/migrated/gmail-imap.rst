.. link:
.. description:
.. tags: google, internet
.. date: 2008/03/11 20:08:02
.. title: Gmail + IMAP
.. slug: gmail-imap

Estos meses que no estuve en casa, se me presentó varias veces el mismo
problema. Si bien lo tengo hace un tiempo, nunca era tan frecuente como
ahora, ya que no estuve en casa por mucho tiempo.

Yo compruebo mi correo de Gmail con `KMail <http://kmail.kde.org/>`__ y
uso `POP3 <http://es.wikipedia.org/wiki/APOP>`__. Pero, ¿Qué pasa? ¿Cuál
es el problema?. POP3 te descarga el correo a la computadora y, en la
mayoría de los Free-Mail, los borra del servidor. Aunque Gmail puede no
trabajar de esta forma, se le puede indicar a Gmail que deje una copia
de los correos descargados mediante POP3 en el servidor.

Ahora, el problema que yo tenía, es que si descargaba durante algunas
semanas mis correos con KMail, leía, administraba, respondía y demás,
cuando me iba de mi casa (computadora) y checkeaba el correo en otro
lado vía Web, no sabía qué correos había leido y cuales no, ya que Gmail
no te marca los descargados mediante POP como leídos o algo así.

Estuve pensando en crear otra cuenta de Gmail y redireccionar los
correos que llegaban a mi cuenta común para despues descargar todos
mediante POP3 y borrarlos de Gmail. Lo cual era bastante complicado para
luego seguir las conversaciones, ya que si tengo un mail nuevo pero no
tengo el mail anterior a cual este nuevo le respondió, no me sirve de
mucho.

Se lo comenté a algunos amigos, y me dijeron que lo que pensaba iba a
funcionar pero que no era lo ideal. La otra forma que se me ocurrió era
siempre leer los correos desde mi máquina. Por acceso SSH y levantando
un Mail-Reader de consola que me muestre las carpetas de Gmail. Probé
uno (`mutt <http://www.mutt.org/>`__) pero al parecer no levanta
las\ **subcarpetas** de KMail. Asique lo descarté.

Después le comenté el problema a
`Karucha <http://www.karuchin.com.ar/wordpress/>`__, y me dijo que lo
que yo estaba buscando se llamaba
`IMAP <http://es.wikipedia.org/wiki/Internet_Message_Access_Protocol>`__
y era más viejo que yo. Que lo que hacía el tipo era leer los correos de
la web en tu cliente pero estando siempre conectado a este. Entonces,
marcás una conversación como *no leída*, y se marca en el servidor
también. Exactamente las mismas cosas que hacés en Gmail, muy bueno.
"Era justo lo que estaba buscando", le dije.

Intenté configurar todo vía SSH, pero se complicó bastante, ya que
Karucha no tenía una buena conexión de internet, pero algo se pudo
hacer. Igualmente cuando llegué de lo de Karucha me puse a configurarlo
directamente en mi computadora.

Estuve viendo y KMail tiene dos tipos de IMAP. El primero es el común,
que realiza todo tipo de acción directamente en el servidor. Por
ejemplo, para leer un mail tenés que estar conectado, y cada vez que
quieras leer el mismo mail, vas a tener que estar conectado. Y el otro
tipo es *IMAP Desconectado*, **este** es el que me sirve a mi. Funciona
así, te baja todos los correos, de la misma forma que POP3 y luego todos
los cambios que se hacen en el cliente (KMail) cuando se presiona el
botón de comprobar correo se realiza una sincronización y tanto el
cliente como el servidor quedan iguales. Esto se pasa.

Ahora bien, leí la ayuda de Google y Gmail, configuré todo como es
debido y me encuentro que es **ultra lento**, demasiado para mi gusto.
Es lento en descargar los mail, en comprobar el correo nuevo, en
sincronizar, en todo. Cubre mis necesidades porque hace lo que quiero,
pero si el servicio que brinda Google con IMAP tiene esta velocidad,
prefiero quedarme con POP3 con sus limitaciones.

Incluso, me parece extraño que en la `página de
ayuda <http://mail.google.com/support/bin/answer.py?ctx=%67mail&hl=es&answer=75725>`__
de Gmail sobre qué es IMAP, ellos te aconsejan usar IMAP y te explican
por qué. Textualmente *"Si estás indeciso entre usar POP o IMAP con tu
cuenta de Gmail, te recomendamos IMAP.*"

Ayer lo configuré y hoy por la tarde terminé de bajar mis 504 MB que
tengo en la cuenta de Gmail con una conexión de 1Mb. Algo a demasiado
mucho lento. Lo voy a seguir testeando unos días más y sino voy a volver
al viejo y querido POP3.
