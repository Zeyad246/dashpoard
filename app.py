import streamlit as st

import plotly.express as px
import pandas as pd
df=pd.read_csv('car_1.csv')
st.set_page_config(layout='wide')
tab1 , tab2 , tab3, tab4 =st.tabs(['MSRP' ,'Origin' , 'Type', 'Comparison between city cars and off-road cars'])
with tab1:
    col1 , col2=st.columns(2)
    st.title('We conclude that the highest car is Acura and the lowest car is Chevrolet and the highest car in terms of horsepower and MSRP is dodge' )
    with col1:
        grp = df.groupby('Make')['MSRP'].max().head(10).sort_values(ascending=False).reset_index()
        st.plotly_chart(px.histogram(data_frame=grp , x='Make' , y='MSRP' , text_auto=True , color='Make' , title='Highest MSRP'))
    with col2:
        min=df.groupby('Make')['MSRP'].min().head(10).sort_values().reset_index()
        st.plotly_chart(px.histogram(data_frame=min , x='Make' , y='MSRP', text_auto=True ,color='Make' , title='Lowest MSRP' ))
        horse=df.groupby('Make')[['Horsepower' , 'MSRP']].max().head(10).sort_values( by= 'Horsepower' ,ascending=False).reset_index()
        st.plotly_chart(px.scatter(data_frame=horse , x='Make' , y=['Horsepower' , 'MSRP'] , title='powerhorse'))
with tab2:
    col1 ,col2 ,col3=st.columns(3)
    st.title('The largest continent in the cars industry is Asia and Rear drivetrain cars are the most common in Europe, while the most common cars in America and Asia is front drivetrain The most common type of car in three countries is the sedan')
    with col1:
        st.plotly_chart(px.pie(data_frame=df , names='Origin' ,title='The country that manufactures the most cars'))
    with col2:
        st.plotly_chart(px.histogram(data_frame=df , x=['Origin'] , color='DriveTrain' , text_auto=True , title='Quantity of front and rear and all wheel drive cars in each country'))
    with col3:
        st.plotly_chart(px.histogram(data_frame=df , x='Origin' ,color='Type' ,text_auto=True,title='The most common type of car in each country'))
with tab3:
    col1 , col2=st.columns(2)
    st.title('The most common car is the sedan in all types of cars, while the Hummer, Jeep and Isuzu cars do not include sedan')
    with col1:
        st.plotly_chart(px.pie(data_frame=df,names='Type' , title='The most common types'))
    with col2:
        st.plotly_chart(px.histogram(data_frame=df , x='Make' , color = 'Type' , text_auto=True,title='Car companies and most types of manufacturing'))
with tab4:
    col1 , col2=st.columns(2)
    st.title('The best car in town is a Dodge, and the best car for off-road driving is a Chevrolet')
    with col1:
        MPG=df.groupby('Make')['MPG_City'].max().head(10).sort_values(ascending=False).reset_index()
        st.plotly_chart(px.histogram(data_frame=MPG , x='Make' , y='MPG_City' , text_auto=True , color='Make' , title='The best car in the city'))
    with col2:
        MG=df.groupby('Make')['MPG_Highway'].max().head(10).sort_values(ascending=False).reset_index()
        fig2=(px.histogram(data_frame=MG , x='Make' , y='MPG_Highway' , text_auto=True , color='Make' ,title='The best off road car'))
        st.plotly_chart(fig2 , key=2)
    
