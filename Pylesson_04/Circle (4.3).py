r = float(input("Enter the radius: "))
area = 0

def calcArea():
    global area, r
    area = 3.14*(r**2)
def display():
    print("The area of a circle with a radius of",r,"is {:0.5f}".format(area))


calcArea()
display()
