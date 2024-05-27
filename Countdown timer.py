from time import sleep as sp
from winsound import Beep
import os
while True:
    try:
        wait = int(input('Time(sec):\n'))
        if wait > 0:
            while wait > 0:
                print(wait)
                sp(1)
                wait = wait - 1
            print('Times Up')
            Beep(500, 2000)
        else:
            print('Non-valid input')
    except:
        print('Non-valid input')