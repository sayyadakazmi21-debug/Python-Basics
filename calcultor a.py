def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("=" * 36)
print("     🧮 FUNCTION CALCULATOR")
print("=" * 36)
print("Operations: add | subtract | multiply | divide")
print()

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation: ").strip().lower()

    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    elif operation == "divide":
        try:
            result = divide(a, b)
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            result = None
    else:
        print("Unknown operation.")
        result = None

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Please enter numbers only.")