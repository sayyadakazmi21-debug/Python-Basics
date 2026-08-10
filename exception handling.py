try:
    num=int(input("enter num ")) 
    print("the num ",num)
except ValueError as hi:
    print("exception is",hi)
