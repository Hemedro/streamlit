import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data with caching for performance
@st.cache_data
def load_data():
    df = pd.read_csv("supermarket_sales.csv")  # Ensure correct filename
    df["Date"] = pd.to_datetime(df["Date"])  # Convert date column
    return df

# Load dataset
df = load_data()

# Streamlit Page Config
st.set_page_config(page_title="Supermarket Sales Dashboard", layout="wide")
st.title("🛒 Supermarket Sales Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Options")
min_date = df["Date"].min()
max_date = df["Date"].max()
start_date = st.sidebar.date_input("Start Date", min_date)
end_date = st.sidebar.date_input("End Date", max_date)

# Filter data based on selected dates
filtered_df = df[(df["Date"] >= pd.Timestamp(start_date)) & (df["Date"] <= pd.Timestamp(end_date))]

# Sales Over Time Plot
st.subheader("📈 Sales Over Time")
sales_over_time = filtered_df.groupby("Date")["Total"].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(data=sales_over_time, x="Date", y="Total", marker="o", ax=ax)
ax.set_title("Daily Sales Trend")
ax.set_xlabel("Date")
ax.set_ylabel("Total Sales")
plt.xticks(rotation=45)
st.pyplot(fig)

# Sales by Product Line
st.subheader("📦 Sales by Product Line")
sales_by_product = filtered_df.groupby("Product line")["Total"].sum().reset_index()

fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.barplot(data=sales_by_product, x="Product line", y="Total", palette="viridis", ax=ax2)
ax2.set_title("Total Sales per Product Line")
ax2.set_xlabel("Product Line")
ax2.set_ylabel("Total Sales")
plt.xticks(rotation=45)
st.pyplot(fig2)

# Payment Method Distribution
st.subheader("💳 Payment Method Distribution")
payment_counts = filtered_df["Payment"].value_counts()

fig3, ax3 = plt.subplots(figsize=(6, 4))
payment_counts.plot(kind="pie", autopct="%1.1f%%", colors=["#ff9999", "#66b3ff", "#99ff99"], ax=ax3)
ax3.set_title("Payment Methods Used")
ax3.set_ylabel("")  # Hide the y-label
st.pyplot(fig3)

# Sales by City
st.subheader("🏙️ Sales by City")
sales_by_city = filtered_df.groupby("City")["Total"].sum().reset_index()

fig4, ax4 = plt.subplots(figsize=(8, 4))
sns.barplot(data=sales_by_city, x="City", y="Total", palette="coolwarm", ax=ax4)
ax4.set_title("Total Sales per City")
ax4.set_xlabel("City")
ax4.set_ylabel("Total Sales")
plt.xticks(rotation=45)
st.pyplot(fig4)

# Show Filtered Data Table
st.subheader("📋 Data Preview")
st.write(filtered_df.head())

st.write("🔎 **Use the sidebar to filter the data by date.** Customize and expand the dashboard as needed!")
