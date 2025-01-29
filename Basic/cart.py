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








