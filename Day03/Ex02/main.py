# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = int(weight) / (float(height) * float(height))
if BMI < 18.5:
    status = "are underweight"
elif BMI > 18.5 and BMI < 25:
    status = "have a normal weight"
elif BMI > 25 and BMI < 30:
    status = "are slightly overweight"
elif BMI > 30 and BMI < 35:
    status = "are obese"
elif BMI > 35:
    status = "are clinically obese"

BMI = round(BMI)
print(f"Your BMI is {BMI}, you {status}.")