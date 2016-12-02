myList = ["I", "like", "to" , "eat", "apple"]
print("In order...")

output = ""
for i in myList:
    output += i + " "
print(output + "\n")

print("Reversed...")
def reverse(words):
    output = ""
    for i in range(len(words) , 0 ,-1):
        output += words[i-1] + " " 
    print(output)

reverse(myList)
