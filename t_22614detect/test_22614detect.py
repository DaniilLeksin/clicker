__author__ = 'daniil'

import pyHook
import pythoncom
import os

def onclick(event):
    mEt = "c:%s\n" % str(event.Position)
    open('c:/Temp/detection.txt', 'a').write(mEt)
    return True

def move(event):
    mEt = "m:%s\n" % str(event.Position)
    open('c:/Temp/detection.txt', 'a').write(mEt)
    return True

#hook the mouse
def detection():
    hm = pyHook.HookManager()
    hm.SubscribeMouseAllButtonsDown(onclick)
    hm.SubscribeMouseMove(move)
    hm.HookMouse()
    pythoncom.PumpMessages()
    hm.UnhookMouse()