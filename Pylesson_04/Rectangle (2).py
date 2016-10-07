length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
perimeter = 0
def calcPerim():
    global perimeter, length, width
    perimeter = (length*2)+(width*2)
  
def display():
    print("Your rectangle is","{:0.5f}".format(perimeter ),"sq ft around.")



calcPerim()

display()



