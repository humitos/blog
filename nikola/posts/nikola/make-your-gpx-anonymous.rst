.. title: Make your GPX anonymous
.. slug: make-your-gpx-anonymous
.. date: 2015-06-21 19:26:54 UTC-03:00
.. tags: openstreetmap, mapa, software, comando
.. category: 
.. link: 
.. description: 
.. type: text

Sometimes I want to make my .gpx files anonymous because it's data
that I recover by myself using OSMTracker for Android and I don't want
the whole world knows when I was there.

Yeah, maybe I'm a bit crazy. Nice to meet you ;)

Today, I found [#]_ a real simple solution for this: `xmlstarlet`

Once you have it installed, you can excecute:

.. code:: bash

   xmlstarlet ed \
      -P \
      -N x=http://www.topografix.com/GPX/1/1 \
      -u '//x:time' \
      -v 1970-01-01T00:00:00Z \
      input.gpx > output-nulltime.gpx

And what will put `1970-01-01T00:00:00Z` on all the `<time>` tags.

That's all! Now, they ready to be uploaded to the OSM community and
nobody will know where you was there :)

.. [#] https://help.openstreetmap.org/questions/2130/gpx-file-no-time-tag
