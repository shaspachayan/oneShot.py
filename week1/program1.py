"""
Exercise: Create a program that calculates the total cost of items in a shopping cart.
Allow users to input item names, prices, and quantities.
"""


def calculate_total_cost():
    num_items = int(input("How many items are in your shopping cart? "))
    total_cost = 0

    for i in range(num_items):
        item_name = input(f"Enter the name of item {i + 1}: ")
        item_price = float(input(f"Enter the price of {item_name}: "))
        item_quantity = int(input(f"Enter the quantity of {item_name}: "))

        item_total = item_price * item_quantity
        total_cost += item_total

        print(f"Added {item_quantity} {item_name}(s) at ${item_price:.2f} each. Subtotal: ${item_total:.2f}")

    print(f"Total cost of items in your shopping cart: ${total_cost:.2f}")


calculate_total_cost()