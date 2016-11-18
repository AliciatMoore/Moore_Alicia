myList = ["I", "like", "to" , "eat", "apple"]
print("In order...")

output = ""
for i in myList:
    output += i + " "
print(output + "\n")

def reverse(words):
    Output = ""
    for i in range(len(words)-1 , -1 ,-1):
        Output += words[i] + " " 
    print(Output)

reverse(myList)
