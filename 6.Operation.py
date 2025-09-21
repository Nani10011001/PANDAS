import pandas as pd
df1=pd.DataFrame({
    "items":["a","b","c"],
    "price":[3,4,5]
})
df2=pd.DataFrame({
    "items":["d","e","f"],
    "price":[5,6,5]
})
print(df1.price+df2.price*2)# you can perform the operation on the columns if the rows match
#multiplication and division 