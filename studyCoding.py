study_loop = True
while(study_loop):

    print("How will you study?:")
    # these options will be replaced by a SQL database of topics to study
    # users can either query the database to choose a topic or get something new
    print("1. Study Option 1")
    print("2. Study Option 2")
    print("x. Return to main menu")
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