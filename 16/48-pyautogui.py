#! python3

# https://pyautogui.readthedocs.org

# X, Y = 0, 0 starts at the top-left. so Y-coordinates increase going down, opposite to math.

import pyautogui

print(pyautogui.aize())
print(pyautogui.position())

width, height = pyautogui.size()

# Instant move to Absolute point
pyautogui.moveTo(100, 100)
# Moves with a duration
pyautogui.moveTo(100, 100, duration=1.5)

# Relative move
pyautogui.moveRel(100, 0)
pyautogui.moveRel(100, 200, duration=5)

pyautogui.click()
pyautogui.click(1245, 41)
pyautogui.doubleClick()
pyautogui.rightClick(0, 0)

pyautogui.dragRel(100,  0, duration=1)

# pyautogui.displayMousePosition()
