def bmiCalcultor(height:float,weight:float)->float:
    bmi: float = weight / (height**2);
    return bmi


height = float(input("Enter height in meters (m): "))
weight = float(input("Enter weight in kilograms (kg): "))
bmi : float = bmiCalcultor(height,weight)
print("BMI:", bmi)