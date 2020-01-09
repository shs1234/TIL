#datas 압축파일을 받아서  '경기도인구데이터'.csv파일을 이용하여 
#다음 내용을 파이썬  numpy라이브러리를 사용해서 결과를 출력하세요
#1. 파일 내용을 읽은 후 상위 5개 데이터 확인
#2. 배열 객체의 크기 확인 
#3. 중복 지역 존재 여부 확인  
#4. 2017년 수원시 인구의 합
#5. 2017년 인구가 50만이상이 지역 출력
#6. 2017년 경기도 전체 인구의 시별 인구 평균  


import pandas as pd
file_path='./경기도인구데이터.xlsx'
df=pd.read_excel(file_path)
df.set_index('구분',inplace=True)
#1
print(df.head())
#2
print(df.shape)
#3
if len(df.index)==len(df.index.unique()):
    print('중복 지역 없음')
else:
    print('중복 지역 있음')
#4
suwon=df.index.str.contains('수원시')
df[suwon][2017].sum()
#5
df[df[2017]>500000].index
#6
df.loc[:][2017].sum()/len(df.index)