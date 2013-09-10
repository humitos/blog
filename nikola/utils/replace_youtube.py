import re
import glob

SEARCH_FOR = '[youtube='
REPLACE_RE = r'\[youtube=(.*)\]'
REPLACE_CONTENT = r'.. media:: \1'

for f in glob.glob('*.rst'):
    fd = open(f, 'r')
    content = fd.read()
    fd.close()
    if SEARCH_FOR in content:
        print f
        # import epdb;epdb.set_trace()
        # raw_input('Press a key...')
        new_content = re.sub(REPLACE_RE, REPLACE_CONTENT, content)
        fd = open(f, 'w')
        fd.write(new_content)
        fd.close()
        # break
