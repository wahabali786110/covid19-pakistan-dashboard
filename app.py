import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='COVID-19 Tracking Dashboard: Pakistan',
                   page_icon='🦠',
                   layout='wide')

st.title('COVID-19 Tracking Dashboard: Pakistan')
st.subheader("Data sourced from: [Our World in Data (OWID)](https://www.kaggle.com/datasets/caesarmario/our-world-in-data-covid19-dataset)")
st.markdown('---')




@st.cache_data
def load_my_data():
    df=pd.read_csv('pakistan_covid_data.csv')
    return df

df= load_my_data()


st.sidebar.header('Filter Options')
year_option=['All']+df['Year'].unique().tolist()
selected_year=st.sidebar.selectbox(label='Select Year',options=year_option)
selected_column=st.sidebar.radio(label='View Trends By:',options=['Cases','Deaths'],horizontal=True)


total_cases=f"{int(df['total_cases'].max()):,}"
total_deaths=f"{int(df['total_deaths'].max()):,}"
people_fully_vaccinated=f"{int(df['people_fully_vaccinated'].max()):,}"
mortality_rate=f"{round(float(df['total_deaths'].max()/df['total_cases'].max()),4)*100}%"

new_cases=f"{int(df['new_cases'].iloc[-1]):,}"
new_deaths=f"{int(df['new_deaths'].iloc[-1]):,}"
new_people_fully_vaccinated=f"{int(df['people_fully_vaccinated'].iloc[-1]):,}"

col1,col2,col3,col4=st.columns(4)

if selected_year=='All':
    with col1:
        st.metric(label='Total Confirmed Cases',
                value=total_cases,
                delta=new_cases
                )

    with col2:
        st.metric(label='Total Confirmed Deaths',
                value=total_deaths,
                delta=new_deaths
                )

    with col3:
        st.metric(label='People Fully Vaccinated',
                value=people_fully_vaccinated,
                delta=new_people_fully_vaccinated
                )
    
    with col4:
        st.metric(label='Mortality Rate',
                  value=mortality_rate
                  
                  )

    st.markdown("---")

    if selected_column=='Cases':
        fig=px.line(df,
                    x='date',
                    y='new_cases',
                    title=f"COVID-19 Daily {selected_column} in Pakistan",
                    labels={'date':'Date','new_cases':'Daily New Cases'},
                    template='plotly_dark'
                    )

        st.plotly_chart(fig,use_container_width=True)
        st.markdown("---")

        months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
            ]   
        
        df2=df.groupby('Month')['new_cases'].sum().loc[months].reset_index()
        

        fig2=px.bar(df2,
                    x='Month',
                    y='new_cases',
                    title=f"Monthly {selected_column} Trends",
                    labels={'Month':'Month','new_cases':'Daily New Cases'},
                    template='plotly_dark'
                    )
        st.plotly_chart(fig2,use_container_width=True)
    else:
        fig=px.line(df,
                    x='date',
                    y='new_deaths',
                    title=f"COVID-19 Daily {selected_column} in Pakistan",
                    labels={'date':'Date','new_deaths':'Daily New Deaths'},
                    template='plotly_dark'
                    )

        st.plotly_chart(fig,use_container_width=True)
        st.markdown("---")

        months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
            ]   
        
        df2=df.groupby('Month')['new_deaths'].sum().loc[months].reset_index()
        

        fig2=px.bar(df2,
                    x='Month',
                    y='new_deaths',
                    title=f"Monthly {selected_column} Trends",
                    labels={'Month':'Month','new_deaths':'Daily New Deaths'},
                    template='plotly_dark'
                    )
        st.plotly_chart(fig2,use_container_width=True)



    with st.expander('📂 View Raw Data'):
        st.dataframe(df,use_container_width=True)
else:
    filtered_df=df[df['Year']==selected_year]

    new_total_cases=f"{int(filtered_df['new_cases'].sum()):,}"
    new_new_cases=f"{int(filtered_df['new_cases'].iloc[-1]):,}"

    new_total_deaths=f"{int(filtered_df['new_deaths'].sum()):,}"
    new_new_deaths=f"{int(filtered_df['new_deaths'].iloc[-1]):,}"

    if selected_year>2020:
        new_total_people_vaccinated=f"{int(filtered_df['people_fully_vaccinated'].max()-df[df['Year']==selected_year-1]['people_fully_vaccinated'].max()):,}"
    else:
        new_total_people_vaccinated=f"{int(filtered_df['people_fully_vaccinated'].max()):,}"

    new_new_people_fully_vaccinated=f"{int(filtered_df['people_fully_vaccinated'].iloc[-1]):,}"

    new_mortality_rate=f"{round(float(filtered_df['new_deaths'].sum()/filtered_df['new_cases'].sum())*100,2)}%"
    with col1:
        st.metric(label='Total Confirmed Cases',
                value=new_total_cases,
                delta=new_new_cases
                )

    with col2:
        st.metric(label='Total Confirmed Deaths',
                value=new_total_deaths,
                delta=new_new_deaths
                )

    with col3:
        st.metric(label='People Fully Vaccinated',
                value=new_total_people_vaccinated,
                delta=new_new_people_fully_vaccinated
                )
    
    with col4:
        st.metric(label='Mortality Rate',
                  value=new_mortality_rate
                  )
        
    st.markdown("---")

    
    if selected_column=='Cases':
        fig=px.line(filtered_df,
                    x='date',
                    y='new_cases',
                    title=f"COVID-19 Daily {selected_column} in Pakistan",
                    labels={'date':'Date','new_cases':'Daily New Cases'},
                    template='plotly_dark'
                    )
        
        st.plotly_chart(fig,use_container_width=True)
    
        st.markdown("---")
        

        if selected_year==2020:
            months = [
                "February", "March", "April",
                "May", "June", "July", "August",
                "September", "October", "November", "December"
            ]   
            filtered_df2=filtered_df.groupby('Month')['new_cases'].sum().loc[months].reset_index()
            fig2=px.bar(filtered_df2,
                        x='Month',
                        y='new_cases',
                        title=f"Monthly {selected_column} Trends",
                        labels={'Month':'Month','new_cases':'Daily New Cases'},
                        template='plotly_dark'
                        )
            
            st.plotly_chart(fig2,use_container_width=True)

        elif selected_year==2023:
                months = [
                            "January","February", "March", "April",
                            "May", "June", "July", "August",
                            "September", "October"
                        ]   
                filtered_df2=filtered_df.groupby('Month')['new_cases'].sum().loc[months].reset_index()
                fig2=px.bar(filtered_df2,
                            x='Month',
                            y='new_cases',
                            title=f"Monthly {selected_column} Trends",
                            labels={'Month':'Month','new_cases':'Daily New Cases'},
                            template='plotly_dark'
                            )
                
                st.plotly_chart(fig2,use_container_width=True)
        else:
            months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
            ]


            filtered_df2=filtered_df.groupby('Month')['new_cases'].sum().loc[months].reset_index()
            fig2=px.bar(filtered_df2,
                        x='Month',
                        y='new_cases',
                        title=f"Monthly {selected_column} Trends",
                        labels={'Month':'Month','new_cases':'Daily New Cases'},
                        template='plotly_dark'
                            )
                
            st.plotly_chart(fig2,use_container_width=True)
    else:
        fig=px.line(filtered_df,
                    x='date',
                    y='new_deaths',
                    title=f"COVID-19 Daily {selected_column} in Pakistan",
                    labels={'date':'Date','new_deaths':'Daily New Deaths'},
                    template='plotly_dark'
                    )
        
        st.plotly_chart(fig,use_container_width=True)
    
        st.markdown("---")
        

        if selected_year==2020:
            months = [
                "February", "March", "April",
                "May", "June", "July", "August",
                "September", "October", "November", "December"
            ]   
            filtered_df2=filtered_df.groupby('Month')['new_deaths'].sum().loc[months].reset_index()
            fig2=px.bar(filtered_df2,
                        x='Month',
                        y='new_deaths',
                        title=f"Monthly {selected_column} Trends",
                        labels={'Month':'Month','new_deaths':'Daily New Deaths'},
                        template='plotly_dark'
                        )
            
            st.plotly_chart(fig2,use_container_width=True)

        elif selected_year==2023:
                months = [
                            "January","February", "March", "April",
                            "May", "June", "July", "August",
                            "September", "October"
                        ]   
                filtered_df2=filtered_df.groupby('Month')['new_deaths'].sum().loc[months].reset_index()
                fig2=px.bar(filtered_df2,
                            x='Month',
                            y='new_deaths',
                            title=f"Monthly {selected_column} Trends",
                            labels={'Month':'Month','new_deaths':'Daily New Deaths'},
                            template='plotly_dark'
                            )
                
                st.plotly_chart(fig2,use_container_width=True)
        else:
            months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
            ]


            filtered_df2=filtered_df.groupby('Month')['new_deaths'].sum().loc[months].reset_index()
            fig2=px.bar(filtered_df2,
                        x='Month',
                        y='new_deaths',
                        title=f"Monthly {selected_column} Trends",
                        labels={'Month':'Month','new_deaths':'Daily New Deaths'},
                        template='plotly_dark'
                            )
                
            st.plotly_chart(fig2,use_container_width=True)
        

    with st.expander('📂 View Raw Data'):
        st.dataframe(filtered_df,use_container_width=True)
