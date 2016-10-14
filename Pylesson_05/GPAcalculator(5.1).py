Math = input("Enter your letter grade for math:")
English = input("Enter your letter grade for English:")
History = input("Enter your letter grade for History:")
Biology = input("Enter your letter grade for Biology:")
Spanish = input("Enter your letter grade for Spanish:")
Chemistry = input("Enter your letter grade for Chemistry:")
Photography = input("Enter your letter grade for Photography:")

def calcPoints(grade):
    if grade == "A":
        return 4.0
    elif grade == "B":
        return 3.0
    elif grade == "C":
        return 2.0
    elif grade == "D":
        return 1.0
    elif grade == "F":
        return 0
M = calcPoints(Math)
E = calcPoints(English)
H = calcPoints(History)
B = calcPoints(Biology)
S = calcPoints(Spanish)
C = calcPoints(Chemistry)
P = calcPoints(Photography)
print("Your GPA is", (1/7)*(M+E+H+B+S+C+P))
