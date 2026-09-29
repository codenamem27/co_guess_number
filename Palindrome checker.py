

loop = True
while loop:
    word = input('insert phrase: ')
    word1 = ''.join(word.replace(" ", ""))
    if ''.join(reversed(word1)) == word1:
        print("this word is a palindrome😁!")
    else:
        print("This phrase is not a palindrome😭.")

    looping = True
    while looping:
        again = input("Go again? y for yes and n for no: ")
        if again == "n":
            loop = False
            looping = False
            print("Goodbye")
        elif again != "y":
            print("Try again")
        else:
            looping = False



