from cliArt import header_art
from cliArt import footer_art

def coder_cred():
    coder_cred_score = 3
    cred_loop = True
    while cred_loop:

        header_art()
        print("Increase your Coder Cred:")
        print("1. Play video games")
        print("2. Take a shower")
        print("3. Go for a walk")
        print("x. Return to main menu")
        footer_art()
        command = input("Input your command here:")

        if command == "1":
                coder_cred_score += 1
                header_art()
                print(f"Your coder cred score has increased and is now: {coder_cred_score}")
                footer_art()
        if coder_cred_score != 0:
            if command == "2":
                coder_cred_score -= 1
                header_art()
                print(f"Your coder cred score has decreased and is now: {coder_cred_score}")
                footer_art()
            elif command == "3":
                coder_cred_score -= 1
                header_art()
                print(f"Your coder cred score has decreased and is now: {coder_cred_score}")
                footer_art()
            elif command == "x":
                cred_loop = False
        elif coder_cred_score == 0:
            header_art()
            print('Your coder cred is too low, try playing some video games instead.')
            footer_art()
        else:
            header_art()
            print("your input is not recognized")
            footer_art()


