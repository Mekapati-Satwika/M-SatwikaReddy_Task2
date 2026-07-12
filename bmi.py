try:
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be greater than zero.")
    else:
        bmi = weight / (height ** 2)

        print("BMI:", round(bmi, 2))

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Please enter numbers only.")