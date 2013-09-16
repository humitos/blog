import re
import glob

SEARCH_FOR = r'\[.*=.*\]'

for f in glob.glob('*.rst'):
    fd = open(f, 'r')
    content = fd.read()
    fd.close()
    if re.match(SEARCH_FOR, content):
        print f
        # import epdb;epdb.set_trace()
        # raw_input('Press a key...')
        # break
