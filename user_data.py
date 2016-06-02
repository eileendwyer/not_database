import csv


def search_user():
    with open("userdata.csv") as readfile:
        data = readfile.readlines()
    for row in data:
        user = User()
        for user.username in row[0]:
            if user.password  in row[1]:
                print("Login successful.")
                user.create_user()
            elif user.username in row[0] and user.password not in row[1]:
                print("Login unsuccessful.")
                user.username()
            else:
                if user.username not in row[0] and user.password not in row[1]:
                    print("Login unsuccessful.")
                    user.username()


class User:

    def __init__(self):
        print("Welcome.")
        self.username = input("Enter your username to login.")
        self.password = input("Password?")
        self.fullname = input("Enter your full name?")
        self.age = input("Enter your age.")

    def create_user(self):
        with open("userdata.csv", "a") as writefile:
            writefile.write("{}, {}, {}, {}".format(self.username, self.password, self.fullname, self.age))
        new_logout = input("(C)reate a new user or (L)ogout?")
        if new_logout.lower() == "C":
            User.create_user(self)
            search_user()
        else:
            print("Logging out.")

User()
