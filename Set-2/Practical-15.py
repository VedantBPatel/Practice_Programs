import pandas as pd
data=pd.read_csv("Practice_Programs/Set-2/student_marksheet.csv")
print(data)#with indexing
print()
print(data.to_string(index=False))#Without indexting