def addFunc(firstNumber, secondNumber):
    return int(firstNumber) + int(secondNumber)

def subFunc(firstNumber, secondNumber):
    return int(firstNumber) - int(secondNumber)

def multipleFunc(firstNumber, secondNumber):
    return int(firstNumber) * int(secondNumber)

def divisionFunc(firstNumber, secondNumber):
    if(secondNumber<="0"):
        return "Please enter second number greater then 0"
    else:
        return int(firstNumber) / int(secondNumber)

def calculator():
    
    firstNumber = input("Enter First Number: ")
    secondNumber = input("Enter Second Number: ")

    operator = input("+, -, *, / : ")

    if(operator=="+"):
        print(addFunc(firstNumber,secondNumber))
    elif(operator=="-"):
        print(subFunc(firstNumber,secondNumber))
    elif(operator=="*"):
        print(multipleFunc(firstNumber,secondNumber))
    elif(operator=="/"):
        print(divisionFunc(firstNumber, secondNumber))
    else:
        print("Please Choose Right operator")
    
    continueCalc = input("Can you Run Calculator Again Please Press 1 otherwise Press any Key : ")
    if(continueCalc=="1"):
        calculator()
    
print("Welcome to Python Calculator Program")
calculator()
