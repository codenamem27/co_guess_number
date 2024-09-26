
import random

correct = False
number = random.randint(1, 1000)
while not correct:
    guessed = input("What is your guess? ")
    if guessed.isdigit():
        if int(guessed) == number:
            print("correct!")
            correct = True
        elif int(guessed) < number:
            print("too low...")
        elif int(guessed) > number:
            print("too high...")
    else:
        print("error")
