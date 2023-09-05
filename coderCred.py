cred_loop = True
coder_cred_score = 0

while(cred_loop):

    print("Increase your Coder Cred:")
    #Need to add logic to this and have options built out.
    print("1. Coder Cred option 1")
    print("2. Coder Cred option 2")
    print("x. Return to main menu")
    command = input("Input your command here:")

    if command == "1":
        coder_cred_score += 1
        print(f"Your coder cred score has increased and is now: {coder_cred_score}")
    elif command == "2":
        coder_cred_score -= 1
        print(f"Your coder cred score has decreased and is now: {coder_cred_score}")
    elif command == "x":
        cred_loop = False
    else:
        print("your input is not recognized")


