#
# tail -f filename | grep string
# python3

import time

def tail(f):
    f.seek(0, 2)  # EOF
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def grep(lines, searchtext):
    for line in lines:
        if searchtext in line: yield line


if __name__ == '__main__':
    w = tail(open(u'/var/www/html/test.txt'))
    pylines = grep(w, 'python')
    for line in pylines:
        print(line)

