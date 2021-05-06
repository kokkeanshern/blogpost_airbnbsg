import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------------------

# Set global printing options to display all columns.
pd.set_option('display.max_columns', None)

listings = pd.read_csv('C:\\Users\\Shern\\Downloads\\airbnb_listings_sg.csv')

# --------------------------------------------------------------------------------------

# Drop id and name columns
listings = listings.drop(columns = ['id','name','host_id','host_name',
                                    'last_review','reviews_per_month'])

# --------------------------------------------------------------------------------------

# Print column names and their data types.
# print(listings.dtypes)

# --------------------------------------------------------------------------------------

# Print number of categories in a column
# print("Number of categories in neighbourhood: ",len(listings['neighbourhood'].unique()))
# print("Examples for neighbourhood:")
# print (listings['neighbourhood'].unique()[:5])
# print()
# print("Number of categories in neighbourhood_group: ",len(listings['neighbourhood_group'].unique()))
# print("Examples for neighbourhood_group:")
# print (listings['neighbourhood_group'].unique()[:5])

# --------------------------------------------------------------------------------------

# Bar chart for neighbourhood_group
# listings['neighbourhood_group'].value_counts().plot.bar(rot=0,fontsize=9)
# plt.show()

# --------------------------------------------------------------------------------------

# Get number of missing values for each column
# print("Count of missing values in each column:","\n")
# print(listings.isna().sum())

# --------------------------------------------------------------------------------------

# Plot histogram for target variable "price"
# print("Summary Statistics for column price:","\n")
# print(listings['price'].describe())
# listings['price'].hist()
# plt.show()

# --------------------------------------------------------------------------------------

# Count number of rows in price where price=0
# listings_price0 = listings[listings['price'] == 0]
# print(listings_price0.shape)

# --------------------------------------------------------------------------------------

# Truncates/pads a float f to n decimal places without rounding
# def truncate(f, n):
#     s = '%.12f' % f
#     i, p, d = s.partition('.')
#     return '.'.join([i, (d+'0'*n)[:n]])

# Examine quantiles in "price"
# quantile_range = [0.8,0.85,0.9,0.91,0.92,0.93,0.94, 0.95, 0.96,0.97,0.98,0.99]

# print("Price (SGD) and skewness from 80th percentile onwards:")
# for q in quantile_range:
#     listings_q = listings.loc[(listings['price'] < listings['price'].quantile(q)) & (listings['price'] != 0)]
#     percentile = str(q)
#     skewness = str(listings_q['price'].skew())
#     price_quantile = str(truncate(listings['price'].quantile(q),1))
#     print("\t".join([percentile,price_quantile,skewness]))

