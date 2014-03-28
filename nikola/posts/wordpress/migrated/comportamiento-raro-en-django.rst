.. link:
.. description:
.. tags: django, python
.. date: 2010/11/16 22:18:56
.. title: Comportamiento "raro" en Django
.. slug: comportamiento-raro-en-django


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2010/11/16/comportamiento-raro-en-django/


En pocas palabras tengo un modelo que obtengo desde su *id* que me viene
por la url. Para esto utilizo la función **get_object_or_404** que
trae Django. En el medio de la vista de Django aplico algunas funciones
a esta instancia del modelo y me estoy encontrando con que luego de
aplicar funciones que modifican la base de datos (la fila a la que
apunta esta instancia); la instancia no se actualiza y me devuelve
valores viejos. ¿Esto está más relacionado con Python que con Django?

El caso que tengo es este (en
`Pastebin.com <http://pastebin.com/r7f6YJA4>`__):
``  >>> def modify_model_state(model):  ...   model.state = 'Closed'  ...   model.save()  ...  >>> model = get_object_or_404(Model, pk=pk_object)  >>> model.state  u'Open'  >>> modify_model_state(model)  >>> model.state  u'Open'  >>> the_same_model = Model.objects.get(id=pk_object)  >>> the_same_model.state  u'Closed'  >>> ``

En realidad esto está muy simplificado, pero refleja exactamente lo que
tengo en mi código y lo que estoy "viviendo" :P
