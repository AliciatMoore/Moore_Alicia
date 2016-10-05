

def calcSurf(s):
    return(6*(s**2))
def display(s):
    print("The surface area of a cube whose sides are",s,"in length is","{:0.5f}".format(calcSurf(s)))
side = float(input("Enter the length of the side: "))
display(side)
