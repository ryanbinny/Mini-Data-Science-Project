import pandas as pd
df=pd.read_csv("Product (1).csv",delimiter='\t')
df["Standard Cost"]=df["Standard Cost"].replace('[\$,]','',regex=True).astype(float)
avg_cost=df.groupby("Category")["Standard Cost"].mean().reset_index()

#barplot
import seaborn as sns
import matplotlib.pyplot as plt
sns.barplot(data=avg_cost,x="Category",y="Standard Cost")
plt.title("Average cost by category")
plt.show()
#boxplot
sns.boxplot(data=df,x="Standard Cost")
plt.title("Distribution of standard cost")
plt.show()
#heatmap
sns.heatmap(df.select_dtypes(include="number").corr(),annot=True)
plt.title("Distribution of numeric values")
plt.show()

