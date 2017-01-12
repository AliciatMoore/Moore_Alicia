import math
class Distance:
    #constructor
    def __init__(self, x1=" ", y1=" ", x2=" ", y2=" ",D = 0):
        self.xOne = x1
        self.xTwo = x2
        self.yOne = y1
        self.yTwo = y2
        self.distance = D

    #Modifier
    def setValues(self, Newx1, Newx2, Newy1, Newy2):
        self.xOne = Newx1
        self.xTwo = Newx2
        self.yOne = Newy1
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
          
    user1.setValues(1,1,3,1)
  
    print("distance = {:0.2f}".format(user1.getDistance()))

main()
    
