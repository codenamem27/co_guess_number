import random

def difficulty():
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    check = True
    difficult = input("choose difficulty 1-10: ")
    while check:
        if not difficult in numbers:
            print("try again")
            difficult = input("choose difficulty 1-10: ")
        else:
            print("please wait until text appears")
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
    lives = 15
    correct = False
    attempts = 0
    number = random.randint(1, diff)
    bonus = []

    bonus_chance = 100
    if diff < 11:
        bonus_chance = 10

    for i in range(int(diff / bonus_chance)):
        bonus.append(str(random.randint(1, diff)))
    while not correct:
        guessed = input("What is your guess? ")
        if guessed.isdigit() and lives > 1:
            if int(guessed) == number:
                print("correct!")
                print("you guessed " + str(attempts) + " times")
                correct = True
            elif guessed in bonus:
                print("you found a bonus number!")
                bonus.remove(guessed)
                lives += 10
                hearts = []
                index1 = 0
                while lives > index1:
                    hearts.append("♥")
                    index1 += 1
                print(''.join(hearts) + " (" + str(lives) + ")")
                attempts += 1
            elif int(guessed) < number:
                print("too low...")
                lives -= 1
                hearts = []
                index1 = 0
                while lives > index1:
                    hearts.append("♥")
                    index1 += 1
                print(''.join(hearts) + " (" + str(lives) + ")")
                attempts += 1
            elif int(guessed) > number:
                print("too high...")
                lives -= 1
                hearts = []
                index2 = 0
                while lives > index2:
                    hearts.append("♥")
                    index2 += 1
                print(''.join(hearts) + " (" + str(lives) + ")")
                attempts += 1
        elif lives == 1:
            print("💀 you lost 💀")
            print("the answer was " + str(number))
            correct = True
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
