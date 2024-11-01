
from wonderwords import RandomWord
import random
def difficulty():
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "hard"]
    difficult = input("insert difficulty from 1-8(you can get extra hard words by saying 'hard'): ")
    test = True
    while test:
        if difficult not in numbers:
            print("Try again")
            difficult = input("insert difficulty from 1-8(you can get extra hard words by typing 'hard'): ")
        else:
            test = False
    return difficult
print("answer in lowercase letters")
def check_letter(letter, worded, guess_worded):
    for c in worded:
        if c == letter:
            guess_worded[worded.index(c)] = c
            worded[worded.index(c)] = c
            worded[worded.index(c)] = "*"

    return guess_worded

def difficult_rating(word):
    score = 0
    diff_letters = ["q", "w", "j", "z", "x", "v"]
    for char in word:
        if char in diff_letters:
            score += 1
    return score




def hangman_symbol(stage):
    if stage == 14:
        print("\n\n\n\n\n\n")
        print("=========")

    elif stage == 13:
        print("\n\n\n")
        print("        |")
        print("        |")
        print("        |")
        print("=========")
    elif stage == 12:
        print("")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("=========")
    elif stage == 11:
        print("        +")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("=========")

    elif stage == 10:
        print("       -+")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("=========")
    elif stage == 9:
        print("      --+")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("=========")

    elif stage == 8:
        print("    +---+")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("=========")
    elif stage == 7:
        print("    +---+")
        print("    |   |")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("=========")
    elif stage == 6:
        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("        |")
        print("        |")
        print("        |")
        print("=========")
    elif stage == 5:

        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("    |   |")
        print("        |")
        print("        |")
        print("=========")
    elif stage == 4:
        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("    |\\  |")
        print("        |")
        print("        |")
        print("=========")
    elif stage == 3:
        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("   /|\\  |")
        print("        |")
        print("        |")
        print("=========")
    elif stage == 2:
        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("   /|\\  |")
        print("     \\  |")
        print("        |")
        print("=========")
    elif stage == 1:
        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("   /|\\  |")
        print("   / \\  |")
        print("        |")
        print("=========")


def game():
    length = difficulty()
    if length == "hard":
        word = list(RandomWord().word(word_min_length=10, word_max_length=10))
        loop = True
        while loop:
            if difficult_rating(word) > 1:
                loop = False
            else:
                word = list(RandomWord().word(word_min_length=10, word_max_length=10))

    else:
        length = int(length) + 2
        word = list(RandomWord().word(word_min_length=int(length), word_max_length=int(length)))
        need = True
        while need:
            if " " in word or "_" in word or "-" in word:
                word = list(RandomWord().word(word_min_length=int(length), word_max_length=int(length)))
            else:
                need = False
    answer = "".join(word)
    letters = []
    guessed = []
    guess_word = ['_' for x in word]
    correct = True
    print(" ".join(guess_word))
    lives = 15
    while '_' in guess_word and lives > 0:
        guess = input('Guess a letter: ')
        if not guess.islower():
            print("Improper answer")
        elif not 0 < len(guess) < 2:
            print("Improper answer")


        else:

            if guess not in word:
                lives -= 1
                hangman_symbol(lives)
            if guess in guessed:
                if guess not in letters:
                    lives -= 1
                    hangman_symbol(lives)
            else:
                guessed.append(guess)
            print(" ".join(check_letter(guess, word, guess_word)))
            if lives == 0:
                print("💀 you lost 💀")
                print("The answer was '" + ''.join(answer) + "'")
                correct = False
            if 4 > lives > 0:
                print("🚨warning!🚨 you only have " + str(lives) +" lives left")
            if guess in letters:
                print("letter has already been guessed")
            else:
                letters.append(guess)
            if lives != 0:
                print(letters)

    if correct:
        print("well done")


play = True
while play:
    game()
    check = True
    while check :
        again = input("play again? answer y or n: ")
        if again == "y":
            game()
        elif again == "n":
            play = False
            check = False
        else:
            print("try again")
print("Goodbye")