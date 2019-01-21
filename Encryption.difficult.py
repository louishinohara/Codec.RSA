# RSA Encryption/Decryption Program

import random
import generate_keys as get_keys
import sys

def Encrypt(e,d,n):
    message = input("Enter a message to encrypt\n: ")
    cipher = [pow(ord(char),e,n) for char in message]
    print()
    print("Here is the ciphered message\n",cipher)
    print()
    option(e,d,n)

def Decrypt(e,d,n):
    val = input("Enter cipher text to decrypt\nDo not include [ or ( \n: ")
    newVal = val.split()
    bestVal = []
    
    for i in newVal:
        x = i.replace(",","")
        bestVal.append(int(x))
     
    decipher = [chr(pow(char,d,n)) for char in bestVal]
    print(''.join(decipher))
    print()
    option(e,d,n)
    
def setup():
    print("\n\nWelcome to my Codec program.\nWith this program, you will be able to generate cipher/keys and encrypt/decrypt a message.\n")
    option = int(input("Enter 1 to input values for 'e', 'd' and 'n'.\nEnter 2 to generate new cipher/keys\n: "))
    if option == 1:
        print()
        print("Please enter your values for 'e', 'd' and 'n'.\n")
        e = int(input("Enter value for e: "))
        d = int(input("Enter value for d: "))
        n = int(input("Enter value for n: "))
        return e,d,n
    else:
        print()
        length = int(input("Enter the amount of bits to generate the keys from.\nNOTE: A higher value takes a longer time to generate.\n10 -> 1 second\n15 -> 30 seconds\n: "))
        e,d,n = get_keys.make_key_pair(length)
        print()
        print("Your e value is",e,"\nYour d value is",d,"\nYour n value is",n)
        print("Your values have been recorded to the program")
        return e,d,n
        

def option(e,d,n):
    print("1. To redefine e, d or n type 'e', 'd' or 'n'")
    print("2. To encrypt a message with the current key, type 'Encrypt'")
    print("3. To decrypt a message with the current key, type 'Decrypt'")
    print("4. Type 'quit' to exit the program")
    choice = input(": ").lower()
    print("\n")
    if choice.lower() == 'quit':
        sys.exit()
    else:
        doStuff(e,d,n,choice)
    return choice

def doStuff(e,d,n,choice):
    while choice != 'quit':
        if choice.lower() == 'encrypt':
            Encrypt(e,d,n)
            
        elif choice.lower() == 'decrypt':
            Decrypt(e,d,n)
        
        elif choice.lower() == 'e':
            try: 
                print("Current value for e is ", e)
                e = int(input("Enter a new value for e: "))
                print("New value for e has been recorded.\n")
                choice = option(e,d,n)
                    
            except ValueError:
                print("That is not a valid entry\n")
                choice = option(e,d,n)
                
        elif choice.lower() == 'd':
            try:
                print("Current value for d is ", d)
                d = int(input("Enter a new value for d: "))
                print("New value for d has been recorded.\n")
                choice = option(e,d,n)
                
            except ValueError:
                print("That is not a valid entry\n")
                choice = option(e,d,n)
                
        elif choice.lower() == 'n':
            try:
                print("Current value for n is ", n)
                n = int(input("Enter a new value for n: "))
                print("New value for n has been recorded.\n")
                choice = option(e,d,n)
                
            except ValueError:
                print("That is not a valid entry\n")
                choice = option(e,d,n)
        elif choice.lower() == 'quit':
            break
        else:
            num = random.randint(0,2)
            statement = ["Can't do that. Try again.\n","That's not a valid option. Try Again.\n","Review the options and try again.\n"]
            print(statement[num])
            choice = option(e,d,n)
def menu():
    e,d,n = setup()
    print()
    choice = option(e,d,n)
    doStuff(e,d,n,choice)
    
    
menu()

# Need to write the encryption program
# Need to write thedecryption program
