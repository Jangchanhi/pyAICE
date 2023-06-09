import numpy as np
import pandas as pd
from IPython.display import Image
# data = pd.DataFrame({'cust_id':['cust1','cust1','cust1','cust2','cust2','cust2','cust3','cust3','cust3'],
#                     'prod_cd' : ['p1','p2','p3','p1','p2','p3','p1','p2','p3'],
#                     'grade' : ['A','A','A','A','A','A','B','B','B'],
#                     'pch_amt' : [30,10,0,40,15,30,0,0,10]})
# print(data)
#
# data.pivot(index= 'cust_id', columns='prod_cd', values='pch_amt')
# print(data.pivot)
# # data.pivot('cust_id', 'prod_cd','pch_amt')
# # columns이 2개 이상인 경우
# data.pivot_table(index = ['cust_id', 'grade'], columns = 'prod_cd', values='pch_amt')
#
# data.pivot_table(index= 'cust_id', columns=['grade', 'prod_cd'], values='pch_amt')
#
#

# df1 = pd.DataFrame({'key1' : [0,1,2,3,4], 'value1' : ['a', 'b', 'c', 'd', 'e']}, index=[0,1,2,3,4])
# df2 = pd.DataFrame({'key1' : [3,4,5,6,7], 'value1' : ['c', 'd', 'e', 'f', 'g']}, index=[3,4,5,6,7])
#
# print("<df1>")
# print(df1)
#
# print("<df2>")
# print(df2)
#
# print("<concat 연습, index=False>")
# print(pd.concat([df1, df2], ignore_index=False))
# print("concat 연습, index=True")
# print(pd.concat([df1, df2], ignore_index=True))
#
# # concat axis = 1
# print(pd.concat([df1,df2],axis=1))
# # concat axis = 0
# print(pd.concat([df1,df2],axis=0))
#
# df3 = pd.DataFrame({'a':['a0','a1','a2','a3'], 'b':['b0','b1','b2','b3'], 'c':['c0','c1','c2','c3']},
#                    index = [0,1,2,3])
# df4 = pd.DataFrame({'a':['a2','a3','a4','a5'], 'b':['b2','b3','b4','b5'], 'c':['c2','c3','c4','c5'], 'd':['d1','d2','d3','d4']},
#                    index = [2,3,4,5])
#
# # df3
# print(df3)
#
# # df4
# print(df4)
#
# # concat, join = outer 사용
# print(pd.concat([df3, df4], join='outer'))
#
# # concat, join = inner 사용
# print(pd.concat([df3, df4], join='inner'))


df5 = pd.DataFrame({'a':['a0','a1','a2'], 'b':['b0','b1','b2'], 'c':['c0','c1','c2'], 'd':['d1','d2','d3']},
                   index = ['i0','i1','i2'])
df6 = pd.DataFrame({'a':['aa2','a3','a4'], 'b':['bb2','b3','b4'], 'c':['cc2','c3','c4'], 'd':['dd2','d3','d4']},
                   index = ['i2','i3','i4'])

print(df5)
print(df6)

# pd.concat([df5,df6], verify_integrity=False)
print(pd.concat([df5,df6], verify_integrity=False))

customer = pd.DataFrame({'cust_id' : np.arange(6),
                         'name' : ['찬희', '정우', '이수', '대광', '민우', '민제'],
                         '나이' : ['30', '29', '20', '40', '55', '45']})
orders = pd.DataFrame({'cust_id' : [1,1,2,2,2,3,3,1,4,9],
                         'item' : ['치약', '칫솔', '이어폰', '헤드셋', '수건','생수','수건','치약','생수','케이스'],
                         'quantity' : [1,2,1,1,3,2,2,3,2,1]})

print(customer)
print(orders)

# merge -> on 'cust_id'
print(pd.merge(customer, orders, on='cust_id')) # 기본적으로 inner 적용됨

# how -> inner
print(pd.merge(customer, orders, on='cust_id', how='inner'))

# how -> left
print(pd.merge(customer, orders, on='cust_id', how='left'))

# how -> right
print(pd.merge(customer, orders, on='cust_id', how='right'))

# how -> outer
print("how=>outer")
print(pd.merge(customer, orders, on='cust_id', how='outer'))

# index 기준으로 join 하기

cust1 = customer.set_index('cust_id')
order1 = orders.set_index('cust_id')

print(cust1)
print(order1)

print(pd.merge(cust1, order1, left_index = True, right_index=True))

#item 위주로
print(pd.merge(customer, orders, on='cust_id', how='right').groupby('item').sum)

# print(pd.merge(customer, orders, on='cust_id', how='right').groupby('item').sum().sort_values(by='quantity',ascending=False))

# print(pd.merge(customer, orders, on='cust_id',how='inner').groupby(['name', 'item']).sum())
#
# a=pd.merge(customer, orders, on='cust_id',how='inner').groupby(['name', 'item']).sum().loc['정우']
# print(a)

print(cust1.join(order1, how='inner'))



