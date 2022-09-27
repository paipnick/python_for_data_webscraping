import pandas as pd
data = {
    "students": ['Emma', 'John', 'Bob'],
    "grades": [12, 18, 17]
}
my_first_df=  pd.DataFrame(data, index=["a", "b", "c"])
first_row = my_first_df.loc["a"]
second_row = my_first_df.loc["b"]
print(my_first_df)
print("---------------")
print(first_row)
print("---------------")
print(second_row)
#with index each row with "a", "b" and "c" we access the first row calling the function loc with parameter the index of the row, meaning "a"#