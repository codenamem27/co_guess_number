from pprint import pprint

from wonderwords import RandomWord
import random

def difficulty():
    numbers = ["1", "2", "3", "4", "5", "hard"]
    difficult = input("insert difficulty from 1-5(you can get extra hard words by saying 'hard'): ")
    test = True
    while test:
        if difficult not in numbers:
            print("Try again")
            difficult = input("insert difficulty from 1-5(you can get extra hard words by typing 'hard'): ")
        else:
            test = False
    return difficult

print("answer in lowercase letters")


def check_letter(letter, worded, guess_worded):
    for c in worded:
        if c == letter:
            guess_worded[worded.index(c)] = c
            worded[worded.index(c)] = c

    return guess_worded

def hangman_symbol(stage):

    if stage >= 10:
        correct = True
        print("\n\n\n\n\n\n\n")
        print("=========")
    elif stage == 9:
        print("")
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
    elif stage  == 1:
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
        words = ["wry", "quiz", "vex", "lynx", "cyst", "glyph", "jinx", "cusp", "fjord"]
        word = list(random.choice(words))
    else:
        length = int(length) + 2
        word = list(RandomWord().word(word_min_length=int(length), word_max_length=int(length)))
        need = True
        while need:
            if len(word) != len(set(word)):
                word = list(RandomWord().word(word_min_length=int(length), word_max_length=int(length)))
            else:
                need = False

    letters = []
    guessed = []
    guess_word = ['_' for x in word]
    correct = True
    print(" ".join(guess_word))
    lives = 11
    while '_' in guess_word and lives > 0:

        guess = input('Guess a letter: ')
        print(" ".join(check_letter(guess, word, guess_word)))
        if guess not in word:
            if guess not in letters:
                lives -= 1
                hangman_symbol(lives)
        elif guess in guessed:
            if guess not in letters:
                lives -= 1
                hangman_symbol(lives)
        else:
            guessed.append(guess)

        if lives == 0:
            print("💀 you lost 💀")
            print("The answer was '" + ''.join(word) + "'")
            correct = False
        if 4 > lives > 0:
            print("🚨warning!🚨 you only have " + str(lives) +" lives left")

        if guess in letters:
            print("letter has already been guessed")
        else:
            letters.append(guess)
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

