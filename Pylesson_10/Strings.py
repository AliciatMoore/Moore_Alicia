wordsList = []
go = input("Please enter a sentence with 16 words: ")
spList = go.split(" ")

spot = 0
for i in range(0, 4):
    output = ""
    wordsList.append([])
    for j in range(0, 4):
        wordsList[i].append(spList[spot])
        output += "{:15}".format(wordsList[i][j])
        spot += 1
    print(output)
    
