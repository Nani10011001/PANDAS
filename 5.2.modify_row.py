import pandas as pd
dataframe=pd.DataFrame({
    "name":["andrew","brain","carolin"],
    "age":[30,32,29],
    "location":["chittoor","greamspets","santhapet"]
})
dataframe.loc[1,"age"]=33
print(dataframe)
