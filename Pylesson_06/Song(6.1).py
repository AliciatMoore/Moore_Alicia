def song(word, repeat):
    output = ""
    for i in range(repeat + 1):
        output = output + str(i) + " "
    print(word * i)

song("Na",4)
song("Na", 4)
song("Hey", 3)
song("Goodbye!",1)
