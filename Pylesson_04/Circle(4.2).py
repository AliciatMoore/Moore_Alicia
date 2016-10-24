
def calcArea(R):
    return(3.14*(R**2))
def display(R):
    print("The area of a circle with a radius of",R,"is {:0.5f}".format(calcArea(R)))
r = float(input("Enter the radius: "))
display(r)
