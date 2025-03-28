import random
import string

def generate_password():
    length = int(input("Enter the desired length of your password : \n"))
    characters = string.ascii_letters+string.digits5
    password = ''.join(random.choice(characters) for i in range(length))
    print(f"Generated Password is: {password}\n")
generate_password()


