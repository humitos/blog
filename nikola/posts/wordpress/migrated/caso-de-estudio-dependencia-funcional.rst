.. link:
.. description:
.. tags: facultad
.. date: 2008/04/30 21:17:35
.. title: Caso de estudio: "Dependencia Funcional"
.. slug: caso-de-estudio-dependencia-funcional

Hoy fui a la facultad a la materia Gestión de Datos e hicimos un
ejercicio de la guía de actividades prácticas. Estamos dando el tema
"Dependencia funcional y normalización". El enunciado es este:

*Se desea construir una BD para gestionar la información de los
electores en un censo electoral con los siguientes supuestos
semánticos:*

-  Un elector es identificado por su DNI (D). Todos los electores tienen
   DNI. Un elector tiene un nombre (N), fecha de nacimiento (F) y sexo
   (S)
-  Un municipio se identifica por la provincia a la que pertenece (P) y
   su código de municipio (C). No pueden existir dos municipios con
   igual código en la misma provincia.
-  Dos municipios pueden tener el mismo nombre (B) pero sólo si
   pertenecen a provincias diferentes
-  Una mesa está identificada por su municipio, número de distrito (T),
   número de sección (NS) y número de mesa (M). Los números de distrito
   se pueden repetir para municipios diferentes pero no dentro del mismo
   municipio. Igual ocurre con los números de sección respecto de los
   distritos y con los números de mesa respecto de las secciones.
-  Un elector está inscrito en una mesa, incluida en una sección, a su
   vez incluida en un distrito, que a su vez pertenece a un municipio.
-  Un elector tiene una dirección, es decir, una calle (L) y un número
   de calle (E).
-  Todos los electores que residen en la misma calle del mismo municipio
   están inscritos en la misma sección, aunque pueden estar en mesas
   diferentes según el número de la calle.

Se pide:

#. Realizar un modelo de tablas que represente la BD a ser utilizada por
   el sistema tratando de minimizar la cantidad de tablas.
#. Llevar el modelo anterior a la tercera forma normal (3FN).

Sinceramente yo no tenía ni idea como arrancar, esto lo dimos en la
clase de teoría hace dos semanas creo y no me acordaba nada, asique
agarré el libro y me puse a leer. Termino de leer la primer forma
normal, comienzo a hacerlo, y la profesora explica como resolverlo.
Escuho, atiendo, y me pongo a resolverlo de la forma que explicó. Me
quedó así:

-  DNI(D) **->**\ Nombre(N), Fecha de nacimiento(F), Sexo(S)
-  Calle(L), Provincia(P), Código(C) **->** Número de sección(NS)
-  Provincia(P), Código(C), Calle(L), Número de calle(E), Número de
   sección(NS), Número de distrito(T) **->** Número de mesa(M)
-  Provincia(P), Código(C) **->**\ Nombre(B)
-  DNI(D) **->**\ Número de sección(NS)
-  DNI(D) **->**\ Calle(L), Número de calle(E)

Justo cuando terminamos de hacer esto, la profesora empieza a
desarrollarlo en el pizarrón y agrega una dependencia funcional que
nosotros no teníamos:

-  DNI(D) **->** Nombre(N), Fecha de nacimiento(F), Sexo(S), Calle(L),
   Provincia(P), Código(C), Número de sección(NS), Número de calle(E),
   Número de distrito(T), Número de mesa(M), Nombre(B)

Resumiendo, el DNI determina todos los otros campos. Con los chicos que
lo estaba haciendo empezamos buscar a ver si se nos había pasado un
axioma en dónde podía llegar a estar dicha relación, aunque sin éxito,
no la encontramos. Uno de nosotros pregunta:

-  **Alumno:** "¿Porqué DNI determina Provincia(P) y Código(C)? Por
   ejemplo"
-  **Profesora:** "Mmm... No sé como explicártelo, creo que se deduce
   del enunciado, es como en la vida, vos sabés dónde votas con tu DNI.
   Osea, podés saber todos los datos de tu mesa"

En ese momento, sinceramente, no podía creer lo que nos estaba diciendo:
"No sé como explicártelo" y además, "Creo que se deduce del enunciado".
Supongo que si hay un enunciado de un problema es para que lo respetemos
y que no queden cosas que **se sobre entienden**, porque justamente esto
es lo que trae consigo muchos problemas a la hora de interpretar algo.

Igualmente, me quedó picando y capaz que tenga razón, que se deduzca del
enunciado porque existen las reglas de Armstrong con las cuales se
pueden inferir en otras dependencias funcionales. Asique cuando llegué a
mi casa me puse a leer éstas reglas y a ver si llegaba a la respuesta de
la profesora. Estas son las reglas:

-  **Reflexividad:** si B es subconjunto de A, entonces A\ **->**\ B
-  **Aumento:** si A\ **->**\ B, entonces AC\ **->**\ BC
-  **Transitividad:** si A\ **->**\ B y B\ **->**\ C, entonces
   A\ **->**\ C

De estas tres reglas se pueden deducir otras tres más:

-  **Descomposición o proyección:** si A\ **->**\ BC, entonces
   A\ **->**\ B y A\ **->**\ C
-  **Unión o adición:** si A\ **->**\ B y B\ **->**\ C, entonces
   A\ **->**\ BC
-  **Pseudo-Transitividad:** A\ **->**\ B y DB\ **->**\ E, entonces
   AD\ **->**\ E

La que acabo de encontrar (es la primera vez que lo hago realmente) es
esta:

-  Por **Unión**: DNI(D) **->** Nombre(N), Fecha de nacimiento(F),
   Sexo(S), Calle(L), Número de calle(E), Número de sección(NS).

En ningún lado veo que exista la dependecia de Provincia(P) y Código(C)
con DNI(D). Por lo tanto no entiendo de dónde está sacando que sabiendo
el DNI de un persona se puede saber la Mesa(M) en cuál vota o la
Provincia(P) en la cual vive. Por lo tanto el resto del ejercicio por
supuesto que lo tenía todo mal hecho ya que yo trabajé **sobre la base
de datos del enunciado** y ella trabajó sobre **la de la vida misma**
