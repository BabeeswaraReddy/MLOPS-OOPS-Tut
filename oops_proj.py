class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        
    def menu(self):
        user_input = input("""Welcome to Chatbook!! How would you like to proceed?
                           1. Press 1 to Sign Up
                           2. Press 2 to Sign In
                           3. Press 3 to Write a Post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           -> """)
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.send_message()
        else:
            exit()
            
    
    def signup(self):
            email = input("Enter your email here -> ")
            pwd = input("Setup your password here -> ")
            self.username = email
            self.password = pwd
            print("You have signedup successfully!!")
            print("\n")
            self.menu() 
            
    def signin(self):
        if self.username == '' or self.password == '':
            print("Please sign up first by pressing 1 in the main menu!!")
        else:
            uname = input("Enter your email here -> ")
            pwd = input("Enter your password here -> ")
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully!!")
                self.loggedin = True
            else:
                print("Please enter correct credentials!!")
        print("\n")
        self.menu()
        
    def write_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            print(f"Your post '{txt}' has been posted successfully!!")
        else:
            print("You need to sign in first to post something....")
        print("\n")
        self.menu()
        
    def send_message(self):
        if self.loggedin==True:
            friend = input("Who would you like to message?")
            msg = input("Enter your message here -> ")
            print(f"Your message '{msg}' has been sent to {friend} successfully!!")
        else:
            print("You need to sign in first to send a message....")
        print("\n")
        self.menu()
                
            
                        
#user1 = chatbook()
            