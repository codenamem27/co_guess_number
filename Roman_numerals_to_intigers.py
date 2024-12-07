
phrase = input("insert roman numerals (in uppercase): ")

output = 0
roman_numerals = ["I","V" ,"X" ,"L" ,"C" ,"D" ,"M"]
roman_num_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

error = False
skip = False
going = True
next_char = 0
for idx, char in enumerate(phrase):
    current = roman_num_dict[char]
    if skip:
        skip = False
    else:
        try:
            latter = roman_num_dict[phrase[idx + 1]]
        except Exception as e:
            output += current
            going = False
        if going:
            if current >= latter:
                output += current
            elif current < latter:
                output += latter - current
                skip = True
        else:
            pass

print(output)
