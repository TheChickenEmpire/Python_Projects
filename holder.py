import keyboard as kb
import time as te
while True:
    te.sleep(0.4)
    kb.press('down')
    if kb.is_pressed('shift'):
        break