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
        else: break
    while True:
        password = str(input("Password:"))
        if not isinstance(password, str):
            print('Password must be a string.')
            continue
        else: break

    User.create_table()
    User.create(username, password)
    looping = False