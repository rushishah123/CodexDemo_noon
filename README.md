# CodexDemo_noon

This repository contains a simple Streamlit application for analyzing sales data from a CSV file. A sample dataset (`sample_sales_data.csv`) with 50 entries is included for demonstration.

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Running the App

Start the Streamlit app with:

```bash
streamlit run app.py
```

Upload a CSV file with columns `Date`, `Product`, `Quantity`, and `Price` to see the analysis:

- **Total revenue per product** (bar chart)
- **Sales trend over time** (line chart)
- **Top 5 best-selling products** (bar chart)
