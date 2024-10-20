# display_inventory.py

def display_inventory(inventory):
    print("\nShoe Inventory:")
    if not inventory:
        print("No shoes in the inventory.")
    else:
        for i, (name, quantity, price) in enumerate(inventory, start=1):
            print(f"{i}. Name: {name}, Quantity: {quantity}, Price: ${price:.2f}")
    print()
