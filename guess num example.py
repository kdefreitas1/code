import random

random_num = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != random_num:
    if guess > random_num:
        print("The number is lower!")
    elif guess < random_num:
        print("The number is higher!")
    guess = int(input("Guess a number between 1 and 10: "))
print("You guessed correctly!")