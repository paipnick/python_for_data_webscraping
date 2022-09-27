import pandas as pd
d1 = {'key': ['a', 'b', 'c', 'd'],
         'Name': ['Mary', 'John', 'Alice', 'Bob']}
d2 = {'key': ['a', 'b', 'c', 'd'],
          'Age': [27, 24, 22, 32]}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
result = pd.merge(df1, df2, on='key')
print(result)
#We define 2 dictionaries which contain employees' names and ages.
# Two dictionaries d1 and d2 are converted in dataframes and we merge into one with the unique key combination.#