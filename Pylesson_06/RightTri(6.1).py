word = input("Please enter a word: ")
def tri():
    for i in range(len(word),0, -1):
        print(word[i : len(word)])
tri()
