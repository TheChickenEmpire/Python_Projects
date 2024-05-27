def Calculator():
    while True:
        try:
            Calculate = str(input("Input Calculation:\n"))
            Calculate = int(eval(Calculate))
            print(Calculate)
        except FileExistsError:
            print("Error")
Calculator()