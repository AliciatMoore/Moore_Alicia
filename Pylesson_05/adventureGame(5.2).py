
choice = input("Would you like to buy..."+
                "\n A ship"+
                "\n A house: ")

if choice == ("A ship" or "A house"):
    Type = input("Would you like..."+
                        "\n A battleship" +
                        "\n or A caravel: ")
    if Type == "A battleship":
        pay = input("Would you pay $45,000,000 for it? Yes or No")
        if pay == "Yes":
                print("You now have a battleship!")
        else:
                print("Thank you for looking around!")
    else:
        pay = input("Would you pay $1,000,000 for it? Yes or No")

        if pay == "Yes":
            
                print("You now have a caravel!")
        else:
                print("Thank you for looking around!")
        
else:
    Type = input("Would you like..."+
                        "\n A castle" +
                        "\n A bungalow: ")
    if Type == "A castle":
        pay = input("Would you pay $45,000,000 for it? Yes or No")
        if pay == "Yes":
                print("You now have a castle!")
        else:
                print("Thank you for looking around!")
    else:
        pay = input("Would you pay $20,000,000 for it? Yes or No")
        if pay == "Yes":
                print("You now have a bungalow!")
        else:
                print("Thank you for looking around!")
