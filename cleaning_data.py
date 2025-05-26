import pandas as pd
df=pd.read_csv("Product (1).csv",delimiter='\t')

#stripping whitespace from columns
df.columns=df.columns.str.strip()
#converting standard cost to numeric
df["Standard Cost"]=df["Standard Cost"].replace('[\$,]','',regex=True).astype(float)
#checking for missing values
print(df.isnull().sum())
# filling missing values
df.fillna(0,inplace=True)