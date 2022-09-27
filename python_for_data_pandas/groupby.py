import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
cn = df.groupby('category_name')
print(cn.first())
# we applied the groupby() function to group the data on category_name value, which contains the name of category of the liquor. 38 rows x 23 columns were returned, as it is shown in code snippet.#