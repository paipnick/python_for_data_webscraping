import pandas as pd
import numpy as np
data = {
    "students": ['Emma', 'John', 'Mary', 'Bob'],
    "grades": [12, np.nan,18, np.nan]
}
my_first_df=  pd.DataFrame(data, index=["a", "b", "c", "d"])
print(my_first_df)
print("---------------")
my_first_df.dropna(inplace=True)
print(my_first_df)
#we used the dropna function to remove the rows with missing values. In order to change the original dataframe we use the inplace= True statement.#