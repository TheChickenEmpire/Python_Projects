import keyboard
import time
import mouse
while True:
    game = input('For Flappy bird type 1\nFor Pong type 2:\n')
    if game == '1':
        print('Press s to stop')
        while True:
            if keyboard.is_pressed('up arrow'):
                keyboard.press('space')
                time.sleep(0.2)
            if keyboard.is_pressed('s'):
                break
    if game == '2':
        print('Press s to stop')
        while True:
            if keyboard.is_pressed('up arrow'):
                mouse.move(x=mouse.get_position()[0], y=mouse.get_position()[1] - 1)
            if keyboard.is_pressed('down arrow'):
                mouse.move(x=mouse.get_position()[0], y=mouse.get_position()[1] + 1)
            time.sleep(0.001)
            if keyboard.is_pressed('s'):
                break
    else:
        pass