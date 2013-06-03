#
# mkhexdir.py
# create 00 - ff , 256 * 256 directories

import os
import time

l = list('0123456789abcdef')

def mkdir(deep, curDep = 0, fromDir = os.getcwd()):
    if curDep != deep:
        for i in l:
            for j in l:
                path = fromDir + '/' + i + j
                print('mkdir', path)
                os.mkdir(path)
                mkdir(deep, curDep + 1, path)

if __name__ == '__main__':
    time1 = time.time()
    mkdir(2)
    time2 = time.time()
    print('spend time:', time2 - time1)

