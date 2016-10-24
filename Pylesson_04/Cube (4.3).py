side = float(input("Enter the length of the side: "))
area = 0

def calcSurf():
    global area, side
    area = 6*(side**2)
    
def display():
    print("The surface area of a cube whose sides are",side,"in length is {:0.5f}".format(area))


calcSurf()

display()
