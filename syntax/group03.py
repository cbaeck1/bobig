# GroupBy 집계 메소드와 함수

import numpy as np
import pandas as pd

# df = pd.read_csv("syntax/test01.csv", index_col=0, encoding='UTF-8')
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

print(df.shape)
print(df.columns)
print(df.info())
print(df)

# (1) GroupBy 메소드를 이용한 집계 (GroupBy aggregation using methods)\
# NA 값은 모두 무시되고 non-NA 값들에 대해서만 GroupBy method가 적용됩니다

# Making GroupBy object : kvalues = df.groupby('SEX_TYPE') 
# STD_YYYY, SEX_TYPE, GAIBJA_TYPE,RVSN_ADDR_CD 
# kvalue = df.groupby(['ASK_ID','RSHP_ID','PRVDR_CD','DATASET','STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD'])
# kvalue.count().reset_index(['ASK_ID','RSHP_ID','PRVDR_CD','DATASET','STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD'])\
#     .set_index(['ASK_ID','RSHP_ID','PRVDR_CD','DATASET','STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD'])\
#     .to_csv("syntax/sum01.csv")

# subset.columns = ['STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD','CNT']
# kvalue5.count()['CNT'].to_csv("syntax/kvalue5.csv")
# subset
subset = df[['ASK_ID','RSHP_ID','PRVDR_CD','DATASET','STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD']]
# distinct 
kvalue3 = subset.groupby(['ASK_ID','RSHP_ID','PRVDR_CD','DATASET','STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD'])
# sum DataFrame
# sumdf = kvalue3.sum() 으로 하면 시간이 많이 걸림 왜 그럴까요?
sumdf = kvalue3.count() 
print(sumdf.shape)
print(sumdf.columns) # 컬럼정보는 없음
print(sumdf.info())
print(sumdf)
sumdf.to_csv("syntax/sum02.csv")

# cnt 컬럼 추가
subsetCnt = df[['ASK_ID','RSHP_ID','PRVDR_CD','DATASET','STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD','CALC_CTRB_VTILE_FD']]
subsetCnt.columns = ['ASK_ID','RSHP_ID','PRVDR_CD','DATASET','STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD','CNT']

kvalueCnt = subsetCnt.groupby(['ASK_ID','RSHP_ID','PRVDR_CD','DATASET','STD_YYYY','SEX_TYPE','GAIBJA_TYPE','RVSN_ADDR_CD'])
# Series
cntdf = kvalueCnt.count()['CNT']
# Series to dataFrmae
cntdf = cntdf.to_frame()
cntdf['ROWID'] = np.arange(1, len(cntdf)+1)
print(cntdf.shape)
print(cntdf)

# csv 파일 쓰기
cntdf.to_csv("syntax/cnt01.csv")
