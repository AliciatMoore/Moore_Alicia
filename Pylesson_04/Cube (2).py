

def calcSurf(s):
    global area
    area = float((6*(s**2)))
    
def display(a):
    print("The surface area of a cube whose sides are",side,"in length is","{:0.5f}".format(a))

side = float(input("Enter the length of the side: "))

calcSurf(side)

display(area)
