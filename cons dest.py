class employee:

    def __init__(self):
        print("employee created")
    

    def __del__(self):
        print("destructor called")


obj1= employee()
print(obj1)

del obj1
#print(obj1)
# this line will givr error


    