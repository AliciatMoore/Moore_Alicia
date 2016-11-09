word = input("Please enter a word: ")
stop = len(word)
start = 0
def tree(word, start, stop):
    if start <= stop:
        print ("{:>10}".format(word[0 : start]))
        start += 1
        tree(word, start, stop)

tree(word, start, stop)
    
