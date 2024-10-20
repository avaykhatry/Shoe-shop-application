# main.py

from display_inventory import display_inventory
from update_quantity import update_quantity

def main():
    inventory = []
    
    while True:
        print("1. Add Shoe")
        print("2. View Inventory")
        print("3. Update Shoe Quantity (Sell/Import)")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter the shoe name: ")
            try:
                quantity = int(input("Enter the quantity: "))
                price = float(input("Enter the price: $"))
                inventory.append((name, quantity, price))
                print(f'Shoe "{name}" added to inventory!')
            except ValueError:
                print("Please enter valid quantity and price.")

        elif choice == '2':
            display_inventory(inventory)

        elif choice == '3':
            if not inventory:
                print("No shoes in the inventory to update.")
            else:
                update_quantity(inventory)

        elif choice == '4':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
