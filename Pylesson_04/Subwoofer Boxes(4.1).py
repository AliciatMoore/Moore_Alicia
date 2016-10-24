def volume(height,length,width):
    return((height*length*width)/1728)
h = float(input("Please enter the height in inches: "))
l = float(input("Please enter the length in inches: "))
w = float(input("Please enter the width in inches: "))

print("The volume of the subwoofer box is: {:5.2f}".format(volume(h,l,w)),"cubic feet")
