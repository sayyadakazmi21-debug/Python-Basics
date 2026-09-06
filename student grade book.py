student={"sayyada":95,"arnav":86,"arya":77,"sam":99}
total=0
for name,score in student.items():
    total=total+score
avg = total/len(student)
top=max(student,key=student.get)
bot=min(student,key=student.get)
print("average is",avg)
print("top scorer is",student[top])
print("bottom socrer is",student[bot])
for name,score in student.items():
     print(name,"=",score)

   