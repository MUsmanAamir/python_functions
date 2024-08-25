
def ageCalculator(birthYear:int, currentYear:int)->int:
    age: int = currentYear - birthYear
    return age;


birthYear = int(input("Enter your birth year: "))
currentYear = int(input("Enter the current year: "))
age : int = ageCalculator(birthYear, currentYear) 
print("Your age:",age)
