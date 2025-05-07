# repo 
#hi

import pandas as pd 

# Read the CSV file into a DataFrame
df = pd.read_csv('new_Groceries_dataset.csv')

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save the DataFrame back to a CSV file
df.to_csv('cleaned_groceries.csv', index=False)

class ShoppingCart:
    "Class that manages a persons shopping cart based on their budget with additional features"