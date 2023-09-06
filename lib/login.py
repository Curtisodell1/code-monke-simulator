from user import User

def login():
    while True:
        username = str(input("Username:"))
        if User.find_by_username(username) == None:
            print('Invalid username. Try again, fuckface.')
            continue
        else: break
    while True:
        password = str(input('Password:'))
        if User.check_password(username, password) == None:
            print('Invalid password. Try again, fuckface.')
            continue
        else:
            tup = User.check_password(username, password)
            user_id = tup[0]
            return user_id