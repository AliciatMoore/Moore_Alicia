num1 = int(input("Please enter the number you want to count to: "))
num2 = int(input("Please enter the number you want to count by: "))

output = " "
for i in range(num2, num1 + 1, num2):
    output = output + str(i) + " "
print(output)
