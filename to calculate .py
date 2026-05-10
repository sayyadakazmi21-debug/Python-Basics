amount=int(input("enter your amount"))
Rs100_notes= amount//100
Rs50_notes= (amount%100)//50
Rs10_notes= ((amount%100)%50)//10
print("The total no of notes needed is",Rs100_notes+Rs50_notes+Rs10_notes)