from pynput.keyboard import Key, Controller
import keyboard
import time
import cv2
from mss import mss
import numpy
from ctypes import windll
from PIL import ImageGrab

sct = mss()
monitor = sct.monitors[0]
kb = Controller()
user32 = windll.user32
user32.SetProcessDPIAware()
title = "anti-mute for teams"
muted = False

print("ANTI-mute for teams")
print("VERSION: v1.0")
print("AUTHOR: Dustin van Hal (DustSwiffer)")
print("")
print("--------------------")
print("")
print("cannot been used while working in other window")
print("")
print("--------------------")
print("")
print("ANTI-mute activate")
print("")

while True:
 
    im = numpy.array(sct.grab(monitor))
    im = numpy.flip(im[:, :, :3], 2)
    screen = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
 
    grayScreen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    targetMuted = cv2.imread("src/images/mute.png", cv2.IMREAD_GRAYSCALE)
    targetUnmuted = cv2.imread("src/images/unmute.png", cv2.IMREAD_GRAYSCALE)

    w, h = targetMuted.shape[::-1]

    result = cv2.matchTemplate(grayScreen, targetMuted, cv2.TM_CCOEFF_NORMED)
    location = numpy.where(result >= 0.9)

    if location [0].size > 0:
        print("You got muted!")

        kb.press(Key.ctrl)
        kb.press(Key.shift)
        kb.press("m")

        time.sleep(0.01)

        kb.release(Key.ctrl)
        kb.release(Key.shift)
        kb.release("m")

        print("You got unmuted!")
        muted = False
        time.sleep(0.05)

    cv2.imshow(title, screen)
    if cv2.waitKey(25) & keyboard.is_pressed('q'):
        cv2.destroyAllWindows()
        quit()