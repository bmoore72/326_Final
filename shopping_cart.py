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
        
        self.grocery_items_df = grocery_item_df
        self.budget = budget
        self.cart = []
        self.price_total = 0.0
        self.wish_list = []

