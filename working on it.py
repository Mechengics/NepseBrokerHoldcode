import pandas as pd

brokerslist = [1, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 16, 17, 18, 19, 20, 21, 22, 25, 26, 28, 29, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]
df1=pd.read_csv("DataCollectionuslb0.csv")#Due to some reasons the process was prematurely breaken down.
df2=pd.read_csv("DataCollectionuslb1.csv")
df3=pd.concat([df2,df1])
print(df3)
a = 0
my_dict = {}
while a < len(brokerslist):
    filtered_buyer = df3[df3['Buyer'] == brokerslist[a]]
    filtered_seller = df3[df3['Seller'] == brokerslist[a]]
    filtereddataframe_buyer = filtered_buyer[['Buyer', 'Qty.']]
    print(filtereddataframe_buyer)
    sum1 = filtereddataframe_buyer['Qty.'].sum()
    filtereddataframe_seller = filtered_seller[['Seller', 'Qty.']]
    sum2 = filtereddataframe_seller['Qty.'].sum()
    on_hold = abs(sum2 - sum1)
    my_dict[brokerslist[a]] = on_hold
    a += 1
df4 = pd.DataFrame(list(my_dict.items()), columns=['Brokers', 'Kitta'])
df5 = df4.sort_values(by='Kitta', ascending=False)
df5.to_csv('resultuslb.csv')
