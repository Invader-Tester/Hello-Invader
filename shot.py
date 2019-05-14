import random
import sys
import os
import time
from pynput.keyboard import Key, Controller



keyboard = Controller()


def shotpress():
    time.sleep(2)
    keyboard.press(Key.print_screen)
    keyboard.release(Key.print_screen)
    time.sleep(2)
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    time.sleep(2)
    for char in "paint":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.14)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    time.sleep(2)
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release('s')
    keyboard.release(Key.ctrl)
    time.sleep(2)
    for char in "StatisticsCaller":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.14)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)


def shotpressVideo():
    time.sleep(2)
    keyboard.press(Key.print_screen)
    keyboard.release(Key.print_screen)
    time.sleep(2)
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    time.sleep(2)
    for char in "paint":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.14)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    time.sleep(2)
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release('s')
    keyboard.release(Key.ctrl)
    time.sleep(2)
    for char in "StatisticsVideoCaller":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.14)


def zoomScreenShotNav():
    i = 0
    
    keyboard.press(Key.alt)
    keyboard.release(Key.alt)
    
    while (i != 8):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        i = i + 1
        time.sleep(0.14)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

    i = 0

    while (i != 2):
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        i = i + 1
        time.sleep(0.14)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(2)
    
    i = 0

    while (i != 3):
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        i = i + 1
        time.sleep(0.14)

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    shotpress()
    time.sleep(2)
    i = 0

    while (i != 2):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        i = i + 1
        time.sleep(0.14)
    time.sleep(2)
    shotpressVideo()





#time.sleep(20)
zoomScreenShotNav()


