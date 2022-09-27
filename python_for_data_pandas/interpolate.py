import pandas as pd
import numpy as np
data = {
    "students": ['Emma', 'John', 'Mary', 'Bob'],
    "grades": [12, np.nan,18, np.nan]
}
my_first_df=  pd.DataFrame(data, index=["a", "b", "c", "d"])
df = my_first_df.interpolate(method='linear', limit_direction='forward')
print(df)
#Having created the DataFrame my_first_df with missing values in the grade column, we used the interpolate function to fill the missing values using linear method#
#It ignores the index and treat the values as equally spaced, the values get filled in forward direction and there is no previous value which could have been used in interpolation.#