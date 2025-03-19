import mouse
import time
import keyboard
def click():
    mouse.click(mouse.LEFT)
def click1():
    mouse.click(mouse.RIGHT)
while True:
    if keyboard.is_pressed('ctrl'):
        click()
    if keyboard.is_pressed('r'):
        click1()
    time.sleep(0.005)