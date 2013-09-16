import os
import re
import csv
import glob
import shutil

SEARCH_FOR = '[gallery '
REPLACE_RE = r'\[gallery.*\]'
FIND_RE = r'ids="(.*)"'
# \1 ids

REPLACE_CONTENT = r'''.. slides::\n\n    %s'''
OLD_FILES_PATH = '/media/humitos/Toshiba/backup-desktop/blog-wordpress-nikola/files'
FILES_PATH = '/home/humitos/blog/files'

csvf = '/home/humitos/blog/nikola/utils/attachments_ids.csv'
idsf = csv.reader(open(csvf, 'r'), delimiter=',')
IDS = {}
for i in idsf:
    IDS[i[0]] = i[1]


for f in glob.glob('*.rst'):
    fd = open(f, 'r')
    content = fd.read()
    fd.close()
    if SEARCH_FOR in content:
        print f
        # import epdb;epdb.set_trace()
        # raw_input('Press a key...')
        ids = re.findall(FIND_RE, content)[0].split(',')
        file_ids = [IDS[i] for i in ids]


        slides = '\n    '.join(file_ids)
        new_content = re.sub(content, REPLACE_RE, REPLACE_CONTENT % slides, re.MULTILINE)

        import ipdb;ipdb.set_trace()
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
