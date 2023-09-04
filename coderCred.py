cred_loop = True
while(cred_loop):

    print("Main Menu:")
    print("1. Increase Coder Cred")
    print('2. Increase Coder Cred')
    print("x. Return to main menu")
    command = input("Input your command here:")

    if command == "1":
        print("...")
    elif command == "2":
        print("...")
    elif command == "x":
        import main
        print("Thank you for using my cli!")
    else:
        print("your input is not recognized")