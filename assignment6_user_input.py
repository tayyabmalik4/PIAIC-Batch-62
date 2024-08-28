name:str = input("Enter Your name : ")

numbersList = []
numbersList1 = input("Enter your first favorite number : ")
numbersList2 = input("Enter your second favorite number : ")
numbersList3 = input("Enter your third favorite number : ")
numbersList.append(int(numbersList1))
numbersList.append(int(numbersList2))
numbersList.append(int(numbersList3))

print(f"\nHello, {name}! Let's explore your favorite numbers:")

for i in numbersList:
    if(i % 2 == 0):
        print(f"The number {i} is even")
    else:
        print(f"The number {i} is odd")


sumOfNumbers: int = 0
for i in numbersList:
    square = i**2
    print(f"The number {i} and its square: ({i}, {square})")
    sumOfNumbers += i



print(f"Amazing! The sum of your favorite numbers is: {sumOfNumbers}")

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

if(is_prime(sumOfNumbers)):
    print(f"Wow, {sumOfNumbers} is a prime number!") 
else:
    print(f"Soory, {sumOfNumbers} is not a prime number!") 
