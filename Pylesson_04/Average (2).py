num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
a = 0
def average():
    global a, num1, num2, num3
    a = (1/3*(num1+num2+num3))
    
def display():
    print("The average of",num1,",",num2,",and",num3,"is","{:0.5f}".format(a),".")
    

average()
display()
