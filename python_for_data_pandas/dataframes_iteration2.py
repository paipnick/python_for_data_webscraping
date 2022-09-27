import pandas as pd
data = {
    "students": ['Emma', 'John'],
     "grades": [12, 19.8]
}
my_first_df = pd.DataFrame(data, index=["a", "b"])
columns = list(my_first_df)
for i in columns:
      print(my_first_df[i][1])
#we create a list of dataframe columns and then we  iterate through that list to pull out the dataframe columns. Finally, we print the 2nd element of the column.#