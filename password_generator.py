import random
import string

def generate_password(length):
    if length < 4:
        return "Error: Password length should be at least 4 characters."

    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(all_characters, length)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Please enter a valid length.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        password = generate_password(length)
        print(f"Generated password: {password}")

        another_password = input("Do you want to generate another password? (yes/no): ")
        if another_password.lower() != 'yes':
            print("Thank you for using the Password Generator! Goodbye!")
            break

if __name__ == "__main__":
    main()
