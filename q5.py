
def fahrenheitToCelsius(fahrenheit:float)->float:
    convert1 : float = (fahrenheit - 32) / 1.8
    return convert1

def celsiusToFahrenheit(celsius:float)->float:
    convert2:  float = (celsius*1.8) + 32
    return convert2



fahrenheit = float(input("Enter the temperature in fahrenheit: "))
celsius = float(input("Enter the temperature in celsius: "))
print("\n")
print("((After Conversion))")
print(fahrenheitToCelsius(fahrenheit), "C")
print(celsiusToFahrenheit(celsius), "F")