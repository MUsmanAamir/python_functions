
def areaCalculator(length:float,width:float)->float:
    areaRectangle = length * width 
    return areaRectangle;

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))
rectangle = areaCalculator(length,width)
print("Area of rectangle is",rectangle)