class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any key to exit""")
        if user_input =="1":
            self.signup()
        elif user_input =="2":
            self.signin()
        elif user_input =="3":
            pass
        elif user_input =="4":
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter your mail -> ")
        pwd = input("Set your password -> ")
        self.username = email
        self.password = pwd
        print("Signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password =='':
            print("Pls signup first by pressing 1 in main menu")
        else:
            uname = input("Enter your username/mail -> ")
            pwd = input("Enter your password -> ")
            if self.username == uname and self.password == pwd:
                print("You have successfully signed in !!")
                self.loggedin = True
            else:
                print("Please input correct ceredentials...")
        print("\n")
        self.menu()

obj = chatbook()