from os import system, name
from time import sleep
from playsound import playsound

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def code_monke_dance():
    playsound("lib/code_monkey.wav", False)
    looping = True
    while looping:
        clear()
        print('''
              __
         w  c(..)o   (
          \__(-)    __)
              /\   (
             /(_)___)
             w /|
              | \ 
             m  m
              


     Press 'x' to be lame
    ''')
        sleep(0.375)
        clear()
        print('''
               __
         )   c(..)o  w
        (__    (-)__/
           )   /\ 
          (___(_)\ 
              |\ w
              / |
              m  m



     Press 'x' to be lame
    ''')
        sleep(0.375)