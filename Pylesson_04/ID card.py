def printq(a,b):
    print("*{:>14}{:>18} *".format(a,b))
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
title = input("Enter your title: ")
schoolSite = input("Enter the school site: ")
year = input("Enter the school year: ")
subject = input("What is your subject?")


print("***********************************")
printq(schoolSite,year)
printq(fname,lname)
printq(title,subject)
    
print("***********************************")
