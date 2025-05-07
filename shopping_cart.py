# repo 
#hi

import pandas as pd 

# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save the DataFrame back to a CSV file
df.to_csv('your_file.csv', index=False)