
study_loop = True
while(study_loop):

    print("How will you study?:")
    print("1. Study Coding")
    print('2. Increase Coder Cred')
    print("x. Exit the program")
    command = input("Input your command here:")

    if command == "1":
        print("...")
    elif command == "2":
        print("...")
    elif command == "x":
        study_loop = False
        print("Thank you for using my cli!")
    else:
        print("your input is not recognized")