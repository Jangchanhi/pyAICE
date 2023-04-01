import pandas as pd
# from aicentro.session import Session
# from aicentro.framework.keras import Keras as AiduFrm

aidu_s = Session(verify=False)
aidu_f = AiduFrm(session = aidu_s)


df = pd.read_csv(aidu_f.config.data_dir + '/sc_cust_info_txn_v1.5.csv')
print(df)


df.info()


