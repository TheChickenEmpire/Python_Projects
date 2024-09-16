import mouse as m
import time as t
import keyboard as k
import os
while True:
    while True:
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        select = input('Select Gravity\nLow, High, Intense, Impossible:\n').lower()
        i = int(0.5)
        if select == 'low':
            gravity = 1
            break
        elif select == 'high':
            gravity = 15
            break
        elif select == 'intense':
            gravity = 20
            break
        elif select == 'impossible':
            gravity = 2000
            i = 0
            break
        else:
            pass
    while True:
        m.move(m.get_position()[0], m.get_position()[1] + gravity)
        if k.is_pressed('esc'):
            break
        t.sleep(i)