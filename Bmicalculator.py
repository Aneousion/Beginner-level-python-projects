print("""

Body Mass Index Calculator
From github.com/aneousion

""")

# INPUT YOUR HEIGHT IN METERS
# float() IS USED TO CONVERT THE INPUT TO A FLOATING POINT NUMBER

height = float(input("What is your height in m?: "))

# INPUT YOUR WEIGHT IN KILOGRAMS
# float() IS USED TO CONVERT THE INPUT TO A FLOATING POINT NUMBER

weight = float(input("What is your weight in kg?: "))


# BODY MASS INDEX(BMI) IS YOUR WEIGHT DIVIDED BY 2 TIMES YOUR HEIGHT
# round() WILL ROUND THE NUMBER TO THE NEAREST WHOLE NUMBER
bmi = round(weight/(height ** 2))

"""
BMI 18 and below – Underweight
BMI 18 to 25 – Normal weight
BMI 25 to 30 – Overweight
BMI 30 to 35 – Obese
BMI 35 and above – Clinically obese
"""

if bmi < 18:
	print(f"Your BMI is {bmi}, you are underweight")
elif bmi >= 35:
		print(f"Your BMI is {bmi}, you are clinically obese")
elif bmi >= 30:
		print(f"Your BMI is {bmi}, you are obese")
elif bmi >= 25:
		print(f"Your BMI is {bmi}, you are overweight")
elif bmi >= 18:
		print(f"Your BMI is {bmi}, you have a normal weight")
