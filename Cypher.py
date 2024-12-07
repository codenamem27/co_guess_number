
import base64



def encrypt(encryption):
    data_bytes = encryption.encode('utf-8')
    encoded_data = base64.b64encode(data_bytes)
    encoded_string = encoded_data.decode('utf-8')
    return encoded_string

def encode(phrase):
    listed = list(phrase)
    return (''.join(reversed(listed)))




def decrypt(number1):
    numbers = list(reversed(number1))
    try:
        decoded_data = base64.b64decode(''.join(numbers))
        decoded_string = decoded_data.decode('utf-8')
        print(decoded_string)
    except Exception as e:
        print("This phrase has caused an error")


loop = True
need_loop = True
check = True
while loop:

    while need_loop:
        _crypt = input("e for encryption or d for decryption: ")
        if _crypt == "e":
            phrase1 = input("insert phrase: ")
            print(encode(encrypt(phrase1)))
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
                    
                    
        elif _crypt == "d":
            check = True
            while check:
                phrase1 = input("insert phrase: ")
                check = False


            decrypt(phrase1)
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














     