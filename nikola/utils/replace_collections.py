import os
import re
import csv
import glob
import shutil

SEARCH_FOR = '[gallery '
REPLACE_RE = '\\[gallery.*\n?.*\\]'
FIND_RE = r'ids="(.*)"'
# \1 ids

REPLACE_CONTENT = '''.. image:: %(image)s\n   :target: %(target)s\n   :height: 135px\n'''
OLD_FILES_PATH = '/media/humitos/Toshiba/backup-desktop/blog-wordpress-nikola/files'
FILES_PATH = '/home/humitos/blog/nikola/files'

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

        images = []
        for i in file_ids:
            year, month = re.search(r'(\d{4})/(\d{2})', i).groups()

            i = re.sub(r'(\d{4}/\d{2}/)', '', i.replace('http://humitos.files.wordpress.com/', ''))
            filename, ext = os.path.splitext(i)
            image = filename + '.thumbnail' + ext
            images.append(REPLACE_CONTENT % {'image': image, 'target': i})
            destination = os.path.join(FILES_PATH, 'posts', 'wordpress', f[:-4])
            source = os.path.join(OLD_FILES_PATH, year, month, i)
            if not os.path.exists(destination):
                os.mkdir(destination)
            shutil.copy(source, destination)

        images = '\n'.join(images)
        new_content = re.sub(REPLACE_RE, images, content)

        import ipdb;ipdb.set_trace()
        fd = open(f, 'w')
        fd.write(new_content)
        fd.close()

        break
