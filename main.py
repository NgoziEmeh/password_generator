#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
user_letters = int(input("How many letters would you like in your password?\n"))
user_symbols = int(input(f"How many symbols would you like?\n"))
user_numbers = int(input(f"How many numbers would you like?\n"))

# generate letters to the number the user wants to add

# Set initial password value to an empty list
password = []

# Loop through the letters and randomly select number of letters the user needs(user_letters)
for num in range(1, user_letters + 1):
    selected_letters = random.choice(letters)
    password += selected_letters

# Loop through the symbols and randomly select number of symbols the user needs(user_symbols)
for num1 in range(1, user_symbols + 1):
    selected_symbols = random.choice(symbols)
    password += selected_symbols

# Loop through the numbers and randomly select number of numbers the user needs(user_numbers)
for num3 in range(1, user_numbers + 1):
    selected_numbers = random.choice(numbers)
    password += selected_numbers

print(password)

# Shuffle the generated password to get the final password
random.shuffle(password)

# Convert to a string
# You can use the join method
final_password = ''.join(password)

# or use for loop to convert

# final_password = ""
# for word in password:
#     final_password += word
print(f"The password generated for you is {final_password}")
