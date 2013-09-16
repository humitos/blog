import os
import re
import glob
import shutil

SEARCH_FOR = 'http://humitos.files.wordpress.com'
REPLACE_IMAGE_RE = r'(\|image\d\| image::) http://humitos.files.wordpress.com/(\d{4})/(\d{2})/(.*)(\?.*)?'
REPLACE_TARGET_RE = r':target: http://humitos.files.wordpress.com/(\d{4})/(\d{2})/(.*)(\?.*)?'
# \1 year
# \2 month
# \3 filename

REPLACE_IMAGE_CONTENT = r'\1 \4'
TO_FILES_PATH = '/home/humitos/blog/nikola/files/posts/wordpress'
FROM_FILES_PATH = '/media/humitos/Toshiba/backup-desktop/blog-wordpress-nikola/files'

for f in glob.glob('*.rst'):
    fd = open(f, 'r')
    content = fd.read()
    fd.close()
    if SEARCH_FOR in content:
        print f
        # import epdb;epdb.set_trace()
        raw_input('Press a key...')
        new_content = re.sub(REPLACE_RE, REPLACE_CONTENT, content)
        import ipdb;ipdb.set_trace()

        fd = open(f, 'w')
        fd.write(new_content)
        fd.close()

        groups = re.search(REPLACE_RE, content).groups()
        destination = os.path.join(TO_FILES_PATH, f[:-4])
        os.mkdir(destination)
        source = os.path.join(
            FROM_FILES_PATH, groups[0], groups[1], groups[2])

        if '?' in source:
            # remove: ?w=580
            source = source[:-6]

        shutil.copy(source, destination)

        break
