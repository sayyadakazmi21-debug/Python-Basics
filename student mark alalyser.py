empty_list = []
print(empty_list)

marks = [85, 72, 90, 66, 78]
print("Student Marks:", marks)

sample_marks = [10, 20, 30] * 2
print("Repeated Sample Marks:", sample_marks)

print("Number of marks:", len(marks))

print("First mark:", marks[0])
print("Last mark:", marks[-1])

print("First three marks:", marks[0:3])

print("Reversed Marks:", marks[::-1])


def match_marks(mark_list):
    count = 0
    matched = []

    for mark in mark_list:
        text = str(mark)

        if len(text) > 1 and text[0] == text[-1]:
            count += 1
            matched.append(mark)

    print("Matching marks:", matched)
    return count


count = match_marks([88, 72, 99, 65, 77])
print("Number of matching marks:", count)


total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("Sum:", total)
print("Average:", average)


marks.sort()

print("Smallest:", marks[0])
print("Largest:", marks[-1])

print()
print("===== STUDENT MARKS LIST ANALYZER =====")
print("Sorted Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Lowest Mark:", marks[0])
print("Highest Mark:", marks[-1])
print("=======================================")