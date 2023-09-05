from user import User

looping = True

while (looping):
    #user_creator menu
    print("User Creator:")
    while True:
        username = input("Username:")
        if not isinstance(username, str):
            print('Username must be a string.')
            continue
        else: break
    
    looping = False