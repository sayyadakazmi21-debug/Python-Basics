import random
playing=True
num=str(random.randint(0,9))
print("i will generetae a num frm 0 to 9 , guess the number 1 digit at a time")
print("the game neds when u get 1 hero")
while playing:
    guess=input("guess the num! \n")
    if num==guess:
        print("u win the game")
        print("the number was",num)
        break
    else:
        print("guess was worng try again")