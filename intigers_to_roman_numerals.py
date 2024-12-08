
def base(number):
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    idx = 0
    while idx < 13:
        if numbers[idx] <= number:
            return numbers[idx]
        else:
            idx += 1

phrase = input("Insert integer: ")
numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

output = []
roman_num_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
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
            quotient = value // base(value)
            remainder = value % base(value)
            for i in range(quotient):
                output.append(roman_num_reversed[base(value)])
            if remainder == 0:
                repeat = False
        print(''.join(output))



