# RSA Encryption/Decryption Program

import random

global e 
global d 
global n
choice = "" 

def Encrypt():
    print("Encrypted")

def Decrypt():
    print("Decrypted")
    
def setup():
    print("SOME STUFF")
    
def option():
    print("To redefine e, d or n type 'e', 'd' or 'n'")
    print("To encrypt a message with the current key, type 'Encrypt'")
    print("To decrypt a message with the current key, type 'Decrypt'")
    print("Type quit to exit the program")
    choice = input(": ").lower()
    print("\n")
    return choice

def menu():
    e = 0
    d = 0
    n = 0
    choice = ""
    setup()
    choice = option()

    while choice != 'quit':
        if choice.lower() == 'encrypt':
            Encrypt()
            
        elif choice.lower() == 'decrypt':
            Decrypt()
        
        elif choice.lower() == 'e':
            try: 
                print("Current value for e is ", e)
                e = int(input("Enter a new value for e: "))
                print("New value for e has been recorded.\n")
                choice = option()
                    
            except ValueError:
                print("That is not a valid entry\n")
                choice = option()
                
        elif choice.lower() == 'd':
            try:
                print("Current value for d is ", d)
                d = int(input("Enter a new value for d: "))
                print("New value for d has been recorded.\n")
                choice = option()
                
            except ValueError:
                print("That is not a valid entry\n")
                choice = option()
                
        elif choice.lower() == 'n':
            try:
                print("Current value for n is ", n)
                n = int(input("Enter a new value for n: "))
                print("New value for n has been recorded.\n")
                choice = option()
                
            except ValueError:
                print("That is not a valid entry\n")
                choice = option()
        else:
            num = random.randint(0,2)
            statement = ["Can't do that. Try again.\n","That's not a valid option. Try Again.\n","Review the options and try again.\n"]
            print(statement[num])
            choice = option()
menu()
