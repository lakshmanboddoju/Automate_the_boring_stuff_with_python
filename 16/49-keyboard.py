#! python3

import pyautogui

pyautogui.click(100, 100)
pyautogui.typewrite('Hello world!', interval=0.2)

pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval = 0.5)

# List of all keywords strings
print(pyautogui.KEYBOARD_KEYS)
pyautogui.press('f1')
pyautogui.hotkey('ctrl', 'o')

