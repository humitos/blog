.. title: Donaciones para arreglo de vehículo
.. slug: argentina-en-python/donaciones/misiones
.. date: 2015-04-06 11:12:58 UTC-03:00
.. tags: donaciones, argentina en python
.. link: 
.. description: 
.. type: text
.. nocomments: True

Luego de mucho esfuerzo, hemos llegado a una etapa del viaje donde se
empiezan a notar los hitos alcanzados [#]_ [#]_ [#]_ [#]_ [#]_ como
así también las complicaciones económicas para seguir adelante. Y
como todo buen programador, ya habiendo hecho los tests
correspondiente, veo que algunos empiezan a fallar cuando son
proyectados a futuro.

::

   test_sprint_resistencia (tests.test_Sprint_resistencia.SprintResistencia) ... ok
   test_cubiertas_delanteras (tests.test_peugeot206.Peugeot206) ... ok
   test_aceite_y_filtros (tests.test_peugeot206.Peugeot206) ... ok
   test_bateria (tests.test_peugeot206.Peugeot206) ... FAIL
   test_bieleta (tests.test_peugeot206.Peugeot206) ... FAIL
   test_cubiertas_traseras (tests.test_peugeot206.Peugeot206) ... FAIL
   test_pyday_formosa (tests.test_pyday_formosa.PyDayFormosa) ... ok
   test_pyday_asuncion (tests.test_pyday_asuncion.PyDayAsuncion) ... ok

   ======================================================================
   FAIL: test_bateria (tests.test_peugeot206.Peugeot206)
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "./test_peugeot206.py", line 71, in test_bateria
       self.assertGreaterThan(MONEY, 0)
   AssertionError: 'Not enought money'

   ======================================================================
   FAIL: test_vieleta (tests.test_peugeot206.Peugeot206)
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "./test_peugeot206.py", line 71, in test_vieleta
       self.assertGreaterThan(MONEY, 0)
   AssertionError: 'Not enought money'

   [...]

   ----------------------------------------------------------------------
   Ran 8 tests in 0.214s

   FAILED (failures=3)


Es por eso que hemos habilitado una nueva página de donaciones con el
objetivo de reparar los daños que ha estado sufriendo el auto en los
últimos meses. Si bien *errante*, nuestro auto estrella, no tiene
nada que esté **sumamente roto** hay algunas piezas que ya se *hacen
notar* y que requieren la atención de un mecánico. Estas piezas son:

* Batería ($ 1200)
* Bieleta ($ 250)
* Cubiertas traseras ($ 2200)
* Circuito eléctrico ($ 1500)
* Mano de obra ($ 850)

Eso da un total de $ 6000 (**USD 600**) [#]_, aproximadamente.

La **fecha límite** para realizar las donaciones es el **15 de Mayo de
2015** ya que cerca de esa fecha estamos dejando la Argentina (luego
del evento `SciPy Latinoamérica <http://scipyla.org/conf/2015/>`_) y
queremos aprovechar a hacer los arreglos allí para abaratar los
costos.

 *Todo el dinero recaudado* será utilizado para el mantenimiento del
 vehículo.

Como forma de agradecimiento personal y del proyecto
:doc:`argentina-en-python`, vamos a agregar tu nombre / empresa a la
:doc:`lista de colaboradores
<argentina-en-python/donaciones/colaboradores>` y si te parece
apropiado también pondremos el logo en esta página y el monto
donado. Además de un Tweet en la cuenta de `@argenpython
<http://twitter.com/argenpython/>`_ el día de la donación y
agradecimientos en un post que se escribirá luego de concluídos los
arreglos.

Al día de la fecha hemos recibido un total de *$ 0* en esta etapa de
donaciones.

.. raw:: html

  <div class="progress" style="height: 50px; width: 70%; margin-left: auto; margin-right: auto;">
    <div class="progress-bar progress-bar-success progress-bar-striped active" style="width: 20%">
      <span class="sr-only">0% Recibido</span>
    </div>
    <div class="progress-bar progress-bar-danger progress-bar-striped active" style="width: 10%">
      <span class="sr-only">100% Restante</span>
    </div>
  </div>

Hacé click en el siguite botón para enterarte sobre cuáles son los
medios disponibles a la fecha para realizar las donaciones:

.. raw:: html

   <div style="text-align: center">
     <a class="btn btn-large btn-primary" href="/pages/argentina-en-python/donaciones/medios/">
       Realizar donación
     </a>
   </div>

.. [#] :doc:`pydayasuncion-un-exito-arrollador`
.. [#] :doc:`pyday-formosa`
.. [#] :doc:`primer-sprint-de-python-en-resistencia-chaco`
.. [#] :doc:`charla-abierta-de-openstreetmap-en-las-brenas`
.. [#] :doc:`curso-de-python-en-parana`
.. [#] los precios están basados en los listados de Mercado Libre Argentina
