
def areaCalculator(length:float,width:float)->float:
    areaRectangle = length * width 
    return areaRectangle;

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))
print("Area of rectangle is",areaCalculator(length,width))