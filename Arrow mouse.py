import keyboard as k
import mouse as m
from time import sleep
print('Use Arrows to move shift to left click ctrl to right click')
while True:
    pos = m.get_position()
    if k.is_pressed('up arrow'):
        m.move(pos[0], pos[1] - 5)
    if k.is_pressed('down arrow'):
        m.move(pos[0], pos[1] + 5)
    if k.is_pressed('left arrow'):
        m.move(pos[0] - 5, pos[1])
    if k.is_pressed('right arrow'):
        m.move(pos[0] + 5, pos[1])
    if k.is_pressed('shift'):
        m.click(m.LEFT)
        sleep(0.5)
    if k.is_pressed('Ctrl'):
        m.click(m.RIGHT)
        sleep(0.5)
    sleep(0.01)