import streamlit as st
import pandas as pd

st.title("Sales Data Analyzer")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])
    st.subheader("Raw Data")
    st.write(df.head())

    df['Revenue'] = df['Quantity'] * df['Price']

    revenue_per_product = df.groupby('Product')['Revenue'].sum()
    st.subheader("Total Revenue per Product")
    st.bar_chart(revenue_per_product)

    sales_trend = df.groupby('Date')['Revenue'].sum()
    st.subheader("Sales Trend Over Time")
    st.line_chart(sales_trend)

    top_products = df.groupby('Product')['Quantity'].sum().nlargest(5)
    st.subheader("Top 5 Best-Selling Products")
    st.bar_chart(top_products)
else:
    st.info("Please upload a CSV file to proceed.")
