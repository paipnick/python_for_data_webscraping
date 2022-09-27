import pandas as pd
import numpy as np
df = pd.read_csv("finance_liquor_sales.csv")
cn = df.groupby('category_name')
print(cn.aggregate(np.sum))
#we applied the groupby() function to group the data on category_name value, which contains the name of category of the liquor.
# Then we  compute the sum of each group, having imported first the numpy module.#