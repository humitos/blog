.. link:
.. description:
.. tags: inglés, internet, olpc, python, software libre, trabajo
.. date: 2012/05/24 20:09:18
.. title: How do you work every single day with your XO?
.. slug: how-do-you-work-every-single-day-with-your-xo

Have you ever had to type all day long on your XO to test different
things? How many times did you get frustrated because of its keyboard,
trying to press the correct letter with your *big*\ finger? How many USB
keyboards and mouses did you buy to solve this?

O.K. Today I found the most cheap and easy solution for this: using your
habitual keyboard and mouse to control both. Yes, that's it. Use the
same PC that you use to fix bugs, to run sugar-jhbuild and more. There
are two or three steps that you have to follow.

First of all, we have to install the necessary package to share the
keyboard and mouse on our normal PC and the following ones will be done
in the XO. The name of the package is: \ **x2x**. So, as I'm in Debian I
have to run:

    sudo apt-get install x2x

Now, we should connect to our habitual pc:

    ssh -X «youruser»@«ip-habitual-pc»

And the final step is... the secret command:

    DISPLAY=:0 x2x -to \`echo $DISPLAY\` -west

Peace of cake! Isn't it? I used \ **-west** here because I have the XO
at the left of my habitual PC, but in the other case you should
use \ **-east**. So, after doing these steps you could control both
computers with the same keyboard and mouse and testing will be more than
easy.

|image0|

Reference:

-  http://wiki.laptop.org/go/Ssh_into_the_XO

.. |image0| image:: http://humitos.files.wordpress.com/2012/05/dsc_3196.jpg
   :target: http://humitos.files.wordpress.com/2012/05/dsc_3196.jpg
