# Finding cost of the orange

buying_price=int(input("Enter the cost of the orange"))
selling_price=int(input("Enter the selling price"))
# FInding the profit
if selling_price>buying_price:
    print("You have earned a profit of",selling_price - buying_price)
else:
    print("you are under loss")