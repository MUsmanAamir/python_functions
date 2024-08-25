def calPercentage(numerator:float , denominator:float)->float:
    percentage : float= (numerator / denominator) * 100
    return percentage

numerator = float(input("Enter the numerator value: "))
denominator = float(input("Enter the denominator value: "))
percenage : float = calPercentage(numerator,denominator)
print(numerator,"is", percenage,"%" ,"of", denominator)