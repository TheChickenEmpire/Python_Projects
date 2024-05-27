from plyer import notification
from time import sleep
while True:
    Title = input("Title:\n")
    Note = input("Note to send:\n")
    try:
        Time = int(input("After how long Seconds:\n"))
        H = input("Repeat Yes No:\n").lower()
        if H == 'yes':
            while True:
                sleep(Time)
                notification.notify(
                    title = Title,
                    message = Note,
                    app_icon = None,
                    timeout = 10,
                )
        else:
            sleep(Time)
            notification.notify(
                title = Title,
                message = Note,
                app_icon = None,
                timeout = 10,
            )
    except:
        print("Non-valid input")