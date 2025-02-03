import streamlit as st
import pandas as pd
import plotly.express as px

# ✅ Move set_page_config to the first Streamlit command
st.set_page_config(page_title="Supermarket Sales Dashboard", layout="wide")

# Load Data Function
@st.cache_data
def load_data():
    df = pd.read_csv("supermarket_sales.csv")  # Ensure correct filename
    df["Date"] = pd.to_datetime(df["Date"])  # Convert date column
    return df

# Load dataset
df = load_data()

# Title
st.title("📊 Supermarket Sales Dashboard")

# Example Visualization
fig = px.histogram(df, x="Branch", title="Sales per Branch")
st.plotly_chart(fig)
