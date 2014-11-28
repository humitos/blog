# -*- coding: utf-8 -*-

"""Calculate a position from an IP or Address and save it into a file

Usage:
  geolocation.py [(-v | --verbose)] (-m | --me)
  geolocation.py [(-v | --verbose)] (-a | --address) [(-p | --previous-city)] <address>
  geolocation.py [(-v | --verbose)] (-s | --symlinks)
  geolocation.py (-h | --help)
  geolocation.py --version

Options:
  <address>            Address to be calculated.
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

from docopt import docopt
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('geolocation')

SYMLINKS_DIR = 'output/assets/data'
GPX_FILES = [
    'geodata/0-etapa.gpx',
    'geodata/primera-etapa.gpx',
    'geodata/segunda-etapa.gpx',
]
CITIES_FILENAME = 'geodata/cities.json'
MY_POSITION_FILENAME = 'geodata/my-position.json'
SYMLINK_FILES = [
    CITIES_FILENAME,
    MY_POSITION_FILENAME,
] + GPX_FILES
WAIT_BEFORE_QUERY = 5


def setup_logging(verbose):
    logfile = 'geodata/geolocation.log'
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


def setup_output(output):
    dirname = os.path.dirname(output)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    if not os.path.exists(output):
        # touch file with an empty dict
        with open(output, 'w') as fh:
            init = {
                'next': [],
                'previous': [],
            }
            fh.write(json.dumps(init))


def create_symlinks(dirname=SYMLINKS_DIR):
    logger.info('Creating symlinks...')
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
    logger.info('Place: %s, %s', response.city, response.state)

    logger.info('Saving file...')
    with open(output, 'w') as fh:
        fh.write(json.dumps(response.latlng))


def calc_address(address, when, output=CITIES_FILENAME):
    setup_output(output)

    logger.info('Querying the server for: "%s" ...', address)
    response = geocoder.osm(address)
    logger.info('Got an answer!')

    logger.info('Loading old cities from: %s', output)
    cities = json.loads(open(output, 'r').read().decode('utf8'))

    osm_id = response.json['osm_id']
    last_osm_id = None
    if cities[when]:
        last_osm_id = cities[when][-1]['osm_id']

    if not cities[when] or osm_id != last_osm_id:
        logger.info('Adding new city: "%s, %s, %s"',
                    response.city, response.state, response.country)
        cities[when].append(response.json)
        logger.info('Saving file...')
        with open(output, 'w') as fh:
            fh.write(json.dumps(cities, indent=4))
    else:
        logger.info('This city is already saved. Excluding...')


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Geolocation 0.1')

    setup_logging(arguments['--verbose'])
    if arguments['-a'] or arguments['--address']:
        address = arguments['<address>'].decode('utf8')

        if arguments['--previous-city']:
            when = 'previous'
        else:
            when = 'next'
        calc_address(address, when)

    if arguments['-m'] or arguments['--me']:
        calc_my_position()

    if arguments['--symlinks']:
        create_symlinks()

    create_symlinks()

    logger.info('Finished!')
