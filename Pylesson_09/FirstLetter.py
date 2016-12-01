myList = ["I", "like", "to" , "eat", "apple"]

def first(words):
    output = ""
    for i in words:
        output += i[0] + " "
    print(output)
first(myList)
