# 1. Simple Message
# Task: Assign a message to a variable and then print that message.

innovation = "Artificial Intelligence is a future of Innovation"
print(innovation)

# 2. Simple Messages
# Task:
# ● Assign a message to a variable and print that message.
# ● Change the value of the variable to a new message, and print the new message.
AI = "Artificial Intelligence New World Innovation"
print(AI)
AI = "Artificial Intelligence Updated"
print(AI)

# 3. Personal Message
# Task:
# ● Use a variable to represent a person’s name.
# ● Print a message to that person, such as, “Hello Eric, would you like to learn some
# Python today?”

personName = "Tayyab"
print(f"Hello {personName}, would you like to learn some Python today?")

# 4. Name Cases
# Task:
# ● Use a variable to represent a person’s name.
# ● Print the person’s name in lowercase, uppercase, and title case.
print("Lower case : ", personName.lower())
print("Upper case : ", personName.upper())
print("title case : ", personName.title())

# 5. Famous Quote
# Task:
# ● Find a quote from a famous person you admire.
# ● Print the quote and the name of its author.

writer = "Marc Benioff"
quote = "Artificial intelligence and generative AI may be the most important technology of any lifetime."
print(f'{writer} once said, "{quote}"')

# 6. Famous Quote 2
# Task:
# ● Use a variable called famous_person to represent the famous person’s name.
# ● Compose the message and represent it with a variable called message.
# ● Print the message.
famous_person = "Elon Musk"
message = f"{famous_person} once said, AI is our future"
print(message)

# 7. Stripping Names
# Task:
# ● Use a variable to represent a person’s name, and include some whitespace characters
# at the beginning and end of the name.
# ● Make sure you use each character combination, \t and \n, at least once.
# ● Print the name once, so the whitespace around the name is displayed.
# ● Print the name using each of the three stripping functions: lstrip(), rstrip(), and
# strip().
personName = "\t\t   Tayyab Ashraf      \t"
print("Simple person name : ",personName, ".")
print("Left Strip person Name : ",personName.lstrip(), ".")
print("Right Strip person Name : ",personName.rstrip(), ".")
print("Strip person Name : ",personName.strip(), ".")

# 8. Variable Sum
# Task: Assign the values 5, 10, and 15 to three variables x, y, and z. Print their sum.
x = 5
y = 10
z = 15
print(x + y + z)

# 9. Variable Swap
# Task: Swap the values of two variables a and b. Print the values before and after the swap.
a = 10
b = 20
print(f"before swaping value of a is : {a} and value of b is : {b}")
[a, b] = [b, a]
print(f"After swaping value of a is : {a} and value of b is : {b}")

# 10. Favorite Color
# Task: Create a variable with your favorite color and print it. Then change the variable name to
# something else and print the color again.
favColor = "red"
print(f"This is my Favorite Color : {favColor}")
updatedFavColor = favColor
print(f"Updated Fav Color : {updatedFavColor}")

# 11. Changing Pet Name
# Task: Create a variable pet_name and set it to "Buddy". Change the value of pet_name to
# "Max" and print the new value.
pet_name = "Buddy"
print(f"This is Pet Name", pet_name)
pet_name = "Oggy"
print(f"This is Updated Pet Name", pet_name)

# 12. Observing Name Error
# Task: Assign the value "Sunshine" to a variable and print it. Then, mistakenly try to print a
# variable with a different name (like sunsine) and observe the error.
sunshine = "Sunshine"
print(sunshine)
# print(sunsine)

# 13. Reassigning Score
# Task: Assign the value 100 to a variable score and print it. Then assign a new value to score
# and print it again.
score = 100
print(f"This is score Now : {score}")
score = 140
print(f"Score is Updated : {score}")

# 14. City Name
# Task: Create a string variable city and assign it the name of a city you like. Print the city
# name.

city:str = "Lahore"
print(f"This is my city {city}")

# 15. Title Case Text
# Task: Create a variable text with the value "python programming" and print it in title case.
text:str = "python programming"
print(text.title())

# 16. Lowercase Conversion
# Task: Assign a string with mixed cases to a variable and print it in all lowercase letters.
text1 : str = "ThIS iS The Practice CoDe"
print(text1.lower())

# 17. Uppercase Conversion
# Task: Assign a string with mixed cases to a variable and print it in all uppercase letters.
text2:str = "ThIS iS The Practice CoDe"
print(text2.upper())

# 18. Current Temperature
# Task: Create a variable temperature with the value 25. Print "The current temperature is
# [temperature] degrees." using the variable.
temperature:int = 25
print(f"The current temperature is {temperature} degrees.")

# 19. Printing a Poem
# Task: Create a variable poem with a short poem that has multiple lines. Print the poem with
# each line starting on a new line.
poem:str='''In the quiet of the night,
Stars whisper soft and bright,
Dreams take flight, hearts ignite,
In the stillness, pure delight.

Moonlight dances, shadows play,
Chasing worries far away,
In this moment, here we stay,
Until the dawn greets the day.'''
print(poem)