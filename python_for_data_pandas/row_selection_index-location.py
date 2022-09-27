import pandas as pd
data = {
    "students": ['Emma', 'John', 'Bob'],
    "grades": [12, 18, 17]
}
my_first_df=  pd.DataFrame(data, index=["a", "b", "c"])
second_row = my_first_df.iloc[1]
print(second_row)
