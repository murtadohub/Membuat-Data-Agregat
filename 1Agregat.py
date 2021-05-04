import datetime
import pandas as pd 
dataset = pd.read_csv('data.csv') # untuk membaca file data.csv

#untuk menambah kolom order_month
dataset['order_month'] = dataset['order_date'].apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))

#untuk menambah kolom gmv
dataset['gmv'] = dataset['item_price']*dataset['quantity']

#untuk membuat data Agregat pada data.csv
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()

print('ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)#mencetak kolom order_month
print('Lima data teratas:')
print(dataset.head())#mencetak lima data teratas
print(monthly_amount)#mencetak hasil Agregat order_month dengan gmv
