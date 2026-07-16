pet_tasks = ["feed pet", "water", "clean", "walk"]
original_count = len(pet_tasks)
completed_count = 0
while len(pet_tasks) > 0:
    current_task = pet_tasks[0]
    answer = input("did you do " + current_task + "? ")
    if answer == "yes":
        pet_tasks.pop(0)
        completed_count = completed_count + 1
        print("left:", len(pet_tasks))
print("loop time")
safety_counter = 0
while True:
    print("stuck")
    safety_counter = safety_counter + 1
    if safety_counter == 3:
        print("saved")
        break
print("all original:", original_count)
print("done:", completed_count)
print("left:", len(pet_tasks))