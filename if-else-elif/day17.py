import random
import string

print("=== Password Generator ===")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + "!@#$%&*?"

password = ""
for _ in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)