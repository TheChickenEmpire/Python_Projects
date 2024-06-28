from keyboard import is_pressed
from mouse import click, LEFT
import time
while True:
    if is_pressed('enter'):
        click(LEFT)
        time.sleep(0.5)