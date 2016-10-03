
def average(n1,n2,n3):
    global average
    average = (1/3*(n1+n2+n3))
    
def display(avg):
    print("The average of",num1,",",num2,",and",num3,"is","{:0.5f}".format(avg),".")
    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

average(num1,num2,num3)
display(average)
