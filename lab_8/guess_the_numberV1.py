# guess the number version 1
import random
num1 = random.randint(0, 10)

count = 1

while True:
    number_guess = input("Guess what number is in my head? ")
    number_guess = int(number_guess)
    if number_guess == num1:
        print("You guessed it!")
        print(count)
        #break
    elif number_guess != num1:
        print("Guess again!")
        count += 1
    if count == 10:
        print("you've reached your guess limit")
        break




