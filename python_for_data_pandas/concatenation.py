import pandas as pd
d1 = {'Name': ['Mary', 'John', 'Alice', 'Bob'],
         'Age': [27, 24, 22, 32],
         'Position': ['Data Analyst', 'Trainee', 'QA Tester', 'IT']}
d2 = {'Name': ['Steve', 'Tom', 'Jenny', 'Nick'],
          'Age': [37, 25, 24, 52],
          'Position': ['IT', 'Data Analyst', 'Consultant', 'IT']}
df1 = pd.DataFrame(d1, index=[0, 1, 2, 3])
df2 = pd.DataFrame(d2, index=[4, 5, 6, 7])
result = pd.concat([df1, df2])
print(result)
#We construct two different dictionaries d1 and d2 with employees data.
# Then the two dictonaries are converted in dataframes and using the concat function we created one dataframe.#