
import random

def game():
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

loop = True

while loop:
    game()
    ask = True
    while ask:
        again = input("go again? answer y or n ")
        if again == "y":
            game()
        elif again == "n":
            loop = False
            ask = False
        else:
            print("try again")
print("goodbye!")
