from wonderwords import RandomWord


def checkLetter(letter, word, guess_word):
    for c in word:
        if c == letter:
            guess_word[word.index(c)] = c
            word[word.index(c)] = '*'

    return guess_word

def hangman_symbol(stage):
    if stage < 7:
        print("        ________________________")
    else:
        print("")
    if stage < 8:
        print("        |")
    elif stage < 6:
        print("        |                    |")
    if stage < 8:
        print("        |")
    elif stage < 6:
        print("        |                    |")
        if stage < 8:
            print("        |")
        elif stage < 5:
            print("        |		     _")
            print("        |		   /   \\")
            print("        |		   \\ _ /")






word = list(RandomWord().word(word_min_length=5, word_max_length=5))

guess_word = ['_' for x in word]
word_display2 = ""
lives = 8
while '_' in guess_word:
    guess = input('Guess a letter: ')
    word_display = checkLetter(guess, word, guess_word)
    print( ' '.join(word_display))

    if word_display == word_display2:
        hangman_symbol(lives)
        lives -= 1

    word_display2 = word_display

    if lives == 0:
        print("💀 you lost 💀")
        print("The answer was " + word)


