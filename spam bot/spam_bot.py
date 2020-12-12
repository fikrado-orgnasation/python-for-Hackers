import pyautogui
import time
import random

time.sleep(6)

file = open('cat.txt', 'r').read()
file = file.splitlines()

while True:
    pyautogui.typewrite(random.choice(file))
    pyautogui.press('enter')
