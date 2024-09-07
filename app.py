import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set up the page configuration
st.set_page_config(layout='wide', page_title='Startup Dashboard', page_icon=':moneybag:')

# Load and preprocess the dataset
df = pd.read_csv('startup_clean.csv')
df['investors'] = df['investors'].fillna('Undisclosed')
df['month'] = pd.to_datetime(df['date']).dt.month
df['year'] = pd.to_datetime(df['date']).dt.year

# Sidebar title
st.sidebar.title('Startup Dashboard')

# Function for overall analysis
def overall_analysis():
    st.title('Overall Analysis')

    # Metrics
    total_funding = round(df['amount'].sum(), 2)
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    avg_funding = df.groupby('startup')['amount'].mean().mean()
    num_startups = df['startup'].nunique()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label='Total Funding', value=f'{total_funding} Cr')
    with col2:
        st.metric(label='Max Funding', value=f'{max_funding} Cr')
    with col3:
        st.metric(label='Average Funding', value=f'{round(avg_funding, 2)} Cr')
    with col4:
        st.metric(label='Funded Startups', value=num_startups)

    # Month-on-Month Graph
    st.header('Month-on-Month Funding Analysis')
    selected_option = st.selectbox('Select Metric', ['Total', 'Count'])

    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)
    fig = px.line(temp_df, x='x_axis', y='amount', title='Month-on-Month Funding Analysis',
                  labels={'x_axis': 'Month-Year', 'amount': 'Total Amount' if selected_option == 'Total' else 'Transaction Count'})
    st.plotly_chart(fig)

    # Top sectors pie chart
    st.header('Top Sectors')
    sector_option = st.selectbox('Select Type', ['Total', 'Count'])

    if sector_option == 'Total':
        tmp_df = df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head(5)
    else:
        tmp_df = df.groupby('vertical')['amount'].count().sort_values(ascending=False).head(5)

    fig = px.pie(tmp_df, values=tmp_df.values, names=tmp_df.index, title='Top Sectors')
    st.plotly_chart(fig)

    # Funding Type Analysis
    st.header('Type of Funding')
    funding_series = df.groupby('round')['amount'].sum().sort_values(ascending=False).head(5)
    fig = px.bar(funding_series, x=funding_series.index, y=funding_series.values, title='Funding Type Distribution')
    st.plotly_chart(fig)

    # City-wise funding analysis
    st.header('City-wise Funding')
    cityfun_series = df.groupby('city')['amount'].sum().sort_values(ascending=False).head(5)
    fig = px.bar(cityfun_series, x=cityfun_series.index, y=cityfun_series.values, title='City-wise Funding')
    st.plotly_chart(fig)

    # Top startups
    st.header('Top Startups')
    top_startups = df.groupby('startup')['amount'].sum().sort_values(ascending=False).head(10)
    fig = px.pie(top_startups, values=top_startups.values, names=top_startups.index, title='Top Startups')
    st.plotly_chart(fig)

    # Top startups overall
    st.header('Top Startups Overall')
    overall_series = df.groupby('startup')['amount'].sum().sort_values(ascending=False).head(8)
    fig = px.bar(overall_series, x=overall_series.index, y=overall_series.values, title='Top Startups Overall')
    st.plotly_chart(fig)

    # Funding Heatmap
    st.header('Funding Heatmap')
    table = pd.crosstab(df['year'], df['round'], values=df['amount'], aggfunc='sum')
    fig = plt.figure(figsize=(12, 6))
    sns.heatmap(table, cmap='coolwarm', annot=True, fmt=".0f", linewidths=.5)
    plt.title('Funding Heatmap')
    st.pyplot(fig)

# Function to load startup details
def load_analysis(item):
    st.title('Startup Analysis')
    st.write(df.groupby('investors')['amount'].sum().sort_values(ascending=False).head())
    
    st.subheader('Name of the Startup')
    st.write(item)
   
    vertical = df[df['startup'].str.contains(item)]['vertical'].values[0]
    st.subheader('Industry')
    st.write(vertical)

    subvertical = df[df['startup'].str.contains(item)]['subvertical'].values[0]
    st.subheader('Sub Industry')
    st.write(subvertical)

    city = df[df['startup'].str.contains(item)]['city'].values[0]
    st.subheader('Location')
    st.write(city)

    funding_rounds = df[df['startup'].str.contains(item)][['round', 'amount', 'date']]
    st.subheader('Funding Rounds')
    st.dataframe(funding_rounds)

# Function to load investor details
def load_investor(investor):
    st.title(investor)
    last5_investor = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Last 5 Investments')
    st.dataframe(last5_investor)

    top_investments = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
    st.subheader('Top 5 Investments')
    st.dataframe(top_investments)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader('Investor Details')
        fig = px.bar(top_investments, x=top_investments.index, y=top_investments.values, title='Investor Details')
        st.plotly_chart(fig)

    with col2:
        st.subheader('Investor Verticals')
        verticals = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        fig = px.pie(verticals, values=verticals.values, names=verticals.index, title='Investor Verticals')
        st.plotly_chart(fig)

    with col3:
        st.subheader('Round Details')
        rounds = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        fig = px.pie(rounds, values=rounds.values, names=rounds.index, title='Round Details')
        st.plotly_chart(fig)

    # Year-on-Year Investment
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader('Year-on-Year Investment')
    fig = px.line(year_series, x=year_series.index, y=year_series.values, title='Year-on-Year Investment')
    st.plotly_chart(fig)

# Sidebar selection
option = st.sidebar.selectbox('Select Analysis', ['Overall Analysis', 'Startup', 'Investors'])

# Conditional rendering based on sidebar selection
if option == 'Startup':
    selected_startup = st.sidebar.selectbox('Select Startup', df['startup'].unique())
    btn = st.sidebar.button('Show Startup Analysis')
    if btn:
        load_analysis(selected_startup)

elif option == 'Overall Analysis':
    btn = st.sidebar.button('Show Overall Analysis')
    if btn:
        overall_analysis()

elif option == 'Investors':
    selected_investor = st.sidebar.selectbox('Select Investor', df['investors'].unique())
    btn = st.sidebar.button('Find Investor Details')
    if btn:
        load_investor(selected_investor)
