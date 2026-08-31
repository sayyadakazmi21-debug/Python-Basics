x=["pencil","eraser","notebook","ruler"]
count=[12,0,8,5,]
inventory={x:count for x , count in zip (x,count)}
print("full inevntory",inventory)

y=[x for x in x if inventory[x]>0]
print("items in stock",y)

z=input("which item do u wnna buy")
if z not in inventory or inventory[z]==0:
    print("out of stock, stopping checking")
    exit()


price=[10,15,40,33]
markup=int(input("enter the markup amount: "))
mak_up=list(map(lambda p:p+ markup,price))
print("marked up prices: ",mak_up)

index=x.index(y)
choosen_price=mak_up[index]

print("price of",y,"after markup is",choosen_price)


print("=========== SCHOOL INVENTORY CHECKER==========")
print("item bought",y)
print("price paid",choosen_price)