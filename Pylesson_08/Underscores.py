sentence = input("Please enter a sentence: ")

def replace(sentence):
    if sentence.count(" ") == 0:
        return sentence
    else:
        return replace(sentence[0 : sentence.index(" ")] + "_" + sentence[sentence.index(" ")+1 : len(sentence)])      
print(replace(sentence))     
