from user import User

looping = True

while (looping):
    #user_creator menu
    print("User Creator:")
    while True:
        username = str(input("Username:"))
        if username in [user.username for user in User.all]:
            print('Username already exists. Please choose another.')
            continue
        elif not 3 < len(username) < 15:
            print('Username must be a string between 3 and 15 characters.')
            continue
        else: break
    while True:
        password = str(input("Password:"))
        if not 3 < len(password) < 15:
            print('Password must be a string between 3 and 15 characters.')
            continue
        else: break

    User.create_table()
    User.create(username, password)
    looping = False