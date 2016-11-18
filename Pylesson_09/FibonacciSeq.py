num = int(input("Please enter your starting number: "))
size = int(input("Please enter your sequence size: "))

seq = []

j = 0
for i in range(0, size):
    if i == 0 or i == 1:
        seq[i] = num 
    else:
        seq[i] = seq[i - 2] + seq[i - 1]
    print (str(seq[i]) + " ")
        
