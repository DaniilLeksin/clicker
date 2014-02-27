__author__ = 'daniil leksin'

import sys

from t_22614reproduct.test_22614reproduct import reproduction
from t_22614detect.test_22614detect import detection

def clear():
    open('c:/Temp/detection.txt', 'w').write("")
    print 'c:/Temp/detection.txt  - CLEANED'


if __name__ == '__main__':
    print 'exec test'
    if sys.argv[1] == '-r':
        print 'reproduction starts'
        reproduction()
    elif sys.argv[1] == '-d':
        print 'detection start'
        detection()
    elif sys.argv[1] == '-c':
        print 'file cleaned'
        clear()
    else:
        print 'no parameters'
