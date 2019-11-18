#! python3

import pyautogui

pyautogui.click()
distance = 400

while distance > 0:
    # Move Right
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration = 0.5)
    distance = distance - 25

    # Move Down
    print(0, distance)
    pyautogui.dragRel(0, distance, duration = 0.5)
    distance = distance - 25

    # Move Left
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration = 0.5)
    distance = distance - 25

    # Move Up
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration = 0.5)
    distance = distance - 25
