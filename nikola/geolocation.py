# -*- coding: utf-8 -*-

"""Calculate a position from an IP or Address and save it into a file

Usage:
  geolocation.py [(-v | --verbose)] [--no-wait] (-m | --me)
  geolocation.py [(-v | --verbose)] (-a | --address) [(-r | --remove)] [(-p | --previous-city)] <address>
  geolocation.py [(-v | --verbose)] (-s | --symlinks)
  geolocation.py (-h | --help)
  geolocation.py --version

Options:
  <address>            Address to be calculated.
  -r --remove          Remove this point from the json file.
  -p --previous-city   Save the calculated point into the previous cities file.
  -s --symlinks        Create symlinks in output directory to upload on deploy.
  -h --help            Show this screen.
  -v --verbose         Show the log in the standard output.
  --version            Show version.
"""

import os
import json
import time
import geocoder
import logging
import collections

from docopt import docopt
from logging.handlers import RotatingFileHandler


logger = logging.getLogger('geolocation')

DIRNAME = os.path.dirname(os.path.abspath(__file__))
SYMLINKS_DIR = os.path.join(DIRNAME, 'output/assets/data')
GPX_FILES = [
    os.path.join(DIRNAME, 'geodata/0-etapa.gpx'),
    os.path.join(DIRNAME, 'geodata/primera-etapa.gpx'),
    os.path.join(DIRNAME, 'geodata/segunda-etapa.gpx'),
]
CITIES_FILENAME = os.path.join(DIRNAME, 'geodata/cities.json')
MY_POSITION_FILENAME = os.path.join(DIRNAME, 'geodata/my-position.json')
SYMLINK_FILES = [
    CITIES_FILENAME,
    MY_POSITION_FILENAME,
] + GPX_FILES
WAIT_BEFORE_QUERY = 5
MAP_ZOOM = 14


def setup_logging(verbose):
    logfile = os.path.join(DIRNAME, 'geodata/geolocation.log')
    handler = RotatingFileHandler(logfile, maxBytes=1e6, backupCount=10)
    logger.addHandler(handler)
    formatter = logging.Formatter("%(asctime)s  %(name)-10s  "
                                  "%(levelname)-8s %(message)s")
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)

    if verbose:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)


def save_json(data, output):
    logger.info('Saving file...')
    with open(output, 'w') as fh:
        data = json.dumps(
            data,
            indent=4,
            sort_keys=True
        )
        fh.write(data)


def load_json(output):
    data = open(output, 'r').read().decode('utf8')
    cities = json.loads(
        data,
        object_pairs_hook=collections.OrderedDict
    )
    return cities


def setup_output(output):
    dirname = os.path.dirname(output)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    if not os.path.exists(output):
        # touch file with an empty dict
        init = {
            'next': [],
            'previous': [],
        }
        save_json(init, output)


def osmurl_invalid():
    logger.info('The URL is not correct. Quitting...')


def is_osmurl_valid(response):
    url = 'http://www.openstreetmap.org/#map={zoom}/{lat}/{lng}'.format(
        zoom=MAP_ZOOM,
        lat=response.lat,
        lng=response.lng,
    )
    logger.info('OSMUrl: %s', url)
    answer = None
    while answer not in ('y', 'yes', 'n', 'no'):
        answer = raw_input('Is this URL correct?\n    {}\n[y/n]: '.format(url))
    if answer in ('y', 'yes'):
        return True
    return False


def create_symlinks(dirname=SYMLINKS_DIR):
    if not os.path.exists(dirname):
        logger.info('Creating directory: %s', dirname)
        os.makedirs(dirname)

    def get_output_path(filename):
        return os.path.join(
            dirname,
            os.path.basename(filename)
        )

    def get_abs_path(filename):
        return os.path.abspath(filename)

    for filename in SYMLINK_FILES:
        destination = get_output_path(filename)
        if not os.path.exists(destination):
            source = get_abs_path(filename)
            logger.info('Creating symlink: %s', destination)
            os.symlink(source, destination)


def calc_my_position(output=MY_POSITION_FILENAME):
    setup_output(output)

    logger.info('Waiting %s seconds...', WAIT_BEFORE_QUERY)
    time.sleep(WAIT_BEFORE_QUERY)
    logger.info('Querying the server about my ip...')
    response = geocoder.ip('me')
    logger.info('LatLng: %s', response.latlng)
    logger.info('Place: %s', response.address)

    logger.info('Querying the server about "%s"...', response.address)
    response = geocoder.osm(response.address)
    logger.info('LatLng: %s', response.latlng)
    logger.info('Place: %s', response.address)

    # if not is_osmurl_valid(response):
    #     osmurl_invalid()
    #     return

    save_json(response.latlng, output)

    command = 'scp {} ' \
              'mkaufmann.com.ar:~/apps/blog.mkaufmann.com.ar/blog/' \
              'nikola/output/assets/data/'.format(
                  os.path.join(DIRNAME, 'geodata/my-position.json'),
              )

    logger.debug(command)
    logger.info('Uploading new "my-position.json" file...')
    os.system(command)
    logger.info('Upload Finished!')

    return response


def calc_address(address, when, output=CITIES_FILENAME):
    setup_output(output)

    logger.info('Querying the server for: "%s" ...', address)
    response = geocoder.osm(address)
    logger.info('Got an answer!')

    if not is_osmurl_valid(response):
        osmurl_invalid()
        return

    logger.info('Loading old cities from: %s', output)
    cities = load_json(output)

    osm_id = response.json['osm_id']
    last_osm_id = None
    if cities[when]:
        last_osm_id = cities[when][-1]['osm_id']

    if not cities[when] or osm_id != last_osm_id:
        logger.info('Adding new city: "%s"', response.address)
        cities[when].append(response.json)
        save_json(cities, output)
    else:
        logger.info('This city is already saved. Excluding...')

    return response


def remove_address(address, output=CITIES_FILENAME):
    logger.info('Querying the server for: "%s" ...', address)
    response = geocoder.osm(address)
    logger.info('Got an answer!')
    logger.info('Place: %s', response.address)

    logger.info('Loading old cities from: %s', output)
    cities = load_json(output)

    removed = False
    next_cities = cities['next']
    for city in next_cities:
        if city['osm_id'] == response.json['osm_id']:
            logger.info('City: %s removed!', city['address'])
            next_cities.remove(city)
            removed = True
            break

    if removed:
        save_json(cities, output)
    else:
        logger.info('City not found!')

    return response


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Geolocation 0.1')

    setup_logging(arguments['--verbose'])
    if arguments['--no-wait']:
        WAIT_BEFORE_QUERY = 0

    if arguments['-a'] or arguments['--address']:
        q = arguments['<address>'].decode('utf8')

        if arguments['--remove']:
            response = remove_address(q)
        else:
            if arguments['--previous-city']:
                when = 'previous'
            else:
                when = 'next'
            calc_address(q, when)

    if arguments['-m'] or arguments['--me']:
        calc_my_position()

    if arguments['--symlinks']:
        create_symlinks()

    create_symlinks()

    logger.info('Finished!')
