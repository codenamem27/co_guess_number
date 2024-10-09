from wonderwords import RandomWord


def checkletter(letter, worded, guess_worded):
    for c in worded:
        if c == letter:
            guess_worded[worded.index(c)] = c
            worded[worded.index(c)] = c

    return guess_worded

def hangman_symbol(stage):
    correct = True
    if stage == 10:
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
        print("   /|\\ |")
        print("     \\ |")
        print("        |")
        print("=========")
    elif stage  == 1:
        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("   /|\\ |")
        print("   / \\ |")
        print("        |")
        print("=========")

def game():
    word = list(RandomWord().word(word_min_length=5, word_max_length=5))
    guessed = []
    print(word)
    guess_word = ['_' for x in word]
    correct = True
    print(" ".join(guess_word))
    lives = 11
    while '_' in guess_word:

        guess = input('Guess a letter: ')
        print(" ".join(checkletter(guess, word, guess_word)))
        if guess not in word:
            lives -= 1
            hangman_symbol(lives)
        elif guess in guessed:
            lives -= 1
            hangman_symbol(lives)
        else:
            guessed.append(guess)
        if lives == 0:
            print("💀 you lost 💀")
            print("The answer was " + ''.join(word))
            correct = False


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






