# Encryption/Decrytion Program
result = ""
message = ""
choice = ""

while choice != "3":
    choice = input("Do you want to encrpyt or decrypt a message? \nEnter 1 to encrypt \nEnter 2 to decrypt \nEnter 3 to exit program \n Choice: ")
    print("\n")
    
    if choice == "1":
        message = input("Enter a message to encrypt:  ")
        print("\n")

        for i in range(0,len(message)):
            result = result + chr((ord(message[i]) - 2))        # The ord() takes the char at the specific index and converts it into the corresponding #
        print("Here is your encrypted message: \n",result)      # The chr() takes the # and converts it back into the corresponding char
        print("\n")                                             # ord() <-> char()
        result = ""

    elif choice == "2":
        message = input("Enter a message to decrpyt:  ")
        print("\n")

        for i in range(0,len(message)):
            result = result + chr((ord(message[i]) + 2))
        print("Here is your decrpyted message: \n", result)
        print("\n")
        result = ""
                                  
    elif choice == "3":
        print("Good bye")
        print("\n")

    else:
        choice = input("That is not a valid. choice. \nEnter 1 to encrypt \nEnter 2 to decrypt \nEnter 3 to exit program \n Choice: ")
