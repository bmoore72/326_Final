# repo 
#hi

import pandas as pd 
import random

# Read the CSV file into a DataFrame
#df = pd.read_csv('new_Groceries_dataset.csv')

# Remove duplicate rows
#df.drop_duplicates(inplace=True)

# Save the DataFrame back to a CSV file
#df.to_csv('cleaned_groceries.csv', index=False)

grocery_item_df = pd.read_csv('clean_grocery_Items_with_Prices.csv')

class ShoppingCart:
    "Class that manages a persons shopping cart based on their budget with additional features"

    def __init__(self, grocery_item_df, budget):
        """
        initialize shopping cart class with item dataframe and budget 

        grocery_item_df: items in dataframe with their prices
        budget: the persons budget they are following
        """
        
        self.grocery_item_df = grocery_item_df
        self.budget = budget
        self.cart = []
        self.wish_list = []
        self.price_total = 0.0
       

    def add_item(self, item_name):
        """
        adds item to the cart if it's in stock(in csv file) and within their budget
        if the item is not found, it gets added to the wishlist

        item_name: name of the item they want to add

        raises ValueError if adding an item exceeds their budget        
        """

        row = self.grocery_item_df[self.grocery_item_df['item_Description'].str.lower() == item_name.lower()]

        if row.empty:
            print(f"{item_name} is out of stock. It will be added to your wishlist.")
            self.wish_list.append(item_name)
            return

    price = row['Price'].values[0]

    if self.price_total + price > self.budget:
            raise ValueError(f"Can not add {item_name} - You are over budget")

    self.cart.append((item_name, price))
    self.price_total += price

    def coupon(self):
        """
        Applies a random discount between 5% and 30%.
    
        returns discount
        
        """
        percent = random.randint(5, 30)
        discount = self.price_total * (percent / 100)
        self.price_total -= discount

        print(f"A {percent}% coupon has been applied to your total")

        return discount
    
    def remove(self, item_name):
        """
        removes item from the cart if it exists in the cart
        if it does not exist, it raises an error

        item_name: name of the item to remove
        """
        for item in self.cart:
            if item[0].lower() == item_name.lower():
                self.cart.remove(item)
                self.price_total -= item[1]
                print(f"{item_name} has been removed from your cart.")
                return

        raise ValueError(f"{item_name} is not in your cart.")
    
    def remaining_budget(self): # Displays how much money user has left to spend
        return self.budget - self.price_total

    def view_cart(self):
        """
        Displays all items in the cart with their prices and the total.
        Offers checkout option if the cart is not empty.
        """
        # Check if cart is empty
        if not self.cart:
            print("Your cart is empty.")
            return
        
        # Display cart contents    
        print("Your cart contains the following items:")
        
        # Loop through each item and display its name and price
        for item, price in self.cart:
            print(f"{item}: ${price:.2f}")
        
        # Display total price and remaining budget
        print(f"Total: ${self.price_total:.2f}")
        print(f"Remaining budget: ${self.budget - self.price_total:.2f}")
        
        # Ask if user wants to checkout and process their response
        checkout_choice = input("\nWould you like to checkout now? (y/n): ")
        if checkout_choice.lower() == 'y':
            self.checkout()
            
    def clear_cart(self): # removes all items from cart
        self.cart = [] 
        self.price_total = 0.0 
        print("Your cart has been cleared")
        
# interactive, user is speaking with program to add itmes to cart 
if __name__ == "__main__":
    try:
        grocery_item_df = pd.read_csv('clean_grocery_Items_with_Prices.csv') # get grocery items with prices
        
    while True: 
        try: 
            budget = float(input("Please enter your budget:$"))
            if budget <= 0:
                print("Invalid Entry. Budget must be greater than 0.")
                continue
            break
        except ValueError:
            print ("Please enter a valid amount for your budget.")
    
    cart = ShoppingCart(grocery_item_df, budget)  # create shoppign cart with users budget        

    
    while True: 
        item = input("Enter an item to add to your cart (or type 'done' to finish)")
        if item.lower() == 'done': 
            break 
        try:
            cart.add_item(item)
            print(f"{item} add! Current Total: ${cart.price_total:.2f}")
        except ValueError: 
            print("Invalid entry. Please try again.")
            
        print("\nFinal Cart Summary:")
        for i, (item, price) in enumerate(cart.cart, 1): 
            print