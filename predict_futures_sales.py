import pandas as pd
import numpy as np
from googletrans import Translator
import re


sales_train_df = pd.read_csv('D:\\Mis Documentos\\Data Science Certificate\\Assignments\\Group Assignment\\sales_train_v2.csv', sep=',',header=0)
shops_df = pd.read_csv('D:\\Mis Documentos\\Data Science Certificate\\Assignments\\Group Assignment\\shops.csv', sep=',',header=0)
item_category_df = pd.read_csv('D:\\Mis Documentos\\Data Science Certificate\\Assignments\\Group Assignment\\item_categories.csv', sep=',',header=0)
items_df = pd.read_csv('D:\\Mis Documentos\\Data Science Certificate\\Assignments\\Group Assignment\\items.csv', sep=',',header=0)
test_df = pd.read_csv('D:\\Mis Documentos\\Data Science Certificate\\Assignments\\Group Assignment\\test.csv', sep=',',header=0)

sales_train_df.info()
sales_train_df.shape
sales_train_df.columns
sales_train_df.dropna(inplace=True)

test_df.shape
test_df.head()
len(test_df['item_id'].unique())  #-- 5100
len(test_df['item_id'])  #-- 214200

#----------------------------------------------------
# Train, Test modified
#----------------------------------------------------

#---- Modification of train set until 31-10-2015 (to respect kaggle mentioned)
sales_train_df['date2']=pd.to_datetime(sales_train_df['date'])
sales_train_df2=sales_train_df[sales_train_df['date2']<='2015-10-31']
sales_train_df2['date2'].max()  # Oct 15
sales_train_df2['date2'].min()  # Jan 13
sales_train_df3=sales_train_df2.groupby(['shop_id','date2']).sum()

sales_train_df3['item_cnt_day']
sales_train_df3.info()

# fecha=sales_train_df['date2'][sales_train_df['date2']>='2015-11-01']
# fecha.to_excel('D:\\Mis Documentos\\Data Science Certificate\\Assignments\\Group Assignment\\fecha.xlsx')

#----- Test modified with sum grouped

test_df2=test_df['shop_id'].unique()
len(test_df2)
len(sales_train_df2['shop_id'].unique())


#----- In case of require prices of the items
# item_price_2015=sales_train_df[['item_price','item_id','date2']][(sales_train_df['date2']>='2015-11-01') & (sales_train_df['date2']<='2015-11-12')]
# item_price_2015['date2'].max()
# sales_train_df['date2'].min()
# test_df2=pd.merge(test_df,item_price_2015,on='item_id',how='left')

# len(item_price_2015['item_id'].unique())
# len(item_price_2015['item_id'])


#----------------------------------------------------
# Translation of russian names
#----------------------------------------------------

# gt=Translator()

# list_shop=shop['shop_name'].tolist()
# list_rus_items=[((items['item_name'].get_values()[i])) for i in range(0,len(items['item_name'].get_values()))]

# rus_shop=gt.translate(list_shop)

# rus_items=gt.translate(['Hola'])

# len(items['item_name'])
# rus_items.shape
# rus_items.head()

# trans_items=[]

# rus_items.text

# for trans in rus_items:
#     # trans_items.append(trans.text)
#     print(trans.text)


# re.sub('\W+',' ','Язык запросов 1С:Предприятия  [Цифровая версия]')


# gt.translate('Язык запросов 1С:Предприятия  [Цифровая версия]').text
# print(gt.translate(items['item_name']).text)

#----------------------------------------------------
# Regression tree
#----------------------------------------------------



