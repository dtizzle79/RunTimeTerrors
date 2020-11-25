# guess the number version 3

import random
num1 = random.randint(0, 10)

while True:
    number_guess = input("Guess what number is in my head? ")
    number_guess = int(number_guess)
    if number_guess == num1:
        print("You guessed it!")
        break
    elif number_guess < num1:
        print("Too low. Try again!")
    elif number_guess > num1:
        print("Too high. Try again!")

