# Star Pyramid
print("STAR PYRAMID")
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Floyd's Triangle
print("\nFLOYD'S TRIANGLE")
rows = int(input("Enter number of rows: "))
num = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()

# Diamond Pattern
print("\nDIAMOND PATTERN")
rows = int(input("Enter number of rows: "))

if rows % 2 == 0:
    half = rows // 2
else:
    half = rows // 2 + 1

# Upper half
for i in range(1, half + 1):
    print(" " * (half - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Lower half
for i in range(half - 1, 0, -1):
    print(" " * (half - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()