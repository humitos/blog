import difflib
import os


def get_files():
    return sorted([f for f in os.listdir() if f.startswith('argenpython.followers_')])


def get_date(filename):
    return filename[:-4].split('_')[1]


def get_diff(old, new):
    # Since Twitter API doesn't give as the followers list sorted, we
    # need to sorted it because if not there will be removed and added users
    # with the same name between 2 different files
    old_lines = sorted(open(old).readlines())
    new_lines = sorted(open(new).readlines())
    return ''.join(difflib.unified_diff(old_lines, new_lines))


def compare_files():
    files = get_files()
    olds = ['/dev/null'] + files[:-1]
    for old, new in zip(olds, files):
        print('Changes in', get_date(new))
        print(get_diff(old, new))

if __name__ == '__main__':
    compare_files()
