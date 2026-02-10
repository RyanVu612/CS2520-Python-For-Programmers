import random

number1 = random.randrange(0, 9)
number2 = random.randrange(0, 9)

if number1 < number2:
    number1, number2 = number2, number1

answer = int(input(f"What is {number1} - {number2}?"))

if answer == number1 - number2:
    print("You are right")
else:
    print("You are wrong")