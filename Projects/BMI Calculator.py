print("=== BMI Calculator ===")
print("How do you wanna calculate your BMI ?")
print(f"1. US Units\n2. Metric Units")

# weight / height^2
choice = int(input("Enter your choice : "))

# age validation
def validateAge():
    age = int(input("\nEnter your age : "))
    return 2 <= age <= 100

# Bmi classification
def classify_bmi(bmi):
    print(f"\nYour BMI is : {bmi:.1f}kg/m\u00B2")
    if bmi < 16:
        print("You are Severe Thinness.")
    elif 16 <= bmi <= 17:
        print("You are Moderate Thinness.")
    elif 17 <= bmi <= 18.5:
        print("You are Mild Thinness.")
    elif 18.5 <= bmi <= 25:
        print("You are Normal.")
    elif 25 <= bmi <= 30:
        print("You are Overweight.")
    elif 30 <= bmi <= 35:
        print("You are in Obese Class 1.")
    elif 35 <= bmi <= 40:
        print("You are Obese Class 2.")
    elif bmi > 40:
        print("You are Obese Class 3.")
    else:
        print("You are underweight.")


# us unit
def usUnits():
    if not validateAge():
        print("Please enter a valid age")
        return
    weight = float(input("Enter your weight in pounds : "))
    height = float(input("Enter your height in inches : "))
    height = height * 12  # convert to inches
    bmi = 703 * ( weight / height **2)
    classify_bmi(bmi)


# metric unit
def metricUnits():
    if not validateAge():
        print("Please enter a valid age")
        return
    weight = float(input("Enter your weight in kg : "))
    height = float(input("Enter your height in cm : "))
    height = height / 100 # convert to meter
    bmi = weight / height **2
    classify_bmi(bmi)


if choice == 1:
    usUnits()
elif choice == 2:
    metricUnits()
else:
    print("Invalid Choice.")




'''
Unicode Characte code
    \u00B2 → ² (superscript 2)
    \u00B3 → ³ (superscript 3)
    \u00B0 → ° (degree symbol)
    \u03C0 → π (pi)
    \u221E → ∞ (infinity)
    \u00B1 → ± (plus/minus)
'''