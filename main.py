looping = True
days = 0
actions = 0

while (looping):
    #main menu
    print("Main Menu:")
    print("1. Study Coding")
    print('2. Increase Coder Cred')
    print("x. Exit the program")

    command = input("Input your command here:")
    if command == "1":
        with open("studyCoding.py") as study_coding:
            study_coding_loop = study_coding.read()
        exec(study_coding_loop)
    elif command == "2":
        with open("coderCred.py") as coder_cred:
            coder_cred_loop = coder_cred.read()
        exec(coder_cred_loop)
    elif command == "x":
        looping = False
        print("Thank you for using my cli!")
    elif command == "01010011 01100101 01100011 01110010 01100101 01110100":
        print ('*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-*')
        print ('*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-*')
        print ('*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-*')
        print ("You've successfully mastered the universe")
        print ('*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-*')
        print ('*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-*')
        print ('*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-*')
        looping = False
    else:
        print("your input is not recognized")