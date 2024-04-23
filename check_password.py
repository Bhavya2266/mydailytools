import random
import string

def generate_password(letters,upper case, lower case,numbers,special_chars):
    characters =" "
if letters=='both':
    characters += string.ascii_letters
elif letters == 'lower':
   characters += string.ascii_letters
elif letters== 'upper':
    characters += string.ascii_letters
    

