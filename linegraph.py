import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
data1=pd.read_csv('DataCollectionuslb0.csv')#Due to some reason my process was breaken down so i joined it. 
data2=pd.read_csv('DataCollectionuslb1.csv')
df = pd.concat([data2,data1])
df2 = df['Date']

print('Specify the Buyer you want to view')
a = input("")

buy_data = df[df["Buyer"] == int(a)]
sell_data = df[df["Seller"] == int(a)]

total_qty_buy = buy_data.groupby('Date')['Qty.'].sum().reset_index()
total_qty_sell = sell_data.groupby('Date')['Qty.'].sum().reset_index()
total_qty_sell['Qty.'] = total_qty_sell['Qty.'] * -1

# Merge with the date information
merged_df1 = pd.merge(total_qty_buy, df2, on='Date', how='inner')
merged_df1.fillna(0, inplace=True)

merged_df2 = pd.merge(total_qty_sell, df2, on='Date', how='inner')
merged_df2.fillna(0, inplace=True)

# Remove duplicates
merged_df1 = merged_df1.drop_duplicates(subset='Date')
merged_df2 = merged_df2.drop_duplicates(subset='Date')

# Convert 'Date' column to datetime type
merged_df1['Date'] = pd.to_datetime(merged_df1['Date'])
merged_df2['Date'] = pd.to_datetime(merged_df2['Date'])

# Sort by 'Date'
merged_df1 = merged_df1.sort_values(by='Date')
merged_df2 = merged_df2.sort_values(by='Date')

plt.figure(figsize=(10, 6))
plt.plot(merged_df1['Date'], merged_df1['Qty.'], color="green", label="Buy")
plt.plot(merged_df2['Date'], merged_df2['Qty.'], color="red", label="Sell")

plt.xlabel('Date')
plt.ylabel('Quantity')
plt.title(f'Buy and Sell Data for Buyer {a}')

# Customize x-axis to show year and month
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))#this solution i found on the internet.

plt.legend()
plt.show()
