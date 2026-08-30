x={"apple","mango","banana","avocado"}
y={"kiwi","mango","apple"}
print("basket1:",x)
print("basket2:",y)

x.add("orange")
print("new basket is ",x)
common=x.intersection(y)
print("common fruits : ",common)

import array as arr
count=arr.array('i',[3,5,2,4])
print("fruit count array:",count)

count.inser(0,1)
count.append(6)
print("new fruit count: ",count)


