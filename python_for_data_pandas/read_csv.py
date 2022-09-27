import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
print(df.head())
#In order to be returned the top 5  rows of dataframe we use the head( ) function.#
print()
print(df.head(8))
#The default number of rows which are returned are 5, but we can pass the exact numbers of the rows we want to be returned, i.e. head(8).#