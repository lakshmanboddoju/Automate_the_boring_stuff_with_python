#! python3

import pyautogui

pyautogui.screenshot(r'D:\Users\pavan\Documents\GitHub-lakshmanboddoju\Automate_the_boring_stuff_with_python\16\screenshot_example.png')

print(pyautogui.locateOnScreen(r'D:\Users\pavan\Documents\GitHub-lakshmanboddoju\Automate_the_boring_stuff_with_python\16\example.png'))

pyautogui.moveTo((pyautogui.locateCenterOnScreen(r'D:\Users\pavan\Documents\GitHub-lakshmanboddoju\Automate_the_boring_stuff_with_python\16\example.png')), duration=1)

