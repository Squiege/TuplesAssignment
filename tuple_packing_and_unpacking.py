# Task 1

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Harry", "Computer", 3)
]

def unpack_orders(orders):
    for i in orders:
        name, item, order_number = i
        print(f"Customer: {name}, Item: {item}, Order Number: {order_number}")

unpack_orders(orders)
