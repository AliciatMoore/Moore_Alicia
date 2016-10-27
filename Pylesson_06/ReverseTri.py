

word = input("Please enter a word: ")
print(len(word))
def tri():
    for i in range(len(word),0, -1):
        print(word[0:i])
tri()
