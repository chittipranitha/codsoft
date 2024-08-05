import random
import string

def generatePassword(length):
   
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number for the length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

   
    password = generatePassword(length)

    
    print("Generated password:", password)

if __name__ == "__main__":
    main()
