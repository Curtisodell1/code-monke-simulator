def coder_cred():
    coder_cred_score = 3
    cred_loop = True
    while cred_loop:

        print("Increase your Coder Cred:")
        #Need to add logic to this and have options built out.
        print("1. Play video games")
        print("2. Take a shower")
        print("3. Go for a walk")
        print("x. Return to main menu")
        command = input("Input your command here:")

        if coder_cred_score > 0:
            if command == "1":
                coder_cred_score += 1
                print(f"Your coder cred score has increased and is now: {coder_cred_score}")
            elif command == "2":
                coder_cred_score -= 1
                print(f"Your coder cred score has decreased and is now: {coder_cred_score}")
            elif command == "3":
                coder_cred_score -= 1
                print(f"Your coder cred score has decreased and is now: {coder_cred_score}")
            elif command == "x":
                cred_loop = False
            else:
                print("your input is not recognized")
        else: print('Your coder cred is too low, try playing some video games instead.')


