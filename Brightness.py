from screen_brightness_control import set_brightness
from word2number import w2n
while True:
    command = input('Brightness:\n')
    command = str(command)
    brightness = command.replace('set brightness to ', '')
    brightness = w2n.word_to_num(brightness)
    set_brightness(brightness)