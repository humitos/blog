import os
import glob


CONTENT = '''.. link:
.. description:
.. tags: %(tags)s
.. date: %(date)s
.. title: %(title)s
.. slug: %(slug)s

'''

for f in glob.glob('*.meta'):
    print f
    fd = open(f, 'r')
    fd_content = fd.readlines()
    # print fd_content
    fd.close()

    title = fd_content[0].strip()

    slug = fd_content[1].strip()
    date = fd_content[2].replace('-', '/').strip()
    tags = ', '.join(fd_content[3].split(',')).strip()

    rst_content = CONTENT % {'title': title,
                             'tags': tags,
                             'slug': slug,
                             'date': date}

    rst_filename = os.path.join('migrated', slug + '.rst')
    fd = open(rst_filename, 'r')
    content = fd.readlines()
    first_line = content[0]
    fd.close()

    if '.. link:' in first_line:
        print 'SKIP:', f
        continue
    else:
        fd = open(rst_filename, 'w')
        rst_content += ''.join(content)
        fd.write(rst_content)
        fd.close()
        # break
