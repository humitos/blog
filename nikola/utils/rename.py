import glob
import shutil


for f in glob.glob('*.meta'):
    fopen = open(f, 'r')
    lines = fopen.readlines()
    fopen.close()
    # import epdb;epdb.set_trace()
    temp = lines[1][8:]
    lines[1] = temp
    fopen = open(f, 'w')
    fopen.writelines(lines)
    fopen.close()

    shutil.move(f, f[8:])
    shutil.move(f[:-4] + 'wp', f[8:-4] + 'wp')

