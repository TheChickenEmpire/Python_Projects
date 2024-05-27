from datetime import datetime
import os
while True:
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    currentDateAndTime = datetime.now()
    output = currentDateAndTime.strftime("%H:%M:%S")
    print(output)