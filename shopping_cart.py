# repo 
#hi

import pandas as pd 

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

        row = self.grocery_item_df[self.grocery_item_df['item_description'].str.lower() == item_name.lower()]

        if row.empty:
            print(f"{item_name} is out of stock. It will be added to your wish list.")
            self.wish_list.append(item_name)


        price = row.loc['Price']

        if self.price_total + price > self.budget:
            raise ValueError(f"Can not add {item_name} - You are over budget")

        self.cart.append((item_name, price))
        self.price_total += price

        

