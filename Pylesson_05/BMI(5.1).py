h = int(input("Please enter the height in inches: "))
w = int(input("Please enter the weight in pounds: "))
BMI = 0
def calcBMI():
    global BMI, condition
    BMI = 703*(w/h**2)
    if BMI < 18.5:
        condition = "Underweight"
    elif 18.5 < BMI < 24.9:
        condition = "Normal"
    elif 25 < BMI < 29.9:
        condition = "Overweight"
    elif 29.9 < BMI < 34.9:
        condition = "Obese"
    elif 35 < BMI < 39.9:
        condition = "Very Obese"
    elif BMI > 39.9:
        conditon = "Morbidly Obese"
calcBMI()
print("Your BMI is: ", BMI)
print("You are",condition)


        
        
