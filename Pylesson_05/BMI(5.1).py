h = int(input("Please enter the height in inches: "))
w = int(input("Please enter the weight in pounds: "))
BMI = 0
condition = 0
def calcBMI():
    global BMI, condition
    BMI = 703*(w/h**2)
    if BMI < 18.5:
        condition = "Underweight"
    elif BMI < 24.9:
        condition = "Normal"
    elif BMI < 29.9:
        condition = "Overweight"
    elif BMI < 34.9:
        condition = "Obese"
    elif BMI < 39.9:
        condition = "Very Obese"
    elif BMI > 39.9:
        conditon = "Morbidly Obese"
calcBMI()
print("Your BMI is: ", BMI)
print("You are",condition)


        
        
