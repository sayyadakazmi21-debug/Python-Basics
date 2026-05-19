math=int(input("enter ur  math marks"))
phy=int(input("enter ur phy marks"))
chem=int(input("enter ur  chem marks"))
cs=int(input("enter ur Cs  marks"))
eng=int(input("enter ur english marks"))
avg=int((math+phy+chem+cs+eng)/5 )
print("avg is ",avg)
if avg not in range(0,101):
    print("error ")



elif avg>=91 and avg<=100:
    print("your grade is A1")
elif avg>=90 and avg<= 80:
    print("your grade is A2")
elif avg>=79 and  avg<=60:
    print("your grade is A3") 
else:
    print("failed") 




