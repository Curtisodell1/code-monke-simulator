from cliArt import secret_wrapper
from cliArt import header_art
from cliArt import footer_art
from cliArt import keyboard
from welcome_menu import welcome_menu
from login import login
from playsound import playsound
from topics_studied_by_user import *
from studyCoding import study_coding
from coderCred import coder_cred
looping = True
days = 0
actions = 0
user_id = None


playsound("lib/code_monkey.wav", False)

welcome_menu()
user_id = login()

while (looping):
    #main menu
    if actions > 2:
        actions = 0
        days += 1
        header_art()
        print("Good job code monkey! You've made it through another day of Googling and using CTRL + C and CTRL + V")
        footer_art()
    print("Main Menu:")
    print("1. Study Coding")
    print('2. Increase coder cred')
    print("x. Exit the program")
    command = input("Input your command here:")
    if command == "1": 
        actions += 1
        study_coding(user_id)
    elif command == "2":
        coder_cred()
    elif command == "x":
        looping = False
        print("Thanks for wasting my time!")
    elif command == "01010011 01100101 01100011 01110010 01100101 01110100": #Secret
        secret_wrapper()
        print ("You've successfully mastered the universe")
        secret_wrapper()
        looping = False
    else:
        print("your input is not recognized")