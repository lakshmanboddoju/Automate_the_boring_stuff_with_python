#! python3

import pyautogui

pyautogui.screenshot(r'D:\Automate_the_boring_stuff_with_python\16\screenshot_example.png')

print(pyautogui.locateOnScreen(r'D:\Automate_the_boring_stuff_with_python\16\example.png'))

pyautogui.moveTo((pyautogui.locateCenterOnScreen(r'D:\Automate_the_boring_stuff_with_python\16\example.png')), duration=1)

