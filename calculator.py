
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    if b==0:
        print("error")
    return(a/b)

try:
   a=int(input("enter number: "))
   b=int(input("enter number: "))
   opp=input("enter the opperator ")

   if opp=="+":
    print(add(a,b))
   if  opp=="-":
    print(sub(a,b))
   if  opp=="*":
    print(mul(a,b))
   if  opp=="/":
    print(div(a,b))

except ValueError:
 print("error")





