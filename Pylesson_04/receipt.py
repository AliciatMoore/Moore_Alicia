def printf(food,space,price):
    print("*"+"{:>17}{:.<9}{:10.2f}".format(food,space,price))
food1 = input("Please enter item 1: ")
price1 = float(input("Please enter the price: "))
space = " "

food2 = input("Please enter item 2: ")
price2 = float(input("Please enter the price: "))

food3 = input("Please enter item 3: ")
price3 = float(input("Please enter the price: "))

tprice = price1+price2+price3

tax = tprice*.07


toprice = tprice+tax
print("\n")
print("<<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>>")
print("\n")
printf(food1,space,price1)
printf(food2,space,price2)
printf(food3,space,price3)
print("\n")
printf("Subtotal:",space,tprice)
printf("Tax:",space,tax)
printf("Total:",space,toprice)

print("____________________________________________")
print("* Thank you for your support *")
