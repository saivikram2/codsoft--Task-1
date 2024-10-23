import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password_generator():
    print("Password Generator")
    length = int(input("Enter the desired password length: "))
    
    if length < 6:
        print("Password length should be at least 6 characters for security.")
    else:
        password = generate_password(length)
        print(f"Generated password: {password}")

if __name__ == "__main__":
    password_generator()
