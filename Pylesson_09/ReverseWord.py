myList = ["I", "like", "to" , "eat", "apple"]
print("In order...")

output = ""
for i in myList:
    output += i + " "
print(output + "\n")

def reverse(words):
    Output = ""
    for i in range (0,5):
        Output += words[i] + " "
reverse(myList)
print(Output)

