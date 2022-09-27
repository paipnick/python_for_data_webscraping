import pandas as pd
import numpy as np
data = {
    "students": ['Emma', 'John', np.nan, 'Bob'],
    "grades": [12, np.nan, 18, 17]
}
my_first_df=  pd.DataFrame(data, index=["a", "b", "c", "d"])
print(my_first_df.isnull())
print("-------------")
print(my_first_df.notnull())

#call the function isnull() to find out the missing values in DataFrame format.#
#the notnull( ) returns the opposite values #