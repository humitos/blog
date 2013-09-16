import os
import re
import glob
import shutil

from import_wordpress import CommandImportWordpress
xml_file = CommandImportWordpress.read_xml_file('/media/humitos/8c9aa144-b4eb-4c05-8ecb-3e6cb2213ef5/descargas/home-humitos-backup/Downloads/humitos.wordpress.2013-09-09.xml')

SEARCH_FOR = '[gallery '
REPLACE_RE = r'\[gallery.*ids="(\d{4},?)+"\]'
FIND_RE = r'(\d{4},?)+'
# \1 ids

REPLACE_CONTENT = r'''.. slides::\n\n    %s'''
FILES_PATH = '/srv/descargas/blog/nikola/files/posts'
OLD_FILES_PATH = '/home/humitos/blog/files'

for f in glob.glob('*.rst'):
    fd = open(f, 'r')
    content = fd.read()
    fd.close()
    if SEARCH_FOR in content:
        print f
        # import epdb;epdb.set_trace()
        # raw_input('Press a key...')
        ids = re.findall(FIND_RE, content)

        import pdb;pdb.set_trace()

        slides = '\n    '.join(ids)
        new_content = content.replace(gallery_text, REPLACE_CONTENT % slides)

        # fd = open(f, 'w')
        # fd.write(new_content)
        # fd.close()

        groups = re.search(REPLACE_RE, content).groups()
        os.mkdir(os.path.join(FILES_PATH, f[:-4]))
        source = os.path.join(
            OLD_FILES_PATH, groups[0], groups[1], groups[2])
        destination = os.path.join(FILES_PATH, f[:-4])

        if '?' in source:
            # remove: ?w=580
            source = source[:-6]

        shutil.copy(source, destination)

        break
