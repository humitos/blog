.. title: Jupyter, no me vuelvas loco
.. slug: jupyter-no-me-vuelvas-loco
.. date: 2016-03-26 12:15:33 UTC-03:00
.. tags: jupyter, python, cuenca, ecuador
.. category: 
.. link: 
.. description: 
.. type: text

Este es un post de mierda, pero que quizás te salve una par de horas
en caso de que tengas el mismo problema: "jupyter intenta utilizar un
binario de python que no existe más"

En algún momento de mi vida creé 2 virtual envs, uno con la versión de
2 de Python y otro con la 3 en los que instalé Jupyter. Luego de unos
cuantos meses, borré esos dos virtual envs y volví a crear uno solo
para python 3 en el que instalé Jupyer con pip.

.. code:: bash

   mkvirtualenv -p python3 jupyter
   pip install jupyter

Sin embargo, cuando ejecutaba `jupyter notebook` me daba un problema
de que no encontraba el binario::

  File "/home/humitos/.virtualenvs/j/lib/python3.4/site-packages/jupyter_client/manager.py", line 189, in _launch_kernel
    return launch_kernel(kernel_cmd, **kw)
  File "/home/humitos/.virtualenvs/j/lib/python3.4/site-packages/jupyter_client/launcher.py", line 123, in launch_kernel
    proc = Popen(cmd, **kwargs)
  File "/usr/lib/python3.4/subprocess.py", line 859, in __init__
    restore_signals, start_new_session)
  File "/usr/lib/python3.4/subprocess.py", line 1457, in _execute_child
    raise child_exception_type(errno_num, err_msg)
  FileNotFoundError: [Errno 2] No such file or directory: '/home/humitos/.virtualenvs/jupyter-py3/bin/python3'

Por algún motivo está buscando el binario de `python3` en un entorno
virtual llamado `jupyter-py3` (creado hace varios meses y borrado hace
unos momentos).

Luego de una tediosa búsqueda encontré un archivo
(`/home/humitos/.local/share/jupyter/kernels/python3/kernel.json`) en
una parte del caché de mi sistema con este contenido:

.. code:: json
	  
   {
       "language": "python",
       "argv": [
       "/home/humitos/.virtualenvs/jupyter-py3/bin/python3",
       "-m",
       "ipykernel",
       "-f",
       "{connection_file}"
       ],
       "display_name": "Python 3"
   }

¿Qué hice? Lo borré. Problema solucionado.
   
