def calPercentage(numerator:float , denominator:float)->float
    percentage : float= (numerator / denominator) * 100
    return percentage

numerator = float(input("Enter the numerator value: "))
denominator = float(input("Enter the denominator value: "))
print(numerator,"is", calPercentage(numerator,denominator),"%" ,"of", denominator)