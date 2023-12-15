
print("This program to calculate the BMI of an individual\n")
name = input("Enter Your Name:")
weight = float(input("Enter Your Weight in Killograms:"))
height = float(input("Enter Your Height in Meters:"))

bmi = weight / (height ** 2 )

if bmi < 25:
    print(f"{name} is Underweight by {bmi} BMI")
else:
    print(f"{name} is Overweight by {bmi} BMI")