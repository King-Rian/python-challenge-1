For this project, I designed an interactive ordering system from a restaurant menu, using the skills I have learned in Python. This consisted of two components: the order system and the order receipt. 

For the Order System, you start by initializing an order list. Then, prompt the user to select a menu item and validate that the input is a number, converting it to an integer. Use an if-else statement to ensure the selection is valid, extract the item name from the menu_items dictionary, and prompt the user for the quantity, defaulting to 1 if invalid. Append the selected item, price, and quantity to the order list as a dictionary. Implement a match-case statement to handle whether the user wants to continue ordering, ensuring to convert the input case.

For the Order Receipt, iterate through the order list using a for loop, extracting and saving each order's key values. Calculate and create formatting spaces, then print the order details with proper formatting. Use list comprehension to compute the total price, which is then printed on the screen.

