import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = int(input("Enter desired password length: "))

password = generate_password(password_length)
print("Generated password:", password)