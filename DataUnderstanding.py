import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set global printing options to display all columns.
pd.set_option('display.max_columns', None)

listings = pd.read_csv('C:\\Users\\Shern\\Downloads\\airbnb_listings_sg.csv')

# Print column names and their data types.
# print(listings.dtypes)

# Drop id and name columns
listings = listings.drop(columns = ['id','name','host_id','host_name'])

# Print number of categories in a column
print("Number of categories in neighbourhood: ",len(listings['neighbourhood'].unique()))
print("Examples for neighbourhood:")
print (listings['neighbourhood'].unique()[:5])
print()
print("Number of categories in neighbourhood_group: ",len(listings['neighbourhood_group'].unique()))
print("Examples for neighbourhood_group:")
print (listings['neighbourhood_group'].unique()[:5])
