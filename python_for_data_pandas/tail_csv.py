import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
print(df.tail())
#In order to be returned the last 5 rows of dataframe we use the tail( ) function. #
print()
print(df.tail(8))
#we can pass the exact numbers of the rows we want to be returned, i.e. tail(8).#