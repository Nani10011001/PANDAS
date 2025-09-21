import pandas as pd
dataframe=pd.DataFrame({
    "name":["andrew","brain","carolin"],
    "age":[30,32,29],
    "location":["chittoor","greamspets","santhapet"]
})
#adding of the data
dataframe.loc[3]={"name":"sam","age":26,"location":"santhapet"}
print(dataframe)