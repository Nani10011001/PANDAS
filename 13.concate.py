import pandas as pd
df1=pd.DataFrame({
    "items":["a","b","c"],
    "price":[3,4,5]
})
df2=pd.DataFrame({
    "items":["d","e","f"],
    "price":[5,6,5]
})
concating=pd.concat([df1,df2])
print(concating)