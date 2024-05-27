Normal = "Merry Christmas"
Normal2 = "Have a great holiday"
while True:
    To = input("To:\n")
    From = input("From:\n")
    Yn = input("Do you want to write a custom message?\n")
    Yn = Yn.lower()
    if Yn == 'yes':
        with open('Card.txt', 'a') as dw:
            custom = input("Custom message:\n")
            dw.write("Dear ")
            dw.write(To)
            dw.write("\n")
            dw.write(custom)
            dw.write("\nFrom: ")
            dw.write(From)
            dw.write("\n\n")
    else:
        with open('Card.txt', 'a') as dw:
            dw.write("Dear ")
            dw.write(To)
            dw.write("\n")
            dw.write(Normal)
            dw.write("\n")
            dw.write(Normal2)
            dw.write("\n")
            dw.write('From: ')
            dw.write(From)
            dw.write("\n\n")
    print("Message Written in card.txt")