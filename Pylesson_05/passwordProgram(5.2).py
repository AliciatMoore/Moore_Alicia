Pass = "123"
User = "helloworld"
def passCheck():
    password = input("Please enter your password: ")
    username = input("Please enter your username: ")

    if ( password == Pass and username == User):
        print("You are granted access!")
    else:
        if password != Pass and username == User:
            print("Your password is incorrect")
            passCheck()
        if username != User and password == Pass:
            print("Your username is incorrect")
            passCheck()
        else: 
            print("Your username and password is incorrect")
            passCheck()

passCheck()
    

