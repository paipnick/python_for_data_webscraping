import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
cnc = df.groupby(['category_name', 'city'])
print(cnc.agg({'bottles_sold': 'sum', 'sale_dollars': 'mean'}))
#we applied the groupby() function to group the data on category_name value, which contains the name of category of the liquor and on city which are sold.
# We applied different aggregation methods in different columns passing a dictionary.#