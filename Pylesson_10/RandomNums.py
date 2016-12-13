numsList = []
import random

for i in range(0, 4):
    output = ""
    numsList.append([random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100)])
    for j in range(0, 4):
        output += str(numsList[i][j]) + "\t"
    print(output + "\n")
print("\n")
for nums in numsList:
    output = ""
    for num in nums:
        output += str(num) + "\t"
    print(output + "\n")
        
