import winsound
import time
while True:
    try:
        te = int(input("Time(Sec):\n"))
        time.sleep(te)
        T = 0
        while T < 4:
            T = T + 1
            winsound.Beep(550, 100)
        time.sleep(0.2)
        T = 0
        while T < 4:
            T = T + 1
            winsound.Beep(550, 100)
    except:
        print("Non-valid input")