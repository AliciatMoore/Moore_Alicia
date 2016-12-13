go = input("Please enter a sentence: ")
spList = go.split(" ")
wordsList = []

spot = 0
for i in range(0, 4):
    output = ""
    wordsList.append([])
    for j in range(0, 4):
        wordsList.append(spList)
        output += wordsList[i][j]
        spot += 1
    print(output)
    
