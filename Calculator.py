def is_float(number):
    try:
        float(number)
        return True 
    except ValueError:
        return False

def calculate():
    while True:
        num1 = input("Number 1:")
        num2 = input("Number 2:")
        if(is_float(num1) and is_float(num2)):
            num1 = float(num1)
            num2 = float(num2)
            while True:
                operator = input("(A)dd, (S)ubtract, (D)ivide, (M)ultiply:")
                operator = operator.lower()
                if operator == "a" or operator == "add":
                    result = num1 + num2
                    break
                elif operator == "s" or operator == "subtract":
                    result = num1 - num2
                    break
                elif operator == "d" or operator == "divide":
                    result = num1 / num2
                    break
                elif operator == "m" or operator == "multiply":
                    result = num1 * num2
                    break
                else:
                    print ("Please Enter Add Subtract Divide Multiply")
            print(result)
            Again = input("Want to do another caculation ")
            Again = Again.lower()
            if Again == "no":
                break
        else:
            print ("Enter Number Only")
calculate()