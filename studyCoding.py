study_loop = True
study_coding_points = 0 


while(study_loop):
    print("How will you study?:")
    # these options will be replaced by a SQL database of topics to study
    # users can either query the database to choose a topic or get something new
    print("1. Study Option 1")
    print("2. Study Option 2")
    print("x. Return to main menu")
    command = input("Input your command here:")
    if command == "1":
        study_coding_points += 1
        print(f"Your coding points have increased you now have: {study_coding_points}")
    elif command == "2":
        study_coding_points -= 1
        print(f"Your coding points have decreased you now have: {study_coding_points}")
    elif command == "x":
        study_loop = False
    else:
        print("your input is not recognized")



