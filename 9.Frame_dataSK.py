from sklearn.datasets import load_diabetes
data=load_diabetes(as_frame=True).frame # this how we see the data of it frameing
#print(data)

print(data.info()) # it gives whole datatype and the column names