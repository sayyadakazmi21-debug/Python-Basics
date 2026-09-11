grades = {
    "Alice": 88,
    "Bob": 73,
    "Sara": 95,
    "David": 81,
    "John": 67
}

print("=" * 38)
print("       📚 STUDENT GRADE BOOK")
print("=" * 38)

total = 0

for score in grades.values():
    total += score

average = total / len(grades)

print("Average:", f"{average:.1f}")

top = max(grades, key=grades.get)
bottom = min(grades, key=grades.get)

print("Top Student:", top, grades[top])
print("Bottom Student:", bottom, grades[bottom])

name = input("Enter student name: ")

score = grades.get(name, None)

if score is not None:
    print("Score:", score)
else:
    print("Student not found.")