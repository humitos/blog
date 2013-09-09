import glob

for f in glob.glob('*.rst'):
    print f
    fd = open(f, 'r')
    fd_content = fd.read()
    fd.close()

    fd = open(f, 'w')
    new_content = fd_content.replace('\\_', '_')
    fd.write(new_content)
    fd.close()
