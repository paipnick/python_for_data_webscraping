import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
summary = df.describe()
print(summary)
# we use the function describe which return the statistics, count, mean, standard deviation, min, max and percentiles.#