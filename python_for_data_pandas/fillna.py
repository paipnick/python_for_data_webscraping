import pandas as pd
import numpy as np
data = {
    "students": ['Emma', 'John', np.nan, 'Bob'],
    "grades": [12, np.nan, 18, 17]
}
my_first_df=  pd.DataFrame(data, index=["a", "b", "c", "d"])
my_first_df["students"].fillna("No Name", inplace=True)
my_first_df["grades"].fillna("No Grade", inplace=True)
print(my_first_df)
#replace theses values from column students with No Name and the column grades with No Grade value.#