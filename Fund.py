import keyboard
while True:
    if keyboard.is_pressed('ctrl'):
        keyboard.press_and_release('t')
        keyboard.press_and_release('w')