weight = float(input())
height = float(input())

height = height / 100
bmi = weight / (height * height)
bmi = round(bmi, 1)

print("BMI:", bmi)
print("Underweight:", bmi < 18.5)
print("Normal:", bmi >= 18.5 and bmi < 25)
print("Overweight:", bmi >= 25)