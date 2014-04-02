.. title: Dame contexto
.. slug: dame-contexto
.. date: 2014/04/02 13:14:49
.. tags: grep, terminal, consola, unix, software libre
.. link: 
.. description: 
.. type: text

`Acabo de encontrar`_ una opción hermosa del comando `grep` que hace
muchísimo tiempo hubiese querido saber pero sin embargo ni siquiera
había buscado: -C (-A -B)

.. _Acabo de encontrar: http://stackoverflow.com/questions/9081/grep-a-file-but-show-several-surrounding-lines

Estas opciones sirven para decirle a grep "Dame contexto", entonces,
en vez de mostrarte solo la línea que machea con tu búsqueda te
muestra `-A` después y `-B` antes o bien `-C` antes y después (si
querés usar el mismo valor)::

  $ grep -n -C 4 VCI hexdump.txt
  91978381-57b90180  b7 5e 59 9c be 6c 9f 7c  60 88 e9 b8 9f 71 db 00  |.^Y..l.|`....q..|
  91978382-57b90190  58 ff d5 55 67 9a f3 d5  ec cd 9f 4c 63 4c 0c 90  |X..Ug......LcL..|
  91978383-57b901a0  70 f3 45 27 a4 58 4b bb  ea 10 7c df 1e ab c6 f2  |p.E'.XK...|.....|
  91978384-57b901b0  9e a0 97 c7 3b 74 d8 8e  b3 ed 0b ca 13 1c 49 5e  |....;t........I^|
  91978385:57b901c0  92 d3 f1 03 2b 56 43 49  c2 d1 92 e8 d0 e6 bf e6  |....+VCI........|
  91978386-57b901d0  17 d3 a2 a1 23 d2 a4 7c  a4 95 bb 82 41 b8 fb e5  |....#..|....A...|
  91978387-57b901e0  18 a6 e1 f0 05 af da da  e1 ad b8 5f 01 b7 9e 6b  |..........._...k|
  91978388-57b901f0  4b 7f ae 37 9b f3 47 c1  35 95 f6 a7 21 93 5e 42  |K..7..G.5...!.^B|
  91978389-57b90200  e3 14 03 79 32 f6 5d 17  a7 b8 6e d5 18 5a ef 8f  |...y2.]...n..Z..|
  --
  92767082-58798f50  f0 14 3f 64 bb 08 42 28  d7 a3 42 5b 7d 55 3b 89  |..?d..B(..B[}U;.|
  92767083-58798f60  77 53 11 3d 62 ec 82 ee  e4 f9 00 30 f4 17 f3 14  |wS.=b......0....|
  92767084-58798f70  1f 68 d6 81 99 1d f1 ec  ff 00 fb 55 47 8f ad b3  |.h.........UG...|
  92767085-58798f80  68 ab 73 42 1f 2c 4a 2d  33 64 8f 7f 48 6e f7 44  |h.sB.,J-3d..Hn.D|
  92767086:58798f90  f5 8e 56 43 49 9c ec 0a  35 a9 fb a2 c3 a0 48 87  |..VCI...5.....H.|
  92767087-58798fa0  60 b6 6c ea a1 71 55 5e  d7 b9 97 4d 8a 6b 22 ec  |`.l..qU^...M.k".|
  92767088-58798fb0  3a 55 1e c2 4d b4 8a 11  f4 52 1e a6 c2 b2 7f 53  |:U..M....R.....S|
  92767089-58798fc0  13 16 c7 ca c0 ed 33 b1  bf bb b1 c9 c2 95 54 70  |......3.......Tp|
  92767090-58798fd0  5d 6e 5f c8 cc 1a 09 7d  3d f3 43 b3 42 d3 14 e1  |]n_....}=.C.B...|
  $

