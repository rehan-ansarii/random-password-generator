import random
import string

length = int(input("Enter a length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print(f"Your Password is: {password}")