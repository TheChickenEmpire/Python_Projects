def Calculator():
    while True:
        try:
            Calculate = str(input("Input Calculation:\n"))
            Calculate = float(eval(Calculate))
            print(Calculate)
        except:
            print("Error")
Calculator()