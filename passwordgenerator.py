import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters  # Includes both uppercase and lowercase letters
    
    if use_digits:
        characters += string.digits  # Adds numbers 0-9
    if use_special_chars:
        characters += string.punctuation  # Adds special characters
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Debugging - Confirm script starts
print("Starting password generator...")

# Get user preferences
length = input("Enter password length: ")
print(f"DEBUG: Length entered = {length}")

use_digits = input("Include numbers? (yes/no): ").strip().lower() == "yes"
print(f"DEBUG: Use digits = {use_digits}")

use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
print(f"DEBUG: Use special characters = {use_special_chars}")

# Convert length to integer
try:
    length = int(length)
except ValueError:
    print("Invalid input! Please enter a valid number for password length.")
    exit()

# DEBUG: Confirm function is being called
print("DEBUG: Calling generate_password()...")

# Generate and print the password
password = generate_password(length, use_digits, use_special_chars)

# DEBUG: Ensure password is generated
print(f"DEBUG: Generated password = {password}")

print(f"\nYour Generated Password: {password}")
