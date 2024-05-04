import random
import string
def generate_password(length=12):
    # Define characters to choose from for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password (default is 12): "))
    if password_length <= 0:
        print("Password length should be greater than zero. Using default length (12).")
        password_length = 12
    
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)
