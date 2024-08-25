import pyautogui
import keyboard
from random import choice
print('Press ctrl')
answers = 'ANSWER NOW', 'HURRY UP', 'BROOOOOO', 'PLEASSSSSSSE', 'uwu', 'IF YOU DONT TALK I WILL TRACK YOU DOWN', 'I HATE YOU', 'PLLLLLLLLLLLLLLLLLLEEEEEEEEEEEEEEEEEEEEEEEEEAAAAAAAAAAAAAAAAAAAASSSSSSSSSSSSSSSSEEEEEEEEEEEE', 'OMG JUST RESPOND', 'DADDY COME', 'UWU', 
while True:
    if keyboard.is_pressed('ctrl'):
        pyautogui.typewrite(choice(answers))
        keyboard.press('enter')