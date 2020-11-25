# guess the number version 2
import random
num1 = random.randint(0, 10)

count = 1

while True:
    number_guess = input("Guess what number is in my head? ")
    number_guess = int(number_guess)
    if number_guess == num1:
        print("You guessed it!")
        print('It took you', count, 'tries')
        break
    elif number_guess != num1:
        print("Guess again!")
        count += 1

