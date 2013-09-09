.. link:
.. description:
.. tags: facultad
.. date: 2008/06/04 21:36:24
.. title: Una "discusión" sobre un parcial
.. slug: una-discusion-sobre-un-parcial

Primero como para ponernos en órbita, explico de qué se trata esto. Ayer
(Martes) rendí el primer y único parcial de **Gestión de datos**. No
pude estudiar mucho por algunas cuestiones personales en cuanto a
discrepancia con los docentes de la materia y no tenía mucho ánimo. Por
suerte algo de SQL sabía porque lo había estudiado por mi cuenta en otra
oportunidad.

Luego de salir del parcial, me fui contento a mi casa porque me había
ido, a mi modo de ver las cosas: *bastante bien*. Como siempre, esto no
quiere decir que apruebe ni nada por el estilo, y mucho menos si
considero la *bronca* que me tienen los docentes por hacer preguntas en
clases.

Dejando de lado todo esto, hoy tuve clase de práctica y un amigo me
preguntó algo sobre un ejercicio que me hizo poner en duda. Aproveché y
le pregunté a la profesora sobre esto. Escribo abajo el diálogo completo
(transcripción que realicé desde un OGG).

Pero antes, explico más o menos como era el enunciado del problema.
Había un diagrama entidad-relación el cuál nosotros teníamos que pasar a
tablas SQL pero sin escribir las sentencias **CREATE TABLE** y demás.
Sino que con algunos dibujos y explicando cuales eran claves primarias y
foráneas estaba bien. El diagrama era como este (lo único que le falta
son algunos atributos a foto que no recuerdo, pero es para mostrar la
idea):

|image0|

El enunciado decía más o menos así: "Un usuario puede tener 0 o n fotos
y una foto puede tener como máximo un dueño. Además un usuario puede
tener n cuentas de email. NOTA: **cant_fotos** es un atributo
calculable."

Yo hice tres tablas, una para *Usuario,* otra para *Foto* y otra
*Usuario_Email* en la que indicaba el email y el usuario, de modo que
pueda tener muchos emails un mismo usuario. En ningún lado puse
*cant_fotos* ya que en el enunciado decía que era un atributo
calculable. Aunque antes de leerlo igualmente pensaba que no debería
estar ya que sale con un **SELECT COUNT**. Asique no lo puse en ningún
lado. Ahora viene lo que hablamos con la profesora hoy. El primero que
hablar ("A") es un amigo, y luego paso a ser yo ("M"). "P" es la
profesora:

    A: En la que teníamos que armar las tablas: a mí me quedaron tres,
    Usuario, Correo y Foto. Además había un atributo que era calculable.

    P: Si, eso es porque estaba en el modelo.

    A: Claro, yo no lo puse en ninguna tabla.

    P: No, pero eso tiene que estar en la tabla Usuario.

    A: ¿Tiene que estar?

    P: Si obvio.

    A: Pero si se puede calcular.

    P: El contenido después lo verán, se supone que si lo estás haciendo
    en la vida real el contenido lo calcularás por código o lo que sea.
    ¿Pero dónde lo vas a almacenar? Tenés que tener creado el campo
    dentro de la tabla.

    M: Pero eso se calcula desde la tabla de fotos. Hacés un SELECT
    COUNT de la tabla de fotos y sabés cuantas fotos tiene ese usuario.
    No es necesario guardarlo.

    P: Bueno, está bien. Lo óptimo sería no guardarlo, sino que ir
    calculando e ir mostrándolo. Sino que así como estaba en el modelo
    se necesitaba tener ese atributo en la tabla.

    M: ¿Porqué? No entiendo...

    P: Y porque es un atributo de Usuario. Después el contenido lo vas
    calculando y, osea, lo que se entiende es que si está en el modelo
    es porque se necesita tenerlo almacenado en algún lado, entonces lo
    almacenás como un atributo en la tabla de Usuario. Igual, si no lo
    pusieron se les bajará unos puntitos nada más. Osea, sólo por no
    haber puesto el atributo N-Fotos no van a salir mal.

    M: No, está bien, no es la cuestión salir bien o salir mal. El tema
    es que no entiendo porqué está mal no ponerlo, a eso me refiero. Si
    justamente el enunciado decía "el atributo es calculable"

    P: Si, en realidad en el enunciado estaba como una aclaración para
    que no pregunten "¿Qué es ese atributo que esta con líneas
    puntadas?" Puede ser que eso los confundió digamos y que pensaban
    que había que hacer algo o no almacenarlos.

    M: Es que está almacenado, porque si vos sabés cuantas fotos hay en
    la base de datos, ese atributo ya lo tenés. A eso es lo que voy yo.

    P: Sí, pero cuando vos hacés el cálculo lo obtenés.

    M: Claro, de hecho si lo guardás puede quedar inconsistente la base
    de datos porque te quedan 5 fotos y tiene 10.

    P: Está bien, y es así como vos me decís. De hecho puede ser que no
    esté el atributo en la vida real y no lo tengas que guardar, pero en
    este caso del modelo sí porque aparecía. Si no fuese necesario
    diréctamente no aparece en el modelo y por código lo obtenés. Y
    listo.

    M: Bueno, entonces que sea calculable y que no sea calculable es
    indistinto.

    P: Si, en este caso es lo mismo.

    M: No puede ser.

    P: ¿Cómo que no? Cuando nosotros hicimos la guía había cosas que te
    pedía la guia y que en modelo no se reflejaban. Bueno en este caso
    es al revés, si estaba en el modelo era porque después al
    transformarlo lo ponías como un atributo en tu tabla. Igualmente
    todo es discutible, cuando después vos empieces a trabajar podés ir
    a preguntarle al usuario que te está mandando hacer el trabajo si lo
    va a querer tener almacenado o no. Y le vas a decir que no hace
    falta porque lo vas a poder calcular y lo podés hacer por código,
    etc etc... Y seguramente no lo vas a tener. En este caso del modelo
    si.

*... me imagino preguntándole al cliente: "Señor, ¿Quiere que guarde el
atributo X o lo calculamos al momento de mostrarlo? ¿Usted que
opina?"...*

.. |image0| image:: http://img242.imageshack.us/img242/9770/parcialnv9.png
