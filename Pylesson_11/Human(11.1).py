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
    hair = input("Enter hair color: ")
    hair = input("Enter hair color: ")
