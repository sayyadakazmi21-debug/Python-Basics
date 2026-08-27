h = ("Reading", True, 7, 20.5)
print(h)

w = (1, 0, 1, 1, 0, 1, 1)
print(w)

print("Total days tracked:", len(w))
print("Day 1 status:", w[0])
print("Day 4 status:", w[3])

a = w[0:3]
print("First three days:", a)

b = w[5:7]
print("Weekend days:", b)

w = w + (1,)
print("After adding one more day:", w)

c = w.count(1)
m = w.count(0)

print("Completed days:", c)
print("Missed days:", m)

d = 0
n = 0

for i in range(len(w)):
    if w[i] == 1:
        d += 1
    else:
        n += 1

if d > n:
    print("Great habit progress!")
else:
    print("Try to be more consistent!")

print("")
print("===== WEEKLY HABIT TRACKER =====")
print("Habit Name:", h[0])
print("Weekly Record:", w)
print("Completed:", d)
print("Missed:", n)
print("================================")