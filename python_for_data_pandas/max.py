import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
max_v = df.max(numeric_only=True)
print(max_v)
#we can calculate the max of each column using the max function which is provided by pandas module.#