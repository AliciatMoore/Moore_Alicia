class MilesPerHour:
    #constructor
    def __init__(self, D=" ", H=" ", M= " ",Mph=0):
        self.distance = D
        self.hours = H
        self.minutes = M
        self.mph = Mph
    #Modifier
    def setValues(self, newD, newH, newM):
        self.distance = newD
        self.hours = newH
        self.minutes = newM
       
    #Accessors
    def getDistance(self):
        return self.distance
    def getHours(self):
        return self.hours
    def getMinutes(self):
        return self.minutes
    def getMph(self):
        self.mph = self.distance/(self.hours + self.minutes /60)
        return self.mph
   

def main():
    distance = int(input("Enter the distance: "))
    hours = int(input("Enter the hours: "))
    minutes = int(input("Enter the minutes: "))

    user1 = MilesPerHour(distance, hours, minutes)

    print(user1.getDistance(), "miles in", user1.getHours(), "hours and", user1.getMinutes(), "minutes =", user1.getMph(), "mph")

    user1.setValues(15,4,60)

    print(user1.getDistance(), "miles in", user1.getHours(), "hours and", user1.getMinutes(), "minutes =", user1.getMph(), "mph")
main()
