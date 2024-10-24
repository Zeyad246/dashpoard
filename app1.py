import streamlit as  st
import pandas as pd 
import plotly.express as px
data=pd.read_csv('bike_1.csv')
st.set_page_config(layout='wide')
tab1 , tab2 , tab3 , tab4 , tab5=st.tabs(['season' , 'profit' , 'registered and casual','rental','work'])
with tab1:
    col1 , col2 ,col3=st.columns(3)
    with col1:
       st.plotly_chart(px.pie(data_frame=data , names='season', values='hour').update_traces(textinfo='label+value+percent'),key=1)
    with col2:
        st.plotly_chart(px.histogram(data_frame=data , x='season' , y='rented_bikes_count' , text_auto=True , title=' count rental bike  for each season' ),key=2)
    with col3:
        st.plotly_chart(px.pie(data_frame=data , names='day_period' , values='rented_bikes_count' , title=' period it has been rented').update_traces(textinfo='label+value+percent'),key=3)
with tab2:
    col1,col2,col3=st.columns(3)
    with col1:
        st.plotly_chart(px.histogram(data_frame=data , x='Profit' , y='season' , text_auto=True , title='The highest profit in the season' ),key=4)
    with col2:
         st.plotly_chart(px.histogram(data_frame=data, x= 'year' ,y='Profit', color='year' , text_auto=True , title='The highest year in the profit'),key=5)
    with col3:
        st.plotly_chart(px.histogram(data_frame=data , x='month_name',y='rented_bikes_count',text_auto='true',title='rental rates each month'),key=6)
with tab3:
    col1,col2,col3=st.columns(3)
    with col1:
        st.plotly_chart(px.pie(data_frame=data , names='season', values='registered',title='Percentage of those registered in each season').update_traces(textinfo='label+value+percent'),key=7)
    with col2:
        st.plotly_chart(px.pie(data_frame=data , names='season', values='casual',title='Percentage of those  not registered in each season').update_traces(textinfo='label+value+percent'),key=8)
    with col3:
        st.plotly_chart(px.histogram(data_frame=data , x=['registered' , 'casual'] , histfunc='sum'),key=9)
with tab4:
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.plotly_chart(px.histogram(data_frame=data , x='season' , y='rented_bikes_count' , text_auto=True , title=' count rental bike  for each season' ),key=10)
    with col2:
        st.plotly_chart(px.histogram(data_frame=data , x='month_name',y='rented_bikes_count',text_auto='true',title='rental rates each month'),key=11)
    with col3:
        st.plotly_chart(px.histogram(data_frame=data , x='day_name' , y='rented_bikes_count' ,text_auto=True , title='Highest renting bikes for any day'),key=12)
    with col4:
        st.plotly_chart(px.pie(data_frame=data , names='day_period' , values='rented_bikes_count' , title=' period it has been rented').update_traces(textinfo='label+value+percent'),key=13)
with tab5:
    st.plotly_chart(px.histogram(data_frame=data , x='workingDay' , title='workingDay'),key=14)
    
