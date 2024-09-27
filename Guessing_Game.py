import random


def difficulty():
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    check = True
    difficult = input("choose difficulty 1-10:")
    while check:
        if not difficult in numbers:
            print("try again")
            difficult = input("choose difficulty 1-10:")
        else:
            check = False
    place_value = 0
    index = 0
    number = [1]
    while int(difficult) > index:
        number.append(0)
        index += 1
    nnumber = int(''.join(map(str, number)))
    return nnumber


def game(diff):
    correct = False
    attempts = 0
    number = random.randint(1, diff)
    while not correct:
        guessed = input("What is your guess? ")
        if guessed.isdigit():
            if int(guessed) == number:
                print("correct!")
                print("you guessed " + str(attempts) + " times")
                correct = True
            elif int(guessed) < number:
                print("too low...")
                attempts += 1
            elif int(guessed) > number:
                print("too high...")
                attempts += 1
        else:
            print("error")


loop = True
while loop:

    game(difficulty())
    ask = True
    while ask:
        again = input("go again? answer y or n ")
        if again == "y":
            game(difficulty())
        elif again == "n":
            loop = False
            ask = False
        else:
            print("try again")
print("goodbye!")
