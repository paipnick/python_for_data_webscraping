import pandas as pd
s = pd.Series(['workearly', 'e-learning', 'python'])
for index, value in s.items():
     print(f"Index : {index}, Value : {value}")
#we use the method items which returns the index and the value of the series data structure. #