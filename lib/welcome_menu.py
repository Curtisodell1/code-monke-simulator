def welcome_menu():
    print('''               
              __M__
            ,.-" "-.,
           /   ===   \\
          /  =======  \\
       __|  (o)   (0)  |__      
      / _|    .---.    |_ \         
     | /.----/ O O \----.\ |       
      \/     |     |     \/        
      |                   |            
      |                   |           
      |                   |          
      _\   -.,_____,.-   /_         
  ,.-"  "-.,_________,.-"  "-.,
 /          |       |          \  
|           l.     .l           | 
|            |     |            |
l.           |     |           .l             
 |           l.   .l           | \,     
 l.           |   |           .l   \,    
  |           |   |           |      \,  
  l.          |   |          .l        |
   |          |   |          |         |
   |          |---|          |         |
   |          |   |          |         |
   /"-.,__,.-"\   /"-.,__,.-"\\"-.,_,.-"\\
  |            \ /            |         |
  |             |             |         |
   \T_|E_|D_|__/ \C_|U_|R_|T_/ \_|__|__/ 
''')
    print("|||||||||||||||||||||||||||||||||||||||||")
    print("          CODE MONKE SIMULATOR           ")
    looping = True

    while looping:
        #welcome menu

        print("|||||||||||||||||||||||||||||||||||||||||")
        print("|1. Create Account  |||||||||||||||||||||")
        print("|2. Login           |||||||||||||||||||||")
        print("|||||||||||||||||||||||||||||||||||||||||")

        command = input("Input your command here:")
        if command == "1":
            with open("lib/user_creator_menu.py") as user_creator:
                user_creator_loop = user_creator.read()
            exec(user_creator_loop)
        elif command == "2":
            looping = False
        else:
            print("|||||||||||||||||||||||||||||||||||||||||") 
            print('Try again, dumbass.')