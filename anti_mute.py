from pynput.keyboard import Key, Controller
import keyboard
import time
import cv2
import mss
import numpy
from ctypes import windll
from PIL import ImageGrab

kb = Controller()
user32 = windll.user32
user32.SetProcessDPIAware()
title = "anti-mute for teams"
muted = False

print("ANTI-mute for teams")
print("VERSION: v1.0")
print("AUTHOR: Dustin van Hal (DustSwiffer)")
print("--------------------")
print("cannot been used while working in other window")

while True:
    screen = numpy.asarray(ImageGrab.grab())    
    grayScreen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    targetMuted = cv2.imread("src/images/mute.png", cv2.IMREAD_GRAYSCALE)
    targetUnmuted = cv2.imread("src/images/unmute.png", cv2.IMREAD_GRAYSCALE)

    w, h = targetMuted.shape[::-1]

    result = cv2.matchTemplate(grayScreen, targetMuted, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(result >= 0.9)

    if loc[0].size > 0:
        muted = True;

    if muted:
        kb.press(Key.ctrl)
        kb.press(Key.shift)
        kb.press("m")

        time.sleep(0.01)

        kb.release(Key.ctrl)
        kb.release(Key.shift)
        kb.release("m")

        muted = False

    for pt in zip(*loc[::-1]):
        cv2.rectangle(screen, pt,(pt[0] + w, pt[1] + h), (0,255,0), 3)

    cv2.imshow(title, screen)

    if cv2.waitKey(25) & keyboard.is_pressed('q'):
        cv2.destroyAllWindows()
        quit()