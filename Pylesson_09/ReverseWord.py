myList = ["I", "like", "to" , "eat", "apple"]
print("In order...")

output = ""
for i in myList:
    output += i + " "
print(output + "\n")

print("Reversed...")
def reverse(words):
    Output = ""
    for i in range(len(words) , 0 ,-1):
        Output += words[i-1] + " " 
    print(Output)

reverse(myList)
