import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
ng = df.groupby('vendor_name')
print(ng.filter(lambda x : len(x) >= 20))
#we applied the groupby() function to group the data on vendor_name value, which contains the name of vendor who sold the liquor.
# Then, we filter data that to return vendor_name which have lived twenty or more times.#