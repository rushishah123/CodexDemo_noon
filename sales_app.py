import pandas as pd
import streamlit as st

st.title('Sales Data Analyzer')

uploaded_file = st.file_uploader('Upload a CSV file with sales data', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('Raw Data')
    st.write(df)

    # Ensure numeric types
    df['Revenue'] = df['Units'] * df['Price']

    st.subheader('Total Revenue per Product')
    revenue_per_product = df.groupby('Product')['Revenue'].sum().reset_index()
    st.write(revenue_per_product)

    st.subheader('Sales Trend Over Time')
    trend = df.groupby('Date')['Revenue'].sum().reset_index()
    st.line_chart(trend.set_index('Date'))

    st.subheader('Top 5 Best-Selling Products')
    top_products = (
        df.groupby('Product')['Units']
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )
    st.bar_chart(top_products.set_index('Product'))
else:
    st.info('Please upload a CSV file to begin.')
