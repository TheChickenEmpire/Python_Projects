import Chipbot_Voice_Assistant
import Chipbot
import shutil
shutil.rmtree("__pycache__")
while True:
    print("Input 1 to use Chipbot\nInput 2 to use Chipbot Voice Assistant\nInput 3 to completely exit")
    OT = input()
    if OT == '1':
        print("Text exit to exit")
        Chipbot.ai()
    elif OT == '2':
        print("Say exit to exit")
        Chipbot_Voice_Assistant.main()
    elif OT == '3':
        exit()
        
    else:
        print("Non-Valid Input")