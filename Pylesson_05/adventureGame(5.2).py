
def choose():
    choice = input("Would you like to buy..."+
                "\n A ship"+
                "\n A house: ")

    if choice == ("A ship" and "A house"):
        if choice == ("A ship"):
            Type = input("Would you like..."+
                        "\n A battleship" +
                        "\n or A caravel: ")
            if Type == "A battleship":
                print("You now have a battleship!")
            else:
                print("You now have a caravel!")
        else:
            Type = input("Would you like..."+
                        "\n A castle" +
                        "\n A bungalow: ")
            if Type == "A castle":
                print("You now have a castle!")
            else:
                print("You now have a bungalow!")
    else:
        print("Please choose a ship or a house.")
        choose()

choose() 
