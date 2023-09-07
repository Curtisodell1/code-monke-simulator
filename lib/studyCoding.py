from cliArt import header_art
from cliArt import footer_art
from resources_class_methods import *
from topics_studied_by_user import *

def study_coding(user_id):
    study_loop = True
    still_studying = True
    while study_loop:
        print("How will you study?:")
        print("1. Show a list of topics to study!")
        print("2. Choose to learn about a topic")
        command = input("Input your command here:")
        if command == "1":
            #print list of things to study
            print(Resources.get_topics())
        elif command == "2":
            topic_id = input("Select the study topic by ID:")
            while still_studying:
                print("________________________________________________________________________________________________________________________")
                print(Resources.select_topic(topic_id))
                print("________________________________________________________________________________________________________________________")
                finished_study = input("Have you mastered this topic? \nEnter y/n:")
                if finished_study == "y":
                    Topics_By_User.add_to_table(user_id, topic_id)
                    still_studying = False
                    study_loop = False 
                    print("You've increased your coder cred")   
                elif finished_study == "n":
                    print("Keep Studying!")
                else:
                    print("Keep studying, dumbass, and learn to read!")
        elif command == "x":
            study_loop = False
        else:
            print("your input is not recognized")



