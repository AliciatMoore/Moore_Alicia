
def song(word, repeat):
    output = word
    for i in range(1, repeat + 1):
       output = output + " "
    print(output)
    
song("Na",4)
song("Na", 4)
song("Hey", 3)
song("Goodbye!",1)
