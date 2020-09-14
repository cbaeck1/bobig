import pandas as pd
import glob, os, csv

df = pd.read_csv("syntax/cnt01.csv",
    dtype = {"ASK_ID": str, 
             "RSHP_ID": str, 
             "PRVDR_CD": str, 
             "DATASET": str, 
             "STD_YYYY": str, 
             "SEX_TYPE": str, 
             "GAIBJA_TYPE": str, 
             "RVSN_ADDR_CD": str, 
             "CNT": int, 
             "ROWID": int} )
print(df.shape)
print(df.columns)
print(df.info())
print(df)

dataMelt = pd.melt(df, id_vars=['ASK_ID', 'RSHP_ID', 'PRVDR_CD','DATASET','ROWID'], 
                    var_name='VAR_CD', value_name='DATA_VALUE')
print(dataMelt.columns)
print(dataMelt)
dataMelt2 = dataMelt.set_index('ASK_ID')

#
dataMelt2.to_csv("syntax/melt01.csv")


