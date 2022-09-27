import pandas as pd
import numpy as np

data = pd.read_csv("1.supermarket.csv")
print(data.head(10))
print("\nShape of Dataset :",data.shape)
print()
print(data.info())
x = data.groupby("item_name")
x = x.sum()
print(x.head(1))