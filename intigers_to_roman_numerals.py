


def base(number, book):
    numbers_in = []
    for key in book:
        numbers_in.append(key)
    numbers_in.reverse()
    index = 0
    while index < 13:
        if numbers_in[index] <= number:
            return numbers_in[index]
        else:
            index += 1

phrase = input("Insert integer: ")
output = []
roman_num_reversed = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M"
}
skip = False

try:
    value = int(phrase)
except ValueError:
    print("Your input contained one or more non integer characters")
except Exception as e:
    print("An unexpected error occurred")
else:
    if value == 0:
        print("")
    else:
        repeat = True

        while repeat:
            base_value = base(value, roman_num_reversed)
            quotient = value // base_value
            remainder = value % base_value
            letter = roman_num_reversed[base_value]
            for i in range(quotient):
                output.append(letter)
            if remainder <= 0:
                repeat = False
            else:
                value -= base_value * quotient


        print(''.join(output))