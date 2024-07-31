import mouse
import time
import keyboard
def click():
    mouse.click(mouse.LEFT)
while True:
    if keyboard.is_pressed('ctrl'):
        click()
    time.sleep(0.0009)