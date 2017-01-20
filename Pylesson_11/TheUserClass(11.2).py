import random
class User:
    def __init__(self, fname="", lname="", avat = ""):
        self.firstName = fname
        self.lastName = lname
        self.avatar = avat
        self.userID = random.randint(0,1000000)

    def setAvat(self,newAvat):
        self.avatar = newAvat

    def getfname(self):
        return self.firstName
    def getlname(self):
        return self.lastName
    def getavat(self):
        return self.avatar
    def getID(self):
        return self.userID
    
        

def main():
    
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    avat = input("Do you want a public avatar? y or n")
    

    if avat == "n":
        user1 = User(firstName, lastName)
    if avat == "y":
        avatar = input("Please enter your avatar name: ")
        user1 = User(firstName, lastName, avatar)
           
main()
def __str__(self):
        return "Customer Info...\nFirst Name: " + self.firstName + \
                                "\nLast Name: " + self.lastName + \
                                "\nAvatar : " + self.avatar + \
                               "\nUser ID#: " + str(self.userID)
__str__(self)
return "Customer Info...\nFirst Name: " + user1.getfname() + \
                                "\nLast Name: " + user1.getlname() + \
                                "\nAvatar : " + user1.getavat()+ \
                                "\nUser ID#: " + str(user1.getID())

