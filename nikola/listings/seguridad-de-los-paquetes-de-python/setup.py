# THIS IS JUST AN EXAMPLE OF A 'SECURITY ISSUE' THAT I FOUND (AT
# LEAST, I THINK IT IS) OF THE PYTHON EGG SYSTEM WHEN YOU TRY TO
# INSTALL SOMETHING INSIDE THE SYSTEM USING ROOT PRIVILEGES (INSTEAD
# UNDER A VIRTUALENV)

import os

from distutils.core import setup

# THIS FUNCTION COULD BE ANYTHING YOU WANT, MAYBE 'rm -rf /' OR 'cat
# ~/.ssh/id_rsa' AND SEND THEM THROUGH EMAIL OR WHATEVER. I THINK IT'S
# REALLY DANGEROUS TO RUN A 'sudo python setup.py install' FROM
# PACKAGES DOWNLOADED FROM PYPI THAT EVERYONE HAS ACCESS TO UPLOAD A
# NEW PYTHON PACKAGE. AT LEAST, IT CALLED MY ATTENTION.
os.system('rm /tmp/sudo.file')


setup(
    name='fake-package',
    version='0.1',
    description='Delete files that are protected by root permissions',
    author='Manuel Kaufmann',
    author_email='humitos@gmail.com',
    keywords=['root', 'delete', 'everything'],
    classifiers=[],
)
