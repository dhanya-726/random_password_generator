import random
import string
def gen_pass(length,letter,digit,symbols):
    chars=' '
    if letter:
        chars+=string.ascii_letters
    if digit:
        chars+=string.digits
    if symbols:
        chars+=string.punctuation
    if not chars:
        raise("At least one character type must be selected.")
    
    password=''.join(random.choice(chars)for _ in range(length))
    return password
def main():
    print("Random Password Generator")
    try:
        length=int(input("Enter the desired password length (minimum 8): "))
        if length<8:
            print("Password length should be at least 8 characters.")
            return
        letter=input("Include letters?(y/n): ").lower()=='y'
        digit=input("Include digits?(y/n): ").lower()=='y'
        symbols=input("Include symbols?(y/n): ").lower()=='y'
        password=gen_pass(length,letter,digit,symbols)
        print(f"\nGenerated Password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")
if __name__=="__main__":
    main()