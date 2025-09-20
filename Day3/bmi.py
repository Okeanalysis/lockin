weight= int(input("what is your weight in kg: "))
height= float(input("what is your height in m: "))

bmi= round(weight/height**2)

if bmi < 18.5:
    print("your bmi is",bmi,"your are underweight")
elif bmi >18.5 and bmi <25:
    print("your bmi is",bmi,"you have a normal weight")
elif bmi >25 and bmi < 30:
    print("your bmi is",bmi,"your are overweight")
elif bmi >30 and bmi <35:
    print("your bmi is",bmi,"your are obese")
else:
    print("your bmi is",bmi,"your are clinically obese")