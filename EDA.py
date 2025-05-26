import pandas as pd
df=pd.read_csv("Product (1).csv",delimiter='\t')
df["Standard Cost"]=df["Standard Cost"].replace('[\$,]','',regex=True).astype(float)

#descriptive statistics
print(df["Standard Cost"].describe())
#product count by category
print(df["Category"].value_counts())
#average cost by category
avg_cost=df.groupby("Category")["Standard Cost"].mean().reset_index()
print(avg_cost)