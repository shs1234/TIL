# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:03:42 2019

@author: student
"""

import folium
import pandas as pd

df=pd.read_excel('C:/class/data/datas/서울지역 대학교 위치.xlsx')
df.columns=['이름','위도','경도']

seoul_map=folium.Map(location=[37.55, 126.98],tiles='Stamen Terrain',zoom_start=12)


for name,lat,lng in zip(df.이름,df.위도,df.경도):
    folium.Marker([lat, lng],popup=name).add_to(seoul_map)
    
seoul_map.save('C:/class/data/datas/output/seoul.colleges.html')
