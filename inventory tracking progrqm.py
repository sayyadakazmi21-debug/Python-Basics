print("INVENTORY PACKING PROGRAM")
box_sizes = (50, 20, 5, 1)
log = []
total_items = 0
n = int(input("How many products? "))
count = 0
while count < n:
    print("\nProduct", count + 1)
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    if quantity <= 0:
        print("Invalid quantity!")
        continue
    total_items += quantity
    boxes = {}
    remaining = quantity
    i = 0
    while i < len(box_sizes):
        size = box_sizes[i]
        boxes[size] = remaining // size
        remaining = remaining % size
        i += 1
    log.append({"name": name, "boxes": boxes})
    count += 1
print("\nFINAL REPORT")
print("Products Processed:", count)
print("Total Items Packed:", total_items)
for size in box_sizes:
    print("\n", size, "-item boxes")
    for product in log:
        print(product["name"], ":", product["boxes"])