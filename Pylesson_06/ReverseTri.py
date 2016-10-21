
word = input("Please enter a word: ")
def tri():
    for i in range(len(word)+1,0, -1):
        print(word[0:i])
tri()
