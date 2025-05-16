## To run the program:
1. Ensure pandas, random, sys and all other appropriate extensions are downloaded
2. Place the 'clean_grocery_Items_with_Prices.csv' file in the same directory
3. Run the command: python shopping_cart.py

## User Guide:
1. Start by entering your budget when prompted
2. Available commands:
   - Type an item name to add it to your cart
   - Type 'view' to see current cart contents
   - Type 'remove' to remove an item from your cart
   - Type 'coupon' to apply a random discount (5-30%)
   - Type 'checkout' to complete your purchase
3. Output:
   - When adding items, the program will confirm addition or notify if an item is unavailable
   - The 'view' command displays all items, their prices, total cost, and remaining budget
   - Error messages will display when you try to exceed your budget
