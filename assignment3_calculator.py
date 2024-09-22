def calculator():
    
    firstNumber = input("Enter First Number: ")
    secondNumber = input("Enter Second Number: ")

    operator = input("+, -, *, / : ")

    if(operator=="+"):
        print(int(firstNumber) + int(secondNumber))
    elif(operator=="-"):
        print(int(firstNumber) - int(secondNumber))
    elif(operator=="*"):
        print(int(firstNumber) * int(secondNumber))
    elif(operator=="/"):
        print(int(firstNumber)/int(secondNumber))
    else:
        print("Please Choose Right operator")
    
    continueCalc = input("Can you Run Calculator Again Please Press 1 otherwise Press any Key : ")
    if(continueCalc=="1"):
        calculator()
    
print("Welcome to Python Calculator Program")
calculator()
