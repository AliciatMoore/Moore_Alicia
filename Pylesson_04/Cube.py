
side = float(input("Enter the length of the side: "))

def calcSurf():
    return(6*(side**2))
def display():
    print("The surface area of a cube whose sides are",side,"in length is","{:0.5f}".format(calcSurf()))
display()
