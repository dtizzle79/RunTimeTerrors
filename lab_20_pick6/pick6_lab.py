# lottery lab
import random

winning_numbers = []

for i in range (0, 6):
    number = random.randint(1, 99)
    while number in winning_numbers:
        number = random.randint(1,99)
    winning_numbers.append(number)

winning_numbers.sort()

pickednumbers = []
for i in range(0, 6):
    number = int(input("Please enter a number 1 through 99: "))
    while (number in pickednumbers or number <1 or number >99):
        print("you already entered that number, please try again.")
        number = int(input("Please enter your numbers: "))
    pickednumbers.append(number) 


print("Today's winning numbers are: ")
print(winning_numbers) 

print("You picked: ")
print(pickednumbers)

counter = 0
for number in pickednumbers:
    if number in winning_numbers:
        counter +=1

for i in range(len(winning_numbers)):
    if pickednumbers[0] == winning_numbers[0]:
        counter +=1
    elif pickednumbers[1] == winning_numbers[1]:
        counter +=1
    elif pickednumbers[2] == winning_numbers[2]:
        counter +=1
    elif pickednumbers[3] == winning_numbers[3]:
        counter +=1
    elif pickednumbers[4] == winning_numbers[4]:
        counter +=1
    elif pickednumbers[5] == winning_numbers[5]:
        counter +=1

    

print("You have " + str(counter) + " matching number(s).")