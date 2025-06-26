#ques 1
import pandas as pd
date = pd.Series(['2025-03-25 14:30:00', '2025-03-26 15:45:00', '2025-03-27 09:15:00','2025-03-27 09:15:00'])

s = pd.to_datetime(date)
print(s)

#ques2
import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Tanuj','Vaibhav','Naval','saboo'],
    'score': [25 , 12 , 45 , 75]
    })

df2 = pd.DataFrame({
    'id': [3, 4, 5, 6],
    'score': [85 , 90 , 75 , 60]})
print( pd.merge(df1, df2, on='id', how='inner'))

print(pd.merge(df1, df2, on='id', how='left'))

print(pd.merge(df1, df2, on='id', how='right'))
print(pd.merge(df1, df2, on=['id', 'score'], how='inner'))

#ques 3
import pandas as pd

df1=pd.DataFrame({"car":["aa","cc","bb"],"price":[90,88,66],"id":[1,2,3]})
df2=pd.DataFrame({"car":["ss","tt","rr"],"price":[56,88,66],"id":[1,2,3]})
print(df2.merge(df1,how="inner",on='price'))
print(df2.merge(df1,how="inner",on='id'))

res=df2.join(df1,rsuffix="_right",lsuffix="_left")
print(res)

df4=pd.DataFrame({"car":["aa","cc","bb"],"price":[90,88,66],"id":[1,2,3]})
df5=pd.DataFrame({"car1":["ss","tt","rr"],"price":[56,88,66],"id":[1,2,3]})
df7=pd.concat([df4,df5],keys=["a1","a2"],axis=1)
df9=pd.concat([df4,df5])
print(df9)
df8=df4.merge(df5,how="inner",on='id')
