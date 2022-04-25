# -*- coding: utf-8 -*-
"""
Created on Sun 10 April, 2022
@author: 
"""

#import relevant libraries (visualization, dashboard, data manipulation)
import pandas as pd 
import numpy as np 
import streamlit as st

#load data
df_agg = pd.read_csv('EPL_20_21.csv')

#engineering data

#dashboard components
add_sidebar = st.sidebar.selectbox('Games played Stats or Contribution Stats', ('Games Played', 'Goal Contributions'))

#total picture
if add_sidebar == 'Games Played':
    df_agg_metrics = df_agg[['Games played', 'Games started', 'Minutes played', 'Yellow cards', 'Red cards']]
    st.write('Games played')

if add_sidebar == 'Goal Contributions':
    st.write('Goals')