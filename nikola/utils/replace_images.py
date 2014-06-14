import os
import re
import glob
import shutil

# 8-9-16.rst:.. |image0| image:: http://humitos.files.wordpress.com/2011/02/p2050779.jpg


SEARCH_FOR = 'http://humitos.files.wordpress.com'
REPLACE_IMAGE_RE = r'(?P<image>\|image\d\d?\| image::) http://humitos.files.wordpress.com/\d{4}/\d{2}/(?P<filename>.*)(?P<size>\?.*)?'
REPLACE_TARGET_RE = r':target: http://humitos.files.wordpress.com/(\d{4})/(\d{2})/(.*)(\?.*)?'
# \1 year
# \2 month
# \3 filename

REPLACE_IMAGE_CONTENT = r'\g<image> \g<filename>' #' \g<size>'
TO_FILES_PATH = '/home/humitos/Source/blog/nikola/files/posts/wordpress'
FROM_FILES_PATH = '/home/humitos/Source/blog/nikola/utils/photos'

for f in glob.glob('*.rst'):
    fd = open(f, 'r')
    content = fd.read()
    fd.close()
    if SEARCH_FOR in content:
        print f
        # import epdb;epdb.set_trace()
        raw_input('Press a key...')
        new_content = re.sub(REPLACE_IMAGE_RE, REPLACE_IMAGE_CONTENT, content)
        # import ipdb;ipdb.set_trace()

        fd = open(f, 'w')
        fd.write(new_content)
        fd.close()

        groups = re.search(REPLACE_IMAGE_RE, content)
        if groups is None:
            continue

        groups = groups.groupdict()
        destination = os.path.join(TO_FILES_PATH, f[:-4])
        if not os.path.exists(destination):
            os.mkdir(destination)
        source = os.path.join(FROM_FILES_PATH, groups['filename'])

        if '?' in source:
            # remove: ?w=580
            source = source[:-6]

        shutil.copy(source, destination)

        break

    else:
        import ipdb;ipdb.set_trace()
