
height = input("Enter your height in cm: ")

weight = input("Enter your weight in kg: ")


h = float(height) / 100  
w = float(weight)

bmi = w / (h ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are classified as: {category}")
