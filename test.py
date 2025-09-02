import pandas as pd
import matplotlib.pyplot as plt
# creating a new pandas set
my_data = {
    'Model':[2345,9807,5675],
    'price':[7000000,6500000,4500000],
    'quantity':[45,60,80]
}
my_datas = pd.DataFrame(my_data)
# my_datas = pd.Series(my_data,index=['x','y','z'])
print(my_datas)
print('\n')
df = pd.read_csv('data.csv')
# x = df.head()
# y = df.tail()
# print(df.to_string())
# print(x)
# print(y)
# df.dropna(inplace=True)
# df.fillna({'Calories':400},inplace=True)
# x = df['Calories'].median()
# df.fillna({'calories': x},inplace=True)
# df.dropna(subset=['Duration'],inplace=True)
# df.drop_duplicates(inplace=True)
# df.loc[60,'Duration'] = 500
# df.corr()
# print(df)

df.plot(kind = 'density',x='Duration',y='Pulse')
plt.show()