from wonderwords import RandomWord

r = RandomWord()
word = r.word(word_min_length=5, word_max_length=5)
word_letters = list(word)
print(word_letters)
print("_ _ _ _ _")
letter = input("guess a letter: ")
if letter in word_letters:
    print("horay")
else:
    print("awww...")
    