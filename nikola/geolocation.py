# -*- coding: utf-8 -*-

import os
import json
import time
import geocoder

filename = 'output/assets/js/points.json'

time.sleep(5)
response = geocoder.ip('me')

print('LatLng: {} - Place: {}, {}'.format(
    response.latlng,
    response.city,
    response.state,
))

points = []
if os.path.exists(filename):
    points = json.loads(open(filename, 'r').read())

current_position = {
    'lat': response.latlng[0],
    'lng': response.latlng[1]
}

if current_position not in points:
    points.insert(
        0,
        current_position
    )

with open(filename, 'w') as fh:
    fh.write(json.dumps(points, indent=4))
