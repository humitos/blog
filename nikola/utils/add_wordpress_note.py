#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script adds a note to every WordPress post, so the user
# can see it in the original version if there is an issue with its
# visualization.

import glob

NOTE = \
'''
.. note::

   Este post no es el original, sino una migración de Wordpress a
   Nikola. Si no se visualiza correctamente, podés ir al original (en
   Wordpress) haciendo click aquí_

.. _aquí: http://humitos.wordpress.com/%(date)s/%(slug)s/


'''

for fn in glob.glob('*.rst'):
    new_content = []
    with open(fn, 'r') as fh:
        date = ''
        slug = ''
        first_n_line = False
        for line in fh.readlines():
            new_content.append(line)
            if line == '\n' and not first_n_line:
                first_n_line = True
                new_content.append(NOTE % dict(date=date, slug=slug))
            elif line.startswith('.. slug:'):
                slug = line.replace('.. slug: ', '')[:-1]
            elif line.startswith('.. date:'):
                date = line.split(' ')[2]

        # print ''.join(new_content)

    with open(fn, 'w') as fh:
        fh.write(''.join(new_content))
