.. link: 
.. description: 
.. tags: software libre, windows
.. date: 2013/09/20 18:00:09
.. title: Solución Windows a: "No más mate frío"
.. slug: solucion-windows-a-no-mas-mate-frio

Hoy `Diego Mernes posteó`_ en su Facebook:

    la cagada de tomar mate solo es que si te distraés por unos minutos, no hay
    nadie que te recuerde que estás cebando, y se enfría al toque... una
    cagada... debería venir un muñequito que te pida un mate cada 3 minutos...
    ¿algún ingeniero que lo haga? yo lo compro!

Y me hizo reír porque yo ya había pasado por la misma sensación y, como lo
había resulto, lo había publicado. Fue muy gracioso pensar que `la publicación
de semejante pelotudés`_ le haya servido a otra persona para resolver "un
problema". Que, aunque creas que no es muy grave, produce diarrea (por lo
menos, a mí)

Entonces, le pasé el link a mi post y él hizo la solución Windows al problema
del mate cada 3 minutos. Es muy, pero muy loco que hayamos pensado los dos que
tenía que ser cada 3 minutos. ¿Porqué no dijo 4? ¿o 3.5?, no sé, otro número.

Acá su solución en PowerShell:

.. code:: bash

    while ($true) {start-sleep -s 180; (New-Object -ComObject SAPI.SPVoice).Speak("mate")}

.. _Diego Mernes posteó: https://www.facebook.com/diego.mernes/posts/10201319350178999
.. _la publicación de semejante pelotudés: http://blog.mkaufmann.com.ar/posts/wordpress/no-mas-mate-frio/
