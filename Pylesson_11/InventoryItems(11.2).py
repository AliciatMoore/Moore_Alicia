import random
class item:
    def __init__(self, M = "", N = "", C = "", p = ""):
        self.manu = M
        self.name = N
        self.category = C
        self.price = p
        self.UPC = random.randint(1000000000, 9999999999)

    def __str__(self):
        return "Manufacturer: " + self.manu + \
               "\nName: " + self.name + \
               "\nCategory: " + self.category + \
               "\nPrice: " + str(self.price) + \
               "\nUPC: " + str(self.UPC)

def main():
    
    manu = input("Please enter the manufacturer: ")
    name = input("Please enter the name: ")
    choose = input("Will you be entering category and price information? y or n ")

    if choose == "n":
        item1 = item(manu, name)
    if choose == "y":
        category = input("Please enter the category: ")
        price = input("Please enter the price: ")
        item1 = item(manu, name, category, price)
    print(item1.__str__())
main()

    
    
    

    
    
    
        
