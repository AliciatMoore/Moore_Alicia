numbers = []
import random
for i in range (0, 10):
    numbers[i] = random.randint(1, 100)
    print("Numbers...")

output = ""
for i in numbers:
    output += str(i) + " "
print(output + "\n")

def average(num):
    average = 0
    for i in num:
        average += i
    return str(average / i)
print("The average of the above numbers is..." + average(numbers))
    
    
