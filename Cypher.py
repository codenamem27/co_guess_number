import random
import textwrap

def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

cyphers = {
    "a" : 4477,
    "b" : 5476,
    "c": 2349,
    "d": 1420,
    "e": 4757,
    "f": 1956,
    "g": 3132,
    "h": 1967,
    "i": 2548,
    "j": 2213,
    "k": 1165,
    "l": 1113,
    "m": 3713,
    "n": 1304,
    "o": 2545,
    "p": 3576,
    "q": 2919,
    "r": 1864,
    "s": 4116,
    "t": 4443,
    "u": 3067,
    "v": 2203,
    "w": 3301,
    "x": 4817,
    "y": 2653,
    "z": 3238,
    "!": 4797,
    "@": 3139,
    "#": 2424,
    "$": 4680,
    "%": 2155,
    "^": 2972,
    "&": 3448,
    "*": 4924,
    "(": 1569,
    ")": 1565,
    "'": 2289,
    '"': 1739,
    ":": 2482,
    ";": 1360,
    ",": 4483,
    ".": 3557,
    "<": 2448,
    ">": 3049,
    "?": 1104,
    "/": 2534,
    "_": 4438,
    "-": 3228,
    "+": 3232,
    "9": 2366,
    "8": 4762,
    "7": 3622,
    "6": 3332,
    "5": 4561,
    "4": 2532,
    "3": 3058,
    "2": 2637,
    "1": 4367,
    "0": 2605,
    "=": 4512,
    " ": 2354
}

def encrypt(encryption):
    number = random.randint(1000, 4000)
    output = []

    for char in encryption:

        output.append(str(cyphers[char] + number))

    print(str(number) + " " + "".join(output))


def decrypt(numbers, key):
    decryption = textwrap.wrap(numbers, 4)

    output = []

    for item in decryption:
        item_no = int(item) - int(key)
        output.append(get_key_by_value(cyphers, item_no))
    print(''.join(output))




    










loop = True
need_loop = True
check = True
while loop:

    while need_loop:
        __crypt = input("e for encryption or d for decryption: ")
        if __crypt == "e":
            phrase1 = input("insert phrase: ")
            phrase = phrase1.lower()
            encrypt(phrase)
            looping = True
            while looping:
                again = input("use again? Answer 'y' for yes and 'n' for no: ")
                if again == "n":
                    loop = False
                    need_loop = False
                    looping = False
                elif again != "y":
                    print("try again")
                else:
                    looping = False
        elif __crypt == "d":

            check = True
            while check:
                phrase1 = input("insert phrase: ")


                check = False
            phrase = phrase1[5:]
            first = phrase1[:4]

            decrypt(phrase, first)
            looping = True
            while looping:
                again = input("use again? Answer 'y' for yes and 'n' for no: ")
                if again == "n":
                    loop = False
                    looping = False
                    check = False
                elif again != "y":
                    print("try again")
                else:
                    looping = False
