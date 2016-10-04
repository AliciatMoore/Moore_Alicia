
def average(n1,n2,n3):
    return(1/3*(n1+n2+n3))
def display(n1,n2,n3):
    print("The average of",n1,",",n2,",and",n3,"is","{:0.5f}".format(n1,n2,n3),".")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
display(num1,num2,num3)
