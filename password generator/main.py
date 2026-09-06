import csv  # Imports the CSV module.
import random  # Imports tools for selecting random values.
import string  # Imports predefined character sets.
import math  # Imports mathematical functions.


class WeakPassword(Exception):  # Defines an exception for short passwords.
    pass  # Uses the default exception behavior.


def password_gen():  # Defines the password-generation function.
    try:  # Starts handling invalid password lengths.
        length_password = int(input("Enter the length of the password: "))  # Reads the requested password length.
        if length_password < 8:  # Checks whether the password is too short.
            raise WeakPassword("Weak password")  # Reports a password that is too short.
        list_of_numbers = list(range(0, math.factorial(length_password)))  # Creates the numeric character choices.
        list_of_letters_lower = list(string.ascii_lowercase)  # Creates lowercase letter choices.
        list_of_letters_upper = list(string.ascii_uppercase)  # Creates uppercase letter choices.
        list_of_special_characters = list(string.punctuation)  # Creates special-character choices.
        password_list = []  # Stores the selected password characters.
        for part in range(length_password):  # Selects characters until the requested length is reached.
            selected_list = random.choice([list_of_numbers, list_of_special_characters, list_of_letters_upper, list_of_letters_lower])  # Chooses a character category.
            part = random.choice(selected_list)  # Chooses one value from that category.
            part = str(part)  # Converts the selected value to text.
            password_list.append(part)  # Adds the selected value to the password.
        password = "".join(password_list)  # Combines the selected values into one password.
        print(password)  # Displays the generated password.
    except WeakPassword:  # Handles passwords shorter than eight characters.
        print("Enter a password length of at least 8.")  # Shows the length requirement.
        password_gen()  # Asks the user for a new length.


password_gen()  # Starts the password generator.
