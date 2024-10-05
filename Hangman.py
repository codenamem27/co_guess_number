from wonderwords import RandomWord


def checkLetter(letter, word2, guess_word):
    for c in word2:
        if c == letter:
            guess_word[word2.index(c)] = c
            word2[word2.index(c)] = '*'

    return guess_word

def hangman_symbol(stage):
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

word = list(RandomWord().word(word_min_length=5, word_max_length=5))

guess_word = ['_' for x in word]
word_display2 = "_ _ _ _ _"
lives = 10
while '_' in guess_word:
    guess = input('Guess a letter: ')
    word_display = checkLetter(guess, word, guess_word)
    print( ' '.join(word_display))
    if guess not in guess_word:
        hangman_symbol(lives)
        lives -= 1
    else:
        guess_word.remove(guess)

    word_display2 = word_display
    if lives == 0:
        print("💀 you lost 💀")
        print("The answer was " + ''.join(word))


