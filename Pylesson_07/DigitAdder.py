number = int(input("Please enter a number: "))
Sum = 0
num = number

def sumDigits():
    global Sum, num
    while num > 0:
        Sum = Sum + (num % 10)
        num = int(num / 10)

sumDigits()
print("The sum of the digits in", number, "is", Sum)
