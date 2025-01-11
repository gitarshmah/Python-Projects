import string
import random



digits = list(string.digits)
letters = list(string.ascii_letters)
characters = list(string.punctuation)

characters_dict = {}
characters_dict[1] = digits
characters_dict[2] = letters
characters_dict[3] = characters

def password_generator():
    print("Welcome! To the Password Generator. I will generate password for you\nInput the following to about the type of password you want\n")
    length = int(input("Enter the length of the password: "))
    password = ''

    for i in range(length):
        r = random.choice([1, 2, 3])
        p = random.choice(characters_dict[r])
        password+=p


    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    print("Password is generated here: ")
        

password_generator()