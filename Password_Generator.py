import random
import time

letters = ['a', 'b', 'c',
           'd', 'e', 'f',
           'g', 'h',
           'i', 'j', 'k',
           'l', 'm', 'n',
           'o', 'p', 'q',
           'r', 's',
           't', 'u', 'v',
           'w',
           'x', 'y', 'z',
           'A', 'B', "C", 'D', "E",
           "F", "G",
           "H", "I", "J", "K", "L",
           "M", "N", "O",
           "P", "Q", "R", "S", "T",
           "U", "V", "W",
           "X", "Y", "Z"]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

print("Welcome to the PyPassword Generator !\n ")
time.sleep(2)
nr_of_letters = int(input(f"How many letters would you like in your password? \n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for character in range(1, nr_of_letters + 1):
    password_list += random.choice(letters)

for character in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for character in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

password = ""
for character in password_list:
    password += character

print(f"Your password is: {password}")
