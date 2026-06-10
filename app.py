import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='COVID-19 Tracking Dashboard: Pakistan',
                   page_icon='🦠',
                   layout='wide')

st.title('COVID-19 Tracking Dashboard: Pakistan')
st.subheader('Data sourced from: Our World in Data (OWID)')
st.markdown('---')

@st.cache_data
def load_my_data():
    df=pd.read_csv('pakistan_covid_data.csv')
    return df

total_cases=int(load_my_data()['total_cases'].max())
total_deaths=int(load_my_data()['total_deaths'].max())
people_fully_vaccinated=int(load_my_data()['people_fully_vaccinated'].max())

col1,col2,col3=st.columns(3)

with col1:
    st.metric(label='Total Confirmed Cases',value=total_cases)

with col2:
    st.metric(label='Total Confirmed Deaths',value=total_deaths)

with col3:
    st.metric(label='People Fully Vaccinated',value=people_fully_vaccinated)