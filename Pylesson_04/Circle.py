r = float(input("Enter the radius: "))
def calcArea():
    return(3.14*(r**2))
def display():
    print("The area of a circle with a radius of",r,"is","{:0.5f}".format(calcArea()))
display()
