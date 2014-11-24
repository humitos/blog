import time
import geocoder

time.sleep(5)
response = geocoder.ip('me')

print('LatLng: {} - Place: {}, {}'.format(
    response.latlng,
    response.city,
    response.state,
))

with open('output/assets/js/point.json', 'w') as fh:
    fh.write(str(response.latlng))
