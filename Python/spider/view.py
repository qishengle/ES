#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import pymysql
import pandas as pd
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
#py.sign_in("XXXX", "XXXX")

conn = pymysql.connect(host="localhost", user="root", passwd="", db="bilitest",charset="utf8")
cursor = conn.cursor()
cursor.execute('select mid,name,place,regtime,sex,fans,level from user_info group by place;')
rows=cursor.fetchall();
#str(rows[0,300])
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'mid', 1: 'name', 2: 'place', 3: 'fans', 4:'level',5:'regtime'}, inplace=True)
#df = df.sort_values(['place'], ascending=[4])
df.head()

trace1 = Scatter(
    x=df['place'],
    y=df['level'],
    text=df['name'],
    mode='markers'
)
layout = Layout(
    xaxis=XAxis( type='log', title='place'),
    yaxis=YAxis( title='level' ),
)
data = Data([trace1])
fig = Figure(data=data, layout=layout)
plotly.offline.plot(data, filename='user_ratio.html')  #本地  
#py.iplot(fig, filename='bilitest fans vs regtime')
