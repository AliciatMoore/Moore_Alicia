numList = []
import random
for i in range(0,4):
    numList.append([])
    for j in range(0,4):
        numList[i].append(random.randint(1, 100))
for nums in numList:
    output = ""
    for num in nums:
        output += "{:5}".format(str(num))
    print(output)

div = int(input("Please enter a number: "))
count = 0
for nums in numList:
    for num in nums:
        if int(num) % div == 0:
            count += 1
print("There are", count,"numbers divisible by", div, "in the list")
        
    
