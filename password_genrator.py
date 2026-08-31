import random
import string
length=int(input("enter the password length : "))
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
characters = letters  + digits + symbols
password = ""
for _ in range(length):
    password += random.choice(characters)
print(f"generated password : {password}")