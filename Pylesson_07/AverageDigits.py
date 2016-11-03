number = int(input("Please enter a number: "))
digits = 0
average = 0
num = number

def avDigits():
    global average,num,digits
    while num > 0:
        digits = digits + 1
        average = (average + (num % 10))/digits
        num = int(num / 10)
avDigits()
print("The average of the digits in", number, "is", average)


