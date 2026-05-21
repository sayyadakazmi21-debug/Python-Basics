char = input("Enter a single character: ")
if len(char) == 1:
    ascii_value = ord(char)
    print("ASCII Value:", ascii_value)
if char.isupper():
        print("Character Type: Uppercase Letter")
elif char.islower():
        print("Character Type: Lowercase Letter")
elif char.isdigit():
        print("Character Type: Digit")
else:
        print("Character Type: Special Character")
 