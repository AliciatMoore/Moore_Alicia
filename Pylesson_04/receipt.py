def printf(food,price):
    print("*"+"{:>17} ........{:10.2f}".format(food, price))
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
printf(food1,price1)
printf(food2,price2)
printf(food3,price3)
print("\n")
printf("Subtotal:",tprice)
printf("Tax:",tax)
printf("Total:",toprice)

print("____________________________________________")
print("* Thank you for your support *")
