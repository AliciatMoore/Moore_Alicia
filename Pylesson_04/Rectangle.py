length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

def calcPerim():
    return(2*(length+width))

def display():
    print("Your rectangle is","{:0.5f}".format(calcPerim()),"sq ft around.")

display()
