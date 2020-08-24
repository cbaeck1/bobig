# GroupBy 집계 메소드와 함수

import numpy as np
import pandas as pd

# df = pd.read_csv("syntax/test01.csv", index_col=0, encoding='UTF-8')
<<<<<<< HEAD
df = pd.read_csv("syntax/test01.csv",
                dtype = {"ASK_ID": str, 
                        "RSHP_ID": str, 
                        "PRVDR_CD": str, 
                        "HASH_DID": str, 
                        "DATASET": str, 
                        "STD_YYYY": str, 
                        "SEX_TYPE": str, 
                        "AGE": int, 
                        "GAIBJA_TYPE": str, 
                        "RVSN_ADDR_CD": str, 
                        "CALC_CTRB_VTILE_FD": str, 
                        "CNT_ID_HHHI_FD": str, 
                        "CMPR_DSB_GRADE": str} )
=======
df = pd.read_csv("syntax/test01.csv")
>>>>>>> 8d8ae2dc232432c2d2529ff127bcb25c66508c45

print(df.shape)
print(df.columns)
print(df.info())
print(df)

# (1) GroupBy 메소드를 이용한 집계 (GroupBy aggregation using methods)\
# NA 값은 모두 무시되고 non-NA 값들에 대해서만 GroupBy method가 적용됩니다

# Making GroupBy object
# kvalues = df.groupby('SEX_TYPE') 
kvalues = df.groupby(['SEX_TYPE','AGE'])
<<<<<<< HEAD
print("kvalues", kvalues)
=======
print(kvalues)
>>>>>>> 8d8ae2dc232432c2d2529ff127bcb25c66508c45

print(kvalues.count())
print(kvalues.count()['ASK_ID'].describe())
print(kvalues.count()['ASK_ID'].max())
# SEX_TYPE, AGE 에 대한 K-익명성 값
<<<<<<< HEAD
print("SEX_TYPE, AGE 에 대한 K-익명성 값:", kvalues.count()['ASK_ID'].min())

# STD_YYYY, SEX_TYPE, GAIBJA_TYPE 에 대한 K-익명성 값
kvalue2 = df.groupby(['STD_YYYY','SEX_TYPE','GAIBJA_TYPE'])
print("kvalue2", kvalue2)
print("STD_YYYY, SEX_TYPE, GAIBJA_TYPE 에 대한 K-익명성 값:", kvalue2.count()['ASK_ID'].min())

# STD_YYYY, SEX_TYPE, GAIBJA_TYPE,RVSN_ADDR_CD 에 대한 K-익명성 값
kvalue3 = df.groupby(['STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD'])
print("kvalue3", kvalue3)
print("STD_YYYY, SEX_TYPE, GAIBJA_TYPE,RVSN_ADDR_CD 에 대한 K-익명성 값:", kvalue3.count()['ASK_ID'].min())
=======
print(kvalues.count()['ASK_ID'].min())

# STD_YYYY, SEX_TYPE, GAIBJA_TYPE 에 대한 K-익명성 값
kvalue2 = df.groupby(['STD_YYYY','SEX_TYPE','GAIBJA_TYPE'])
print(kvalue2)
print(kvalue2.count()['ASK_ID'].min())

# STD_YYYY, SEX_TYPE, GAIBJA_TYPE,RVSN_ADDR_CD 에 대한 K-익명성 값
kvalue3 = df.groupby(['STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD'])
print(kvalue3)
print(kvalue3.count()['ASK_ID'].min())
>>>>>>> 8d8ae2dc232432c2d2529ff127bcb25c66508c45


# subset
subset = df[['STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD','ASK_ID']]
<<<<<<< HEAD
print("subset", subset)
subset.columns = ['STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD','CNT']

# STD_YYYY, SEX_TYPE, GAIBJA_TYPE,RVSN_ADDR_CD 에 대한 K-익명성 값
kvalue4 = subset.groupby(['STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD'])
print("kvalue4", kvalue4)
print(kvalue4.count()['CNT'])
print("STD_YYYY, SEX_TYPE, GAIBJA_TYPE,RVSN_ADDR_CD 에 대한 K-익명성 값:", kvalue4.count()['CNT'].min())

#  SEX_TYPE, GAIBJA_TYPE,RVSN_ADDR_CD 에 대한 K-익명성 값
kvalue5 = subset.groupby(['SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD'])
kvalue5.count()['CNT'].to_csv("syntax/kvalue5.csv")
print("kvalue5", kvalue5)
print(kvalue5.count()['CNT'])
print("SEX_TYPE, GAIBJA_TYPE,RVSN_ADDR_CD 에 대한 K-익명성 값:", kvalue5.count()['CNT'].min())
=======
print(subset)

# STD_YYYY, SEX_TYPE, GAIBJA_TYPE,RVSN_ADDR_CD 에 대한 K-익명성 값
kvalue4 = subset.groupby(['STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD'])
print(kvalue4)
print(kvalue4.count()['ASK_ID'])
print(kvalue4.count()['ASK_ID'].min())

#  SEX_TYPE, GAIBJA_TYPE,RVSN_ADDR_CD 에 대한 K-익명성 값
kvalue5 = subset.groupby(['SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD'])
kvalue5.count()['ASK_ID'].to_csv("syntax/kvalue5.csv")
print(kvalue5)
print(kvalue5.count()['ASK_ID'])
print(kvalue5.count()['ASK_ID'].min())
>>>>>>> 8d8ae2dc232432c2d2529ff127bcb25c66508c45

