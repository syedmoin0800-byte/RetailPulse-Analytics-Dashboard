import streamlit as st
import pandas as pd

df = pd.read_csv("Data/train.csv")

# Sidebar Filters
st.sidebar.header("🔍 Filter Dashboard")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

# Apply Filters
df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category))
]

st.set_page_config(
    page_title="RetailPulse Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 RetailPulse Analytics Dashboard")

st.markdown("""
Welcome to RetailPulse Dashboard.

This dashboard provides:
- 📈 Sales Analysis
- 👥 Customer Segmentation
- 🛒 Product Performance Analysis
- 🔮 Sales Forecasting (ARIMA & Prophet)
- 📊 Business Insights
""")

st.header("📌 Project Overview")

st.write("""
RetailPulse analyzes retail sales data, identifies customer behavior,
finds top products, and predicts future sales using ARIMA and Prophet models.
""")

st.write(df.head())
st.header("🚀 Project Status")

st.success("✔ Sales Analysis Completed")
st.success("✔ Customer Segmentation Completed")
st.success("✔ Forecasting Completed")
st.success("✔ Churn Customer Analysis Completed")

st.markdown("---")
st.write("Developed by Syed Moin S")
st.header("📊 Dataset Information")

st.write("Shape of Dataset:", df.shape)

st.write("Columns in Dataset:")
st.write(df.columns)

st.write("Missing Values:")
st.write(df.isnull().sum())
st.header("💰 Sales Analysis")

total_sales = df["Sales"].sum()
total_orders = df["Order ID"].nunique()

col1, col2 = st.columns(2)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Orders", total_orders)
st.subheader("Sales by Category")

category_sales = df.groupby("Category")["Sales"].sum()

st.bar_chart(category_sales)
st.subheader("Top 10 Selling Products")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_products)
st.subheader("Region-wise Sales")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(region_sales)
st.subheader("Customer Segmentation")

customer_segment = (
    df.groupby("Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(customer_segment)
st.subheader("Sub-Category Performance")

subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(subcategory_sales)
st.subheader("Monthly Sales Trend")

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

st.line_chart(monthly_sales)
st.subheader("Top 10 Customers by Sales")

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_customers)
st.subheader("Yearly Sales Trend")

df["Year"] = df["Order Date"].dt.year

yearly_sales = (
    df.groupby("Year")["Sales"]
    .sum()
)
st.bar_chart(yearly_sales)
st.sidebar.markdown("---")
st.sidebar.header("📌 Project Info")

st.sidebar.info("""
RetailPulse Analytics Dashboard

Developer: Syed Moin S

Features:
- Sales Analysis
- Customer Segmentation
- Product Performance
- Sales Trends
- Region Analysis

Note:
Profit analysis is not included because the dataset does not contain a Profit column.
""")