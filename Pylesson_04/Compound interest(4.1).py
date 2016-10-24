

def payment(R,P,N,T):
    return((P*(1+(R/N))**(N*T))/(T*12))
r = float(input("Enter the interest rate: "))
p = float(input("Enter the principal: "))
n = float(input("Enter the number of times the loan is compounded per year: "))
t = float(input("Enter the life of the loan(in year): "))

print("The payment is $", "{:5.2f}".format(payment(r,p,n,t)))

