class MilesPerHour:
    #constructor
    def __init__(self, D=" ", H=" ", M= " ",Mph=0):
        self.distance = D
        self.hours = H
        self.minutes = M
        self.mph = Mph
    #Modifier
    def setD(self, newD):
        self.distance = newD
    def setH(self, newH):
        self.hours = newH
    def setM(self, newM):
        self.minutes = newM
    def setMph(self, newMph):
        self.mph = newMph
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

    user1.setD(15)
    user1.setH(4)
    user1.setM(60)

    print(user1.getDistance(), "miles in", user1.getHours(), "hours and", user1.getMinutes(), "minutes =", user1.getMph(), "mph")
main()
