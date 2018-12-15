#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:59:07 2018

@author: Tianjing Cai
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='gtxskyline', api_key='xnOjRbHfdZKPjqGRcgam')

alcohol_expend = pd.read_csv('../dataset/alcohol-expenditure.csv', sep=',', encoding='latin1')
# Stacked Area Chart
col_list = list(alcohol_expend)
# remove some columns from all columns
col_set = set(col_list)-set(['Entity', 'Code', 'Year'])
col_list = list(col_set)
alcohol_expend['total_expend'] = alcohol_expend[col_list].sum(axis = 1)

for i in range(0, len(col_list)):
    alcohol_expend[col_list[i]]= alcohol_expend[col_list[i]] / alcohol_expend['total_expend'] * 100

alcohol_expend = alcohol_expend.round(2)

x = alcohol_expend['Year']

trace0 = go.Scatter(
        x = x,
        y = alcohol_expend[col_list[0]],
        hoverinfo = 'x+y',
        mode = 'lines', 
        line=dict(width=0.5,
              color='rgb(131, 90, 241)'),
        stackgroup='one',
        name = 'All other (away from home)'
        )

trace1 = go.Scatter(
    x=x,
    y=alcohol_expend[col_list[1]],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(111, 231, 219)'),
    stackgroup='one',
    name = 'Restaurants $ bars (away from home)'
)
    
trace2 = go.Scatter(
    x=x,
    y=alcohol_expend[col_list[2]],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(184, 247, 212)'),
    stackgroup='one',
    name = 'Hotels & motels (away from home)'
)

trace3 = go.Scatter(
    x=x,
    y=alcohol_expend[col_list[3]],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(135, 17, 22)'),
    stackgroup='one',
    name = 'Liquor stores (at home)'
)

trace4 = go.Scatter(
    x=x,
    y=alcohol_expend[col_list[4]],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(166, 130, 200)'),
    stackgroup='one',
    name = 'Food stores (at home)'
)
    
trace5 = go.Scatter(
    x=x,
    y=alcohol_expend[col_list[5]],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(130, 196, 87)'),
    stackgroup='one',
    name = 'Other (at home)'
)

data = [trace0, trace1, trace2, trace3, trace4, trace5]

layout = go.Layout(
        title = 'Percentage of each alcohol sold at each location over years',
        xaxis = dict(
                title = 'Year',
                titlefont = dict(
                        family='Courier New, monospace',
                        size=18,
                        color='#7f7f7f'
                )
            ),
        yaxis = dict(
                title = 'Percentage of alcohol sold',
                titlefont = dict(
                        family='Courier New, monospace',
                        size=18,
                        color='#7f7f7f'
                )
        )
  )
fig = go.Figure(data=data, layout = layout)
py.iplot(fig, filename='stacked-area-plot-hover', validate=False)