import pandas as pd
dataframe=pd.DataFrame({
    "name":["andrew","brain","carolin"],
    "age":[30,32,29],
    "location":["chittoor","greamspets","santhapet"]
})
#print(dataframe)
dataSetIndex=dataframe.set_index(["name"])

#accessing throught the index
print(dataSetIndex.loc["andrew"])
