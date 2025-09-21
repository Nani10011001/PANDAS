import pandas as pd
dataframe=pd.DataFrame({
    "name":["andrew","brain","carolin"],
    "age":[30,32,29],
    "location":["chittoor","greamspets","santhapet"]
})
set_index_data=dataframe.set_index("name")
for i,row in set_index_data.iterrows(): # iteran
    print(i)
for j,col in dataframe.items():# iteration by colums
    print("col=",j)
