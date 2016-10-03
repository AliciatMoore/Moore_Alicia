def calcPerim(le,wi):
    global perim
    perim = int((le*2)+(wi*2));
  
def display(prm):
    print("Your rectangle is","{:0.5f}".format( prm ),"sq ft around.")

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

calcPerim(length,width)

display(perim);



