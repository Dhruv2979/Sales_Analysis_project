import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Data preparation 
df = pd.read_csv(r"C:\Users\DHRUV SHAH\SalesAnalysis\Salesdata.csv")
print(df)
print("\n")

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
print(df['OrderDate'])
print(type(df['OrderDate']))

df['Revenue'] = df['Price'] * df['Quantity']
print(df)
print("\n")

# Data analysis 

Total_Revenue = df['Revenue'].sum()
print(Total_Revenue)
print("\n")

Revenue_by_PC = df.groupby('ProductCategory')['Revenue'].sum()
print(Revenue_by_PC)
print("\n")

Top5_products = df.nlargest(5,'Revenue')[['ProductCategory','ProductName']]
print(Top5_products)
print("\n")

Revenue_by_City = df.groupby('City')['Revenue'].sum()
print(Revenue_by_City)
print("\n")

mostUsed_Paymentmethod = df['PaymentMethod'].max()
print(mostUsed_Paymentmethod)

# Visualization 

sns.barplot(x="ProductCategory", y="Revenue", data=df, color="y")
plt.show()

sns.barplot(x="City", y="Revenue", data=df, color="g")
plt.show()

sns.countplot(x="PaymentMethod", data=df, color="r")
plt.show()

""" INSIGHTS

1 Which category is most profitable? Clothing
2 Which city performs best? Mumbai
3 Which products generate highest revenue? Jackets
"""