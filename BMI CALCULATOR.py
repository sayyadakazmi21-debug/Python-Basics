weight=float(input("enter your weight in kg"))
height=float(input("enter your height in m"))
BMI=weight/(height**2)
if BMI<18.5:
    print("eat more u r underweight")
elif BMI >=18.5 and BMI<=24.9:
    print("ypu are healthy")
elif BMI >=25.0 and BMI <=29.9:
    print("loose a little weight you are overweight")
elif BMI >=30.0:
    print("you are obese , eat less")
else:
    print("error")    
