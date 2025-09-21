import pandas as pd
data=pd.read_csv("employee.csv")
print(data)

def DF_fun(x):
    if(x%2==0):
        return x**2
    else:
        return x/3
condata=data.age.apply(DF_fun)
print(condata)

