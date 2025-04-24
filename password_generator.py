import random
import string

print("Welcome To Password Generator\n")

chars = (
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    string.punctuation
)

while True:
    try:
        num = int(input("No of passwords to generate: "))
        if num <= 0:
            print("Please enter a number greater than 0.")
            break

        length = int(input("Input your password length: "))
        if length <= 0:
            print("Please enter a length greater than 0.")
            break

        print("Here are your passwords:")
        for _ in range(num):
            password = ""
            for _ in range(length):
                password += random.choice(chars)
            print(password)
        break

    except ValueError:
        print("Please enter valid numbers.")
        break
