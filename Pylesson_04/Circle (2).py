
def calcArea(radius):
    global area
    area = float((3.14*(radius**2)))
def display(A):
    print("The area of a circle with a radius of",r,"is","{:0.5f}".format(A))
r = float(input("Enter the radius: "))

calcArea(r)
display(area)
