import numpy as np
import pandas as pd

data = pd.DataFrame ({ 'cust_ID': [ 'C_001', 'C_001', 'C_002', 'C_002'],
    'prd_CD': [ 'P_001', 'P_002', 'P_001', 'P_002'],
    'pch_cnt': [1, 2, 3, 4],
    'pch_amt': [100, 200, 300, 400]})

print(data.index, data.columns)
print(data)
dataMelt = pd.melt(data, id_vars=['cust_ID', 'prd_CD'])
print(dataMelt.columns)
print(dataMelt)

# variable 이름, value 이름 부여하기 : var_name, value_name
dataMelt2 = pd.melt(data, id_vars=['cust_ID', 'prd_CD'], var_name='pch_type', value_name='pch_value')
print(dataMelt2.index, dataMelt2.columns)
print(dataMelt2)

data2 = pd.pivot_table(dataMelt2, index=['cust_ID', 'prd_CD'], columns='pch_type', values='pch_value', aggfunc=np.mean)
print(data2.index, data2.columns)
print(data2)
