import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
mean = df.mean(numeric_only=True)
print(mean)
#we can calculate the mean of each column using the mean function which is provided by pandas module.#