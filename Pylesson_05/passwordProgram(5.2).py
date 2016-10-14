password = input("Please enter your password: ")
username = input("Please enter your username: ")
def passCheck():
    Pass = input("Please enter your password: ")
    User = input("Please enter your username: ")
    if (password == Pass and username == User):
        print("You are granted access!")
    else:
        if password != Pass:
            print("Your password is incorrect")
            passCheck()
        if username != User:
            print("Your username is incorrect")
            passCheck()
        elif (password != Pass and username != User):
            print("Your username and password is incorrect")
            passCheck()

passCheck()
    
