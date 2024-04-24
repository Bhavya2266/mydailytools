"""import random
import string

def generate_password(letters,upper case, lower case,numbers,special_chars):
    characters =" "
if letters=='both':
    characters += string.ascii_letters
elif letters == 'lower':
   characters += string.ascii_letters
elif letters== 'upper':
    characters += string.ascii_letters """
    

import string
import random

def generate_password(length):
    """Generate a random password of the given length."""
    # Define the set of possible characters
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password by selecting characters from the set
    password = ''.join(random.choice(chars) for i in range(length))
    
    return password

# Example usage:
print(generate_password(12))