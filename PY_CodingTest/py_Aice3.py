import numpy as np
import pandas as pd
data = pd.DataFrame({'cust_id':['cust1','cust1','cust1','cust2','cust2','cust2','cust3','cust3','cust3'],
                    'prod_cd' : ['p1','p2','p3','p1','p2','p3','p1','p2','p3'],
                    'grade' : ['A','A','A','A','A','A','B','B','B'],
                    'pch_amt' : [30,10,0,40,15,30,0,0,10]})
print(data)

data.pivot(index= 'cust_id', columns='prod_cd', values='pch_amt')
print(data.pivot)
# data.pivot('cust_id', 'prod_cd','pch_amt')
# columns이 2개 이상인 경우
data.pivot_table(index = ['cust_id', 'grade'], columns = 'prod_cd', values='pch_amt')

data.pivot_table(index= 'cust_id', columns=['grade', 'prod_cd'], values='pch_amt')
