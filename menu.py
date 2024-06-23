# Menu dictionary for Sup Dogs
menu = {
    "WORLD CLASS APPS": {
        "Cheesy Tots": {
            "Regular": 8.99,
            'Add Chopped Bacon for': 10.49
        },
        "World Class Bacon Cheese Fries": 8.99,
        "Jalapeño Popper Tots": 8.99,
        "Macho Nachos": {
            "Regular": 8.99,
            'Add Buffalo Chicken': 11.99
        },
        "Buffalo Boneless Wings": 8.99,
        "Pepperoni Pizza Fries or Tots": 8.99,
        "Fried pickles fries": 8.99,
        "Taco Tots": 8.99,
        "Green Bean Fries": 8.99,
        "Funnel Cake Stix": 8.99

    },
    "SUP DOGS": {
        "Sup Dogs Combo": 6.99,
        "Simple Dog Combo": 6.99,
        "Slaw Dog Combo": 6.99,
        "Old School Dog Combo": 6.99,
        "Chili Cheese Dog Combo": 6.99,
        "Spicy Hot Dog Combo": {
            "Regular": 7.99,
            "Double the Dog": 9.99
        }
    },
    "SPECIALTY SUP DOGS": {
        "Smokehouse Dog Combo": {
            "Regular": 6.99,
            "Double the Dog": 8.49
        },




        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "HAND-SMASHED BURGERS": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    },
    "CHICKEN STRIPS & SANDWICHES": {
      "Buffalo Chicken Sandwich Combo": 9.99,
      "Hot Honey BBQ Chicken Sandwich Combo": 9.99,
      "Juicy Chicken Strips Combo": 9.99,
      "Sup-Fil-A Sandwich Combo": 9.99,
      "Buffalo Chicken Strips Combo": 9.99,
      "Buffalo Chicken Chopped Salad": 9.99

    },
    "OUR FAMOUS DRINKS": {
        "Orange Sup Crush": 7.00,
        "Grapefruit Sup Crush": 7.00,
        "Sup Swirl": 7.00

    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("Welcome to Sup Dogs Chapel Hill.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"\nYou selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"\nWhat {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + " - " + key2) 
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2:.2f}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value:.2f}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            item_selection = input("\nType the item number: ")

            # 3. Check if the customer typed a number
            if item_selection.isdigit():

                # Convert the menu selection to an integer
                item_selection = int(item_selection)


                # 4. Check if the menu selection is in the menu items
                if item_selection in menu_items:

                    # Store the item name as a variable
                    item_name = menu_items[item_selection]["Item name"]
                    item_price = menu_items[item_selection]["Price"]


                    # Ask the customer for the quantity of the menu item
                    quantity_input = input(f"How many {item_name}s would you like? (default is 1): ")


                    # Check if the quantity is a number, default to 1 if not
                    if not quantity_input.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity_input)

                    # Add the item name, price, and quantity to the order list
                    order.append({"Item name": item_name, "Price": item_price, "Quantity": quantity})


                    # Tell the customer that their input isn't valid


                # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input

                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing


    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.






