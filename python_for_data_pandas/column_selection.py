import pandas as pd
data = {
    "students": ['Emma', 'John', 'Bob'],
    "grades": [12, 18, 17]
}
my_first_df=  pd.DataFrame(data)
print(my_first_df)
print("----------------------")
print(my_first_df['students'])
