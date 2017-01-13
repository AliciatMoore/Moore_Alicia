class Human:
    #constuctor
    def __init__(self, h=" ", e=" ", s=" "):
        self.hair = h
        self.eyes = e
        self.skin = s

    #modifier
    def setHES(self, newh, newe, news):
        self.hair = newh
        self.eyes = newe
        self.skin = news

    #accessor
    def gethair(self):
        return self.hair
    def geteyes(self):
        return self.eyes
    def getskin(self):
        return self.skin

def main():
    hair = input("Enter hair color: ")
    eyes = input("Enter eye color: ")
    skin = input("Enter skin color: ")

    user1 = Human(hair, eyes, skin)
    print("My info...\n"
          "Hair: ", user1.gethair(),"\n"
          "Eyes: ", user1.geteyes(),"\n"
          "Skin: ", user1.getskin(),"\n")
    user1.setHES("brown","blue","tan")
    print("Friend's info...\n"
          "Hair: ", user1.gethair(),"\n"
          "Eyes: ", user1.geteyes(),"\n"
          "Skin: ", user1.getskin())      
main()
