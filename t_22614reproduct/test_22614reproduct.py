__author__ = 'daniil'
import os
import win32api, win32con
path = 'c:/Temp/detection.txt'


def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def reproduction():
    from pymouse.pymouse import PyMouse
    import time
    if os.path.exists(path):
        l_points = open(path, 'r').readlines()
    if l_points:
        m = PyMouse()
        for line in l_points:
            if 'm:' in line:
                point = eval(line.split('m:')[1])
                m.move(point[0], point[1])
            if 'c:' in line:
                point = eval(line.split('c:')[1])
                click(point[0], point[1])
            time.sleep(0.05)
    else:
        print 'no point map'
        return
    # instantiate an mouse object
    #m = PyMouse()
    #start position (1;1)
    #m.move(1, 1)
    # move the mouse to int x and int y (these are absolute positions)
    #for i in xrange(150):
    #    m.move(i + 1, i + 1)
    #    print m.position()
    #    time.sleep(0.1)



# click works about the same, except for int button possible values are 1: left, 2: middle, 3: right
#m.click(500, 300, 1)

# get the screen size
#m.screen_size()
# (1024, 768)

# get the mouse position
#m.position()
# (500, 300)