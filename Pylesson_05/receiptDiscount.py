item1 = input("Enter the first item: ")
p1 = int(input("Enter the price:"))
item2 = input("Enter the second item: ")
p2 = int(input("Enter the price:"))
item3 = input("Enter the third item: ")
p3 = int(input("Enter the price:"))
item4 = input("Enter the fourth item: ")
p4 = int(input("Enter the price:"))

def receipt(one, two):
    print("{:<10}{:.>8}{:0.2f}".format(one, "$", two))
          
print("<<<<<<<<<< Receipt >>>>>>>>>>")
receipt(item1, p1)
receipt(item1, p1)
receipt(item1, p1)
receipt(item1, p1)
print("\n")

sub = p1 + p2 + p3 + p4
receipt("Subtotal", sub)

if sub > 2000:
    discount = sub*.07
if sub < 2000:
    discount = 0
receipt("Discount", discount)

tax = (sub - discount)*.15
receipt("Tax", tax)
receipt("Total", sub - discount + tax)
print("______________________________")
print("* Thank you for your support *")

