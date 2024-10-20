# update_quantity.py

from display_inventory import display_inventory

def update_quantity(inventory):
    display_inventory(inventory)
    try:
        shoe_index = int(input("Enter the shoe number to update: ")) - 1
        if 0 <= shoe_index < len(inventory):
            action = input("Enter 's' to sell or 'a' to add: ").lower()
            amount = int(input("Enter the quantity: "))
            
            if action == 's':  # Sell shoes
                if inventory[shoe_index][1] >= amount:
                    inventory[shoe_index] = (inventory[shoe_index][0], inventory[shoe_index][1] - amount, inventory[shoe_index][2])
                    print(f'Sold {amount} of "{inventory[shoe_index][0]}".')
                else:
                    print("Not enough stock to sell.")
            elif action == 'a':  # Add shoes
                inventory[shoe_index] = (inventory[shoe_index][0], inventory[shoe_index][1] + amount, inventory[shoe_index][2])
                print(f'Added {amount} of "{inventory[shoe_index][0]}".')
            else:
                print("Invalid action. Please enter 's' or 'a'.")
        else:
            print("Invalid shoe number.")
    except ValueError:
        print("Please enter valid numbers.")
