import pandas as pd
data=pd.DataFrame({
    "name":["nani","nina","soni"],
    "age":[24,23,22],
    "job":["full_stack Ai devloper","data anylist","front end developer"]
})
data.to_csv("employee.csv",index=False) # you can convert json dic records anyhting as you wish 
