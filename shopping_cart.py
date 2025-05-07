# repo 
#hi

import pandas as pd 

# Read the CSV file into a DataFrame
df = pd.read_csv('Groceries_dataset.csv')

# Remove duplicate rows
groceries = df.drop_duplicates()

# Save the DataFrame back to a CSV file
groceries.to_csv('new_list_dataset.csv', index=False)