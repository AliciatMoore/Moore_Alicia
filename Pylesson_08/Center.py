a = input("Please enter the first word: ")
b = input("Please enter the second word: ")
c = input("Please enter the third word: ")

def makeCenter(word):
    if len(word) >= 20:
        return word
    else:
        return makeCenter(" " + word + " ")
print(makeCenter(a))
print(makeCenter(b))
print(makeCenter(c))
