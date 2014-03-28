.. link:
.. description:
.. tags: olpc, proyectos, software libre, sugar
.. date: 2012/03/19 21:16:34
.. title: Compile Sugar on Debian Testing (wheezy)
.. slug: compile-sugar-on-debian-testing-wheezy


.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/2012/03/19/compile-sugar-on-debian-testing-wheezy/


I've been trying to compile Sugar on Debian Testing since a week ago. I
chat with some guys on #sugar (irc.freenode.net) looking for help and
solving some bugs related with dependencies:
`#3364 <http://bugs.sugarlabs.org/ticket/3364>`__,
`#3365 <http://bugs.sugarlabs.org/ticket/3365>`__,
`#3370 <http://bugs.sugarlabs.org/ticket/3370>`__ and
`#3372 <http://bugs.sugarlabs.org/ticket/3372>`__.

After these two weeks, we found the solution to those issues and we
discover another ones. I was helped by **silbe** to compile Sugar on
Debian Testing. He helped me a lot fixing some missing dependencies that
I found and guiding me to the solution; telling me about what .log file
to take a look for example.

I think that Sugar has a blocking bar to start coding. I'm a developer,
I don't know too much about *jhbuild* and I think that I shouldn't fight
against it. Sometimes this blocking bar is sufficient to lost a good
developer that tries to collaborate but he can't cross that bar, so
maybe he goes for another project.

O.K., let's go to the really steps to compile Sugar on a Debian Testing
installation:

1. Download the *sugar-jhbuild* source code

::

    git clone git://git.sugarlabs.org/sugar-jhbuild/mainline.git sugar-jhbuild

2.  Update the sugar code

::

    cd sugar-jhbuild

    ./sugar-jhbuild update

3. Now, you need to check what dependencies are missing in your system

::

    ./sugar-jhbuild depscheck

4. Install all Debian packages listed bydepscheck command

::

    sudo apt-get install <all-packages-listed-by-depscheck>

NOTE:You need to `apply a
patch <http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=648724>`__ on
the *libgconf2-4* package. So, we have to download the libgconf source
package and apply that patch.

5. Download the source

::

    mkdir /tmp/src-libgconf2-4

    cd /tmp/src-libgconf2-4

    apt-get source libgconf2-4

6. Install building dependencies

::

    sudo apt-get build-dep libgconf2-4

6. Download and apply the patch

::

    cd gconf-3.2.3

    wget -c http://bugzilla-attachments.gnome.org/attachment.cgi?id=201398 -O gconf.patch

    git apply gconf.patch --verbose

7. Create the .deb packages

::

    dpkg-buildpackage -rfakeroot -b

    cd ..

8. Install .deb packages

::

    sudo dpkg -i *.deb

9. Build Sugar

::

    cd <your-sugar-jhbuild-directory>

    ./sugar-jhbuild build

10. Runsugar-emulator

::

    ./sugar-jhbuild run sugar-emulator

That's all! Two weeks of work summarized in one single post with 10
simple steps!!!

Yes! Now I can collaborate with this project. It's really interesting; I
was working some years ago on the OLPC project, and it was cool. This
time I found that the GUI and the activities grew a lot! I'm happy with
that.

Here are the references that I used to compile sugar:

-  http://wiki.sugarlabs.org/go/Development_Team/Jhbuild
-  https://wiki.sugarlabs.org/go/Development_Team/Jhbuild/Debian
-  http://ariejan.net/2008/05/04/how-to-compile-packages-on-debianubuntu-by-hand

