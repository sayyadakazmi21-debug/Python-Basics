number1=int(input("enter the first number"))
operator=("enter the operator (+,=,*,/)")
number2=int(input("enter the second number"))
if operator == "+":
     print(number1, "+", number2, "=", number1 + number2)
elif operator == "-":
     print(number1, "-", number2, "=", number1 - number2)
elif operator == "*":
     print(number1, "*", number2, "=", number1 * number2) 
elif operator == "/":
     print(number1, "/", number2, "=", number1 / number2)
else:
     print("Error")
   