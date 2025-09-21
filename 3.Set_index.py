import pandas as pd
data=pd.DataFrame({
    "name":["nani","nina","soni"],
    "age":[24,23,22],
    "job":["full_stack Ai devloper","data anylist","front end developer"]
})
dataReIndex=data.set_index("name")
print(dataReIndex)
