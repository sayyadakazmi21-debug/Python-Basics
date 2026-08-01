def greet_customer():
    print("Welcome to the Art Supplies Store!")
    print("Get your colours, brushes, and paper here.")

greet_customer()

price = float(input("Enter the price per art item in dollars: "))
items = int(input("Enter the number of art items bought: "))

def calculate_total(price, items):
    return price * items

total = round(calculate_total(price, items), 2)

print("Total Cost:", total)

paid = float(input("Enter the amount paid by the customer: "))

def calculate_change(paid, total):
    return paid - total

change = round(calculate_change(paid, total), 2)

def thank_you_message(items):
    if items >= 5:
        return "Great choice! You picked many art supplies for your project."
    return "Thanks for shopping at the art supplies store!"

message = thank_you_message(items)

print()
print("===== ART SUPPLIES BILL =====")
print("Price Per Item:", price)
print("Items Bought:", items)
print("Total Cost:", total)
print("Amount Paid:", paid)
print("Change Due:", change)
print(message)
print("=============================")