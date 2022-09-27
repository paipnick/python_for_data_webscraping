import pandas as pd
import numpy as np
data = {
    "students": ['Emma', 'John', np.nan, 'Bob'],
    "grades": [12, np.nan,18, 17]
}
my_first_df =  pd.DataFrame(data, index=["a", "b", "c", "d"])
df2 = my_first_df.replace(to_replace="Bob", value="Alice")
print(my_first_df)
print("-----------------------")
print(df2)
#replace the student Bob with the student Alice value.#