import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
median = df.median(numeric_only=True)
print(median)
#we can calculate the median of each column using the median function which is provided by pandas module.#