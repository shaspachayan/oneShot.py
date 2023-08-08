"""
Write a program that calculates the Body Mass Index (BMI) of a person based on their weight (in kilograms) and height (in meters).
The BMI is calculated using the formula: BMI = weight / (height * height).

Your program should:

Prompt the user to enter their weight (in kilograms) and height (in meters).
Calculate the BMI using the provided formula.
Display a message indicating the BMI category based on the calculated value:
BMI less than 18.5: "Underweight"
BMI between 18.5 and 24.9: "Normal weight"
BMI between 25 and 29.9: "Overweight"
BMI 30 or greater: "Obese"
"""


def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi


def check_bmi(bmi):
    if bmi < 18.5:
        print(f"Your BMI is {bmi: 2f} and you are underweight")
    elif 18.5 < bmi < 24.9:
        print(f"Your BMI is {bmi: 2f} and your weight is normal")
    elif 25 < bmi < 29.9:
        print(f"Your BMI is {bmi: 2f} and you belongs to overweight")
    else:
        print(f"Your BMI is {bmi: 2f} and you need to loose weight seriously")


weight = float(input("Enter the weight in kg : "))
height = float(input("Enter the height in meters : "))

bmi = calculate_bmi(weight, height)
check_bmi(bmi)