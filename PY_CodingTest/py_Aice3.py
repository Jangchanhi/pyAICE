import numpy as np
import pandas as pd
data = pd.DataFrame({'cust_id':['cust1','cust1','cust1','cust2','cust2','cust2','cust3','cust3','cust3',],
                    'PROD_CD ': ['p1','p2','p3','p1','p2','p3','p1','p2','p3',],
                    'grade' : ['A','A','A','A','A','A','B','B','B',],
                    'pch_amt' : [30,10,0,40,15,30,0,0,10]})
print(data)