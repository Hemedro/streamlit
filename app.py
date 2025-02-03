import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data Function
@st.cache_data
def load_data():
    df = pd.read_csv("supermarket_sales.csv")
    df.columns = df.columns.str.strip()  # Remove extra spaces
    return df

df = load_data()

# Streamlit Page Config
st.set_page_config(page_title="Supermarket Sales Dashboard", layout="wide")

# Title
st.title("📊 Supermarket Sales Dashboard")
st.write("Analyze sales, profit, and product categories.")

# ---- DATA OVERVIEW ----
st.sidebar.header("🔍 Filter Data")
category_filter = st.sidebar.multiselect("Select Categories", df["Category"].unique(), default=df["Category"].unique())

filtered_df = df[df["Category"].isin(category_filter)]

st.write("### Dataset Preview:")
st.write(filtered_df.head())

# ---- SALES SUMMARY ----
st.write("### 💰 Sales Summary")
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = len(filtered_df)

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales ($)", f"{total_sales:,.2f}")
col2.metric("Total Profit ($)", f"{total_profit:,.2f}")
col3.metric("Total Orders", total_orders)

# ---- SALES BY CATEGORY ----
st.write("### 📦 Sales by Category")
sales_by_category = filtered_df.groupby("Category")["Sales"].sum().reset_index()
fig1 = px.bar(sales_by_category, x="Category", y="Sales", text="Sales", title="Total Sales by Category")
st.plotly_chart(fig1, use_container_width=True)

# ---- PROFIT BY REGION ----
st.write("### 🌎 Profit by Region")
profit_by_region = filtered_df.groupby("Region")["Profit"].sum().reset_index()
fig2 = px.bar(profit_by_region, x="Region", y="Profit", text="Profit", title="Total Profit by Region", color="Region")
st.plotly_chart(fig2, use_container_width=True)

# ---- SALES BY CITY ----
st.write("### 🏙️ Sales by City")
top_cities = filtered_df.groupby("City")["Sales"].sum().nlargest(10).reset_index()
fig3 = px.bar(top_cities, x="City", y="Sales", text="Sales", title="Top 10 Cities by Sales")
st.plotly_chart(fig3, use_container_width=True)

# ---- CONCLUSION ----
st.write("This dashboard helps visualize key sales and profit metrics for better decision-making.")

