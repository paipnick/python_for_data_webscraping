import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("1.supermarket.csv")
q = data.groupby("item_name").quantity.sum()

plt.bar(q.index, q, color=["orange", "red", "purple", "yellow", "green", "blue", "cyan" ])
plt.xlabel("Items")
plt.ylabel("Number of items ordered")
plt.xticks(rotation=3)
plt.title("Most ordered Supermarket\'s Items")
plt.show()