number = int(input("Please enter a number"))
digits = 0
average = 0
num = number

while num > 0:
    digits = digits + 1
    average = (average + (num % 10))/digits
    num = int(num / 10)

print("The average of the digits in", number, "is", average)


