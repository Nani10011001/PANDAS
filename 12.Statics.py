import pandas as pd
dataframe=pd.DataFrame({
    "name":["andrew","brain","carolin"],
    "age":[30,32,29],
    "location":["chittoor","greamspets","santhapet"]
})
meanData=dataframe.groupby("name").agg({ # by using the manual data
    "age":"median"
})
""" print(meanData) """
# by using the sklearn data
from sklearn.datasets import load_breast_cancer
data=load_breast_cancer(as_frame=True).frame
mean=data.agg({
    "mean radius":"mean"
})
print(mean)