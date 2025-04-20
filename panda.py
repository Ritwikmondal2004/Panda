import pandas as pd

#df.sort_values(by=["Age","salary"], ascending=True,inplace=True)
data={
    "Name":['Ram','sam','jadu'],
    "Age":[28,55,22],
    "salary":[1000,2000,3000],
}
print("before--------")
df=pd.DataFrame(data)
print(df)
print("After-------")

df.sort_values(by=["Age"], ascending=[True], inplace=True)
print(df)
