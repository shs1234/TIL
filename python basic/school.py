# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 10:10:30 2019

@author: student
"""

import pandas as pd
import folium

file_path='C:/class/data/datas/2016_middle_shcool_graduates_report.xlsx'
df=pd.read_excel(file_path)

school_map=folium.Map(location=[37.55, 126.98], tiles = 'Stamen Terrain', zoom_start=12)


for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.CircleMarker([lat, lng], radius=10, color='black' , fill=True,  fill_color='yellow',
                                          fill_opacity=0.7,  popup=name).add_to(school_map)


school_map.save('C:/class/data/datas/school.html')

from sklearn import preprocessing
#LabelEncoder는 문자를 0부터 시작하는 정수형 숫자로 바꿔주는 기능을 제공 (반대 연산도 가능)
label_encoder=preprocessing.LabelEncoder()
onehot_encoder=preprocessing.OneHotEncoder()

onehot_loc=label_encoder.fit_transform(df['지역'])
onehot_code=label_encoder.fit_transform(df['코드'])
onehot_type=label_encoder.fit_transform(df['유형'])
onehot_day=label_encoder.fit_transform(df['주야'])

df['loc']=onehot_loc
df['code']=onehot_code
df['type']=onehot_type
df['day']=onehot_day

from sklearn import cluster
col_list=[9,10,13]
X=df.iloc[:,col_list]

#정규화
X=preprocessing.StandardScaler().fit(X).transform(X)

dbscan_model=cluster.DBSCAN(eps=0.2,min_samples=5)
dbscan_model.fit(X)

cluster_label=dbscan_model.labels_

df['Cluster']=cluster_label

grouped_cols=[0, 1, 3]+col_list
grouped=df.groupby('Cluster')

#그룹 내부 확인
for key, group in grouped:
    print('* key : ' , key)
    print('* number : ' , len(group))
    print(group.iloc[:, grouped_cols].head())
    print('\n')


colors = {-1:'gray', 0:'coral', 1:'black', 2:'green', 3:'red', 4:'purple', 5:'orange', 6:'brown', 7:'magenta', 8:'yellow', 9:'brick', 10:'cyan', 11:'pink'}

cluster_map = folium.Map(location=[37.55, 126.98],  tiles='Stamen Terrain', zoom_start=12)
for name, lat, lng, clus in zip (df.학교명, df.위도, df. 경도, df.Cluster) :
    folium.CircleMarker([lat, lng],
                              radius=5,
                              color=colors[clus],
                              fill=True,
                              fill_color=colors[clus] ,
                              fill_opacity=0.5,
                              popup=name).add_to(cluster_map)
                        
cluster_map.save('C:/class/data/datas/seoul_mschool_cluster123.html')
