import random

pass_words = "qwertyuiopasdfghjklzxcvbnmk1234567890"

password = ""

question = input("wanna change your password?: ")

if question.lower() == "yes":
    print("Ok")
    password_length = int(input("Pick Password Length: "))
    new_password = ""

    for _ in range(password_length):
        new_password += random.choice(pass_words)

    print("New password: ", new_password)
