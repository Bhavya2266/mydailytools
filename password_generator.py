
import string
import random

def generate_password(length=8,upper_case=True, numbers_case=True, special_case=True):
    if upper_case:
        chars = string.ascii_letters
    else:
        chars = string.ascii_lowercase

    if numbers_case:
        chars += string.digits

    if special_case:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))

def main():
    while True:
        mode = input("Please select the mode (default/manual): ").lower()
        if mode == "default":
            print(f'Generated password: {generate_password()}')
            
        elif mode == "manual":
            while 1 :
                try:
                    length = int(input("Enter the password with its desired length: "))
                   
                except ValueError:
                    print("Enter a correct number to continue.")
                upper_case = input(f"Use uppercase letters (y/n): ").lower() == "y"
                numbers_case= input(f"Use numbers (y/n): ").lower() == "y"
                special_case= input(f"Use special characters (y/n): ").lower() == "y"
                print(f"Generated password: {generate_password(length, upper_case, numbers_case, special_case)}")
                    
        else:
            print("Invalid option, please try again later.")

if __name__ == "__main__":
    main()