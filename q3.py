
def areaCircle(pi: float, radius: float) -> float:
    area: float = pi * (radius**2)
    return area


pi = float(input("Enter the value of pi: "))
radius = float(input("Enter the radius of circle: "))
area : float = areaCircle(pi, radius)
print("Area of circle is", area)
