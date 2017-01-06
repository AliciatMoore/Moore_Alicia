import math
class Distance:
    #constructor
    def __init__(self, x1, y1, x2, y2,D = 0):
        self.xOne = x1
        self.xTwo = x2
        self.yOne = y1
        self.yTwo = y2
        self.distance = D

    #Modifier
    def setx1(self, Newx1):
        self.xOne = Newx1
    def setx2(self, Newx2):
        self.xTwo = Newx2
    def sety1(self, Newy1):
        self.yOne = Newy1
    def sety2(self, Newy2):
        self.yTwo = Newy2

    #Accessor
    def getxOne(self):
        return self.xOne
    def getxTwo(self):
        return self.xTwo
    def getyOne(self):
        return self.yOne
    def getyTwo(self):
        return self.yTwo
    def getDistance(self):
        self.distance = math.sqrt((self.xTwo-self.xOne)*(self.xTwo-self.xOne)+(self.yTwo-self.yOne)*(self.yTwo-self.yOne))
        return self.distance

def main():
    xOne = float(input("Enter x1: "))
    xTwo = float(input("Enter x2: "))
    yOne = float(input("Enter y1: "))
    yTwo = float(input("Enter y2: "))

   
    user1 = Distance(xOne, xTwo, yOne, yTwo)
               
    print("distance = {:0.2f}".format(user1.getDistance()))
          
    user1.setx1(1)
    user1.setx2(1)
    user1.sety1(3)
    user1.sety2(1)
    print("distance = {:0.2f}".format(user1.getDistance()))

main()
    
