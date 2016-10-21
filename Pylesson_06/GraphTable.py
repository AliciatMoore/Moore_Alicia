integer = int(input("Please enter an integer: "))
size = int(input("Please enter the size of the table: "))
for i in range(1, size+1):
    print("{:<5}{:<5}".format(i,i*integer))
