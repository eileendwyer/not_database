import csv


class User:

    def __init__(self):
        self.search_user()
        self.create_user = input("Enter your full name?")
        self.age = input("Enter your age.")

    def search_user(self):
        print("Welcome.")
        with open("userdata.csv") as readfile:
            data = readfile.readlines()
            self.username = input("Enter your username to login.")
            self.password = input("Password?")
            for row in data:
                user = User()
                if user.username in row[0]:
                    if user.password in row[1]:
                        print("Login successful.")
                        User.create_user()
                    elif user.username in row[0] and user.password not in row[1]:
                        print("Login unsuccessful.")
                        User.username()
                    else:
                        if user.username not in row[0] and user.password not in row[1]:
                            print("Login unsuccessful.")
                            User.username()

    def create_user(self):
        with open("userdata.csv", "a") as outfile:
            outfile.write("{}, {}, {}, {}".format(self.username, self.password, self.fullname, self.age))
        new_logout = input("(C)reate a new user or (L)ogout?")
        if new_logout.lower() == "C":
            User.create_user(self)
            User.search_user()
        else:
            print("Logging out.")

User()
