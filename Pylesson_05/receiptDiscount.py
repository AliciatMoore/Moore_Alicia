item1 = input("Enter the first item: ")
p1 = int(input("Enter the price:"))
item2 = input("Enter the second item: ")
p2 = int(input("Enter the price:"))
item3 = input("Enter the third item: ")
p3 = int(input("Enter the price:"))
item4 = input("Enter the fourth item: ")
p4 = int(input("Enter the price:"))

def format(one, two):
    print("{:<10}{:.>8}{:0.2f}".format(one, "$", two))
          
print("<<<<<<<<<< Receipt >>>>>>>>>>")
format(item1, p1)
format(item2, p2)
format(item3, p3)
format(item4, p4)
print("\n")

sub = p1 + p2 + p3 + p4
format("Subtotal", sub)

def discount():
    global sub
    if sub > 2000:
        return sub*.15
    if sub < 2000:
        return 0
format("Discount", discount())

tax = (sub - discount())*.07
format("Tax", tax)
format("Total", sub - discount() + tax)
print("______________________________")
print("* Thank you for your support *")

