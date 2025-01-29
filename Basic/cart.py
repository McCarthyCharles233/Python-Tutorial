# Problem 1: Calculate the Total Cost of Items in a Shopping Cart
# Problem Statement:
# You are building a program for an online store. The user adds items to their shopping cart,
# and each item has a name, quantity, and price. Your task is to calculate the total cost of
# all items in the cart.

cart = [
    {"name": "Apple", "quantity": 3, "price": 0.50},
    {"name": "Banana", "quantity": 2, "price": 0.30},
    {"name": "Orange", "quantity": 5, "price": 0.40}
]

total_cost = 0

for i in cart:
    subtotal = i["quantity"] * i["price"]
    total_cost += subtotal
print(total_cost)








