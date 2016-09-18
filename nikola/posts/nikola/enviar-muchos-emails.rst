.. title: Enviar muchos emails
.. slug: enviar-muchos-emails
.. date: 2016-01-19 20:34:30 UTC-03:00
.. tags: argentina en python, perú, chiclayo, email, python, script, thunderbird, mailmerge
.. category: 
.. link: 
.. description: 
.. type: text


Como en algunos de los eventos que organizamos tenemos una
confirmación por email de parte de los organizadores, siempre tenemos
que enviar unos 40~50 emails a los asistenes (uno para cada uno de
ellos) y luego algunos 30 más para los que, por falta de cupo, se
quedaron afuera.

Para esta tarea probé varias cosas y ninguna, hasta hoy, había sido de
utilidad/simpleza. Básicamente lo que buscaba era que:

* sea simple de utilizar
* los links incluídos en los emails no estén ofuscado
* los emails no tengan textos en inglés
* emails en texto plano
* posibilidad de enviar el mismo email a *una sola* persona

... y probablemente algunas cositas más que ahora no tengo en mente.

Probé `mailgun <http://mailgun.com/>`_, `mailchimp
<http://mailchimp.com/>`_, enviarlos a mano y finalmente terminé yendo
por un plugin de Thunderbird llamado `MailMerge
<https://addons.mozilla.org/es/thunderbird/addon/mail-merge/>`_ que me
recomendó `Facundo <http://taniquetil.com.ar/>`_.

¿Qué tiene de bueno MailMerge? Básicamente te permite enviar emails
personalizados (mediante algunas variables) a todos los contactos que
provengan de un `.csv` o libreta de direcciones. Eso del .csv ya está
bueno porque me ahorra el paso de tener que importarlos (de alguna
manera en particular) a la libreta del servicio que utilice.

Para crear/filtrar ese .csv que necesito darle de comer a MailMerge me
creé un `script en Python
<https://github.com/humitos/argentinaenpython.com.ar/blob/master/tools/mailmerge.py>`_
que lee el .csv que obtengo del formulario de registración de Google
Form, lo filtro de acuerdo a una columna en particular y finalmente
crea el .csv de la forma correcta para MailMerge: que no es ni más ni
menos que en la primera fila los nombres de las variables que querés
utilizar y el resto son los datos.

Para generar ese `.csv` utilizo el script de esta forma:

.. code:: bash

   python mailmerge.py \
     -i /tmp/inscriptos.csv \
     -o /tmp/mailmerge-confirmados.csv \
     --title --strip \
     --email 3 --first-name 1 --last-name 2 \
     --url "https://argentinaenpython.com/django-girls-piura/" \
     --date "Sábado 23 de Enero de 2016" --city Piura \
     --place "UDEP - Universidad de Piura, Av. Ramón Mugica 131, Piura, Piura, Perú" \
     --hour "8:30 (puntual) a 18:30 hs." --days 5 \
     --filter-column 21 --filter-column-text "Confirmado"

Finalmente, mi template/plantilla que utilizo con MailMerge se vé más
o menos así:

:To: {{first_name}} {{last_name}} <{{email}}>
:From: Argentina en Python <argentinaenpython@...>
:Subject: Confirmación: Taller Django Girls en {{city}}
:Body: Hola {{first_name}}! ...

Eso me permite en pocos minutos, confirmar a todos los inscriptos,
avisarles a los que están en "Lista de espera" y seguir con lo que
estaba haciendo.
