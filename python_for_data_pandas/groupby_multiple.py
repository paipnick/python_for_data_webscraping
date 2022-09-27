import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
cn2 = df.groupby(['category_name', 'city'])
print(cn2.first())
 # group the data on category_name value, which contains the name of category of the liquor and on city which are sold. 172 rows x 22 columns were returned as it is shown in code snippet.#