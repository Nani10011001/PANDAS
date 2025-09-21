import pandas as pd
df1=pd.DataFrame({
    "items":["a","b","c"],
    "price":[3,4,5]
})
df2=pd.DataFrame({
    "items":["a","b","c"],
    "discount":[30,20,90]
})
merge=pd.merge(df1,df2,on="items",how="inner")
 # merge used when you have differnt colums data like discounts and same names index of it
print(merge)
#dropna() and drop() their to the pandas to its so many more