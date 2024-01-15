import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
data1=pd.read_csv('DataCollectionmakar1.csv')
data2=pd.read_csv('DataCollectionuslb1.csv')
df = pd.concat([data2,data1])
df=df[-1000:]
print(df)
df2 = df['Date']
print('Specify the Buyer you want to view')
a = input("")
buy_data = df[df["Buyer"] == int(a)]
sell_data = df[df["Seller"] == int(a)]
buy_data=buy_data[-1000:]
sell_data=sell_data[-1000:]
print(buy_data)
total_qty_buy = buy_data.groupby('Rate (Rs)')['Qty.'].sum().reset_index()
print(total_qty_buy)
total_qty_sell = sell_data.groupby('Rate (Rs)')['Qty.'].sum().reset_index()
total_qty_sell['Qty.'] = total_qty_sell['Qty.'] * -1
plt.plot(total_qty_buy["Rate (Rs)"],total_qty_buy["Qty."])
plt.plot(total_qty_sell['Rate (Rs)'], total_qty_sell["Qty."])
plt.xlabel('Rate')
plt.ylabel('Quantity')
plt.title(f'Buy and Sell Data for Buyer {a}')
plt.show()
