class Car:
    #Constructor
    def __init__(self,p=" ",i=" ",e=" ",t=" "):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    #Modifier
    def setCustom(self,newp,newi,newe,newt):
        self.paint = newp
        self.interior = newi
        self.engine = newe
        self.tires = newt

    #Accessor
    def getPaint(self):
        return self.paint
    def getInterior(self):
        return self.interior
    def getEngine(self):
        return self.engine
    def getTires(self):
        return self.tires

def main():
    paint = input("Enter paint color: ")
    interior = input("Enter interior type: ")
    engine = input("Enter engine type: ")
    tires = input("Enter tires: ")

    Car1 = Car(paint,interior,engine,tires)

    print("Your vehicle is ready......")
    print("Paint: ", Car1.getPaint(),"\n"
          "Interior:", Car1.getInterior(),"\n"
          "Engine: ", Car1.getEngine(),"\n"
          "Tires: ", Car1.getTires(),"\n")
    
    Car1.setCustom("red", "Corinthian leather", "5 litre v8 507hp", "20\" Priellis")
    print("Your vehicle is ready......")
    print("Paint: ", Car1.getPaint(),"\n"
          "Interior:", Car1.getInterior(),"\n"
          "Engine: ", Car1.getEngine(),"\n"
          "Tires: ", Car1.getTires(),"\n")

main()   
