import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
data1=pd.read_csv('DataCollectionmakar1.csv')#Due to some reason my process was breaken down so i joined it. 
data2=pd.read_csv('DataCollectionuslb1.csv')
df = pd.concat([data2,data1])
df=df[-50:]
buy_data=df[['Buyer','Rate (Rs)', 'Qty.']]
sell_data=df[['Seller','Rate (Rs)','Qty.']]
sell_data['Qty.']=sell_data['Qty.']*-1
df1=buy_data.groupby('Rate (Rs)')['Qty.'].sum().reset_index()
df2=sell_data.groupby('Rate (Rs)')['Qty.'].sum().reset_index()
print(df1)
x_axis1=df1['Rate (Rs)']
y_axis1=df1['Qty.']
plt.plot(x_axis1,y_axis1)
x_axis2=df2['Rate (Rs)']
y_axis2=df2['Qty.']
plt.plot(x_axis2,y_axis2)
plt.show()