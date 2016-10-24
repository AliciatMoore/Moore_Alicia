

def calcPerim(le,wi):
    return(2*(le+wi))

def display(le,wi):
    print("Your rectangle is {:0.5f}".format(calcPerim(le,wi)),"sq ft around.")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
display(length,width)
