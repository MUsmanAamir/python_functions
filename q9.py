def calculateVolumeCylinder(radius:float, height:float, pi:float)->float:
    volumeCylinder : float = pi * (radius**2) * height
    return volumeCylinder

radius = float(input("Enter the height of cylinder: "))
height = float(input("Enter the radius of cylinder: "))
pi  = float(input("Enter the value of pi: "))
volume : float = calculateVolumeCylinder(radius,height,pi)

print(f"The volume of Cylinder: {volume}")