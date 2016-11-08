word = input("Please enter a word: ")
stop = len(word)
start = 0
def tree(word, start, stop):
    if start <= stop:
        print (word[start : stop])
        start += 1
        tree(word, start, stop)

print(tree(word, start, stop))
    
