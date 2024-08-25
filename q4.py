def areaCube(edge:float)->float:
    area : float = 6 * (edge**2)
    return area

edge = float(input("Enter the size of edge: "))
print("Area of cube is",areaCube(edge))