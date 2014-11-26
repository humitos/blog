.. link: 
.. description: 
.. tags: icaro, pic, python, robótica
.. date: 2013/11/18 11:30:40
.. title: Instalar ICARO en Ubuntu
.. slug: instalar-icaro-en-ubuntu

ICARO_ es una "plataforma" para experimentar y crear robots de forma
sencilla destinada a estudiantes. Hace aproximadamente 2 semanas que
estoy investigando como funciona su placa y me encontré con que está
demasiada muy buena.

Entonces, como me encontré con que superó mis espectativas
ampliamentes, decidí escribir un post para comentar cómo es la
instalación de ICARO en Ubuntu ya que es un inconveniente no tan fácil
de resolver sin un poco de conocimiento en el tema.

1. Instalar los paquetes necesarios desde los repositorios oficiales::

    sudo apt-get install python-pygame python-rsvg python-usb \
    python-webkit python-serial python-gtk python-cairo \
    python-gtksourceview2

2. Instalar `sdcc` y `sdcc-libraries` desde los repositorios de
**lucid** ya que necesitamos versiones viejas de esos paquetes porque
en las nuevas han quitado el archivo
`/usr/share/sdcc/lib/pic16/libm18f.lib` por problemas de licencias
(creo) y es fundamental para trabajar con ICARO.

* Agregar la siguiente línea al archivo `/etc/apt/sources.list`::

   deb http://cz.archive.ubuntu.com/ubuntu lucid main universe

* Luego, instalar los paquetes que necesitamos::

   sudo apt-get update
   sudo apt-get install sdcc-libraries=2.9.0-5 sdcc=2.9.0-5

3. Bajar el código fuente de github::

    git clone https://github.com/valentinbasel/icaro.git

4. Cambiar el nombre del ejecutable de `sdcc-sdcc` a `sdcc` en el
archivo `config.dat` que está dentro del repositorio (es la primera
línea del archivo).

5. Copiar el Firmware desde el repositorio para trabajar con PICs::

    cd icaro
    sudo mkdir /usr/share/icaro
    sudo cp -r pic16 /usr/share/icaro

6. Copiar reglas UDEV desde el repositorio para el manejo de los
grupos y permisos para escribir en el puerto USB de la placa::

    cd icaro
    sudo cp udev/* /etc/udev/rules.d/

7. Agregar tu usuario a los grupos `dialout` y `microchip`::

    sudo usermod -a -G dialout $USER
    sudo usermod -a -G microchip $USER 

8. Modificar la línea de `main.py`:

.. code:: diff

    diff --git a/main.py b/main.py
    index efe5794..533629a 100644
    --- a/main.py
    +++ b/main.py

    @@ -204,7 +204,7 @@ def comprobacion_errores(ventana):
                 #tar=tarfile.open(dir_conf+"/np05.tar.gz","r:gz")
                 #tar.extractall(dir_conf)
                 #tar.close
    -            shutil.copytree("/usr/share/icaro/pic16/np05",dir_conf+"/firmware/")
    +            shutil.copytree("pic16/np05",dir_conf+"/firmware/")
             except:
                 ventana.mensajes(2,"no se pudo copiar el directorio")
                 exit()

9. ICARO ya está configurado y listo para ser ejecutado mediante::

    python main.py

Eso es todo por ahora, espero resolver varios dolores de cabeza a la
gente que tiene ganas de experimentar con esta placa y está renegando
para instalarlo en Ubuntu/Debian/Huayra y/o derivados.

Además, para que con cada actualización del sistema ICARO me siga
funcionando, "pinié" los paquetes `sdcc` y `sdcc-libraries` para que
no sean actualizados y así no perder las librerías que
necesitamos. Para eso, agregué estas líneas al archivo `/etc/apt/preferences`::

  Package: sdcc-libraries
  Pin: version 2.9.0-5
  Pin-Priority: 555

  Package: sdcc
  Pin: version 2.9.0-5
  Pin-Priority: 555

.. note::

   Si encontrás algo que me esté faltando en la explicación, por
   favor, comunicámelo por email o en los comentarios así actualizo el
   post.

.. _ICARO: http://roboticaro.org/
