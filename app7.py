import streamlit as  st
import pandas as pd 
import plotly.express as px
st.set_page_config(layout='wide')
df=px.data.tips()
col1 , col2 = st.columns(2)
with col1 :
    st.plotly_chart(px.histogram(data_frame=df  , x='total_bill' , y='sex'))
    st.plotly_chart(px.histogram(data_frame=df  , x='day' , y='total_bill'))
with col2 :
    st.plotly_chart(px.histogram(data_frame=df , x='total_bill' , y='tip'))
    st.plotly_chart(px.histogram(data_frame=df  , x='time' , y='total_bill'))
    
