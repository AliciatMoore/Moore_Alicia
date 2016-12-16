numsList = []
import random

for i in range(0, 4):
    output = ""
    numsList.append([])
    for j in range(0, 4):
        numsList[i].append(random.randint(1, 100))

print("\n")
for nums in numsList:
    output = ""
    for num in nums:
        output += str(num) + "\t"
    print(output + "\n")
