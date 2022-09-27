import pandas as pd
data = {
    "students": ['Emma', 'John'],
     "grades": [12, 19.8]
}
my_first_df = pd.DataFrame(data, index=["a", "b"])
for i, j in my_first_df.iterrows():
      print(i, j)
      print("------")
# we use the function iterrows() function in order to get  each element of rows#