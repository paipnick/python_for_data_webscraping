import pandas as pd
d1 = {'Name': ['Mary', 'John', 'Alice', 'Bob'],
         'Age': [27, 24, 42, 32]}
d2 = {'Position': ['Data Analyst', 'Trainee', 'QA Tester', 'IT'],
          'Years_of_experience':[5, 1, 10, 3] }
df1 = pd.DataFrame(d1, index=[0, 1, 2, 3])
df2 = pd.DataFrame(d2, index=[0, 2, 3, 4])
result = df1.join(df2, how='inner')
print(result)
#we defined two dictionaries with employees data, and then they are converted in two dataframes.
# We used the join() function for combining the columns of these two DataFrames into a single result DataFrame getting the intesection.