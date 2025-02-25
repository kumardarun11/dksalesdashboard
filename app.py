import streamlit as st
import pandas as pd
import plotly.express as px

# ---- PAGE CONFIGURATION ----
st.set_page_config(page_title="📊 DK Sales Dashboard", layout="wide")

# ---- TITLE ----
st.markdown("<h1 style='text-align: center; color:#4CAF50;'>📊 DK Sales Dashboard</h1>", unsafe_allow_html=True)

# ---- LOAD DATA ----
@st.cache_data
def load_data():
    df = pd.read_csv("sales_data.csv")
    df.columns = df.columns.str.strip()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])  # Drop invalid dates
    df["Month"] = df["Date"].dt.strftime("%Y-%m")  # Extract Month-Year format
    df["Year"] = df["Date"].dt.year.astype(str)  # Extract Year as a string
    df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100
    return df

df = load_data()

# ---- SIDEBAR FILTERS ----
st.sidebar.header("📌 Filter Data:")

# Dynamic Year Selection
selected_year = st.sidebar.selectbox("📅 Select Year:", sorted(df["Year"].unique(), reverse=True))

# Filter data based on the selected year
year_filtered_df = df[df["Year"] == selected_year]

# Dynamic Month Selection based on selected year
selected_month = st.sidebar.selectbox("📅 Select Month:", sorted(year_filtered_df["Month"].unique()))

# Region & Category Filters
selected_region = st.sidebar.multiselect("🌍 Select Region:", df["Region"].unique(), default=df["Region"].unique())
selected_category = st.sidebar.multiselect("📂 Select Category:", df["Category"].unique(), default=df["Category"].unique())

# Apply Filters
filtered_df = df[(df["Month"] == selected_month) & 
                 (df["Region"].isin(selected_region)) & 
                 (df["Category"].isin(selected_category))]

# ---- METRICS ----
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
avg_discount = filtered_df["Discount"].mean()
profit_margin = total_profit / total_sales * 100 if total_sales > 0 else 0
total_orders = filtered_df["Order ID"].nunique()

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("📈 Total Sales", f"${total_sales:,.2f}")
col2.metric("💰 Total Profit", f"${total_profit:,.2f}")
col3.metric("🔖 Avg Discount", f"{avg_discount:.2f}%")
col4.metric("📊 Profit Margin", f"{profit_margin:.2f}%")
col5.metric("📦 Total Orders", total_orders)

# ---- SALES TREND CHART ----
st.subheader("📊 Monthly Sales Trend")
monthly_sales = df.groupby("Month", as_index=False)["Sales"].sum()
fig = px.line(monthly_sales, x="Month", y="Sales", title="Monthly Sales Over Time", markers=True, template="plotly_dark")
fig.update_xaxes(title="Month")
fig.update_yaxes(title="Total Sales")
st.plotly_chart(fig, use_container_width=True)

# ---- SALES BY REGION ----
st.subheader("🌍 Sales by Region")
region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()
fig2 = px.bar(region_sales, x="Region", y="Sales", text_auto=True, title="Sales by Region", template="plotly_dark")
fig2.update_xaxes(title="Region")
fig2.update_yaxes(title="Sales")
st.plotly_chart(fig2, use_container_width=True)

# ---- CATEGORY-WISE SALES ----
st.subheader("📂 Sales by Category")
category_sales = filtered_df.groupby("Category")["Sales"].sum().reset_index()
fig3 = px.pie(category_sales, names="Category", values="Sales", title="Sales Breakdown by Category", template="plotly_dark")
st.plotly_chart(fig3, use_container_width=True)

# ---- TOP 5 PRODUCTS ----
st.subheader("🛒 Top 5 Best-Selling Products")
top_products = filtered_df.groupby("Product")["Sales"].sum().nlargest(5).reset_index()
fig4 = px.bar(top_products, x="Product", y="Sales", text_auto=True, title="Top Products", template="plotly_dark")
fig4.update_xaxes(title="Product")
fig4.update_yaxes(title="Sales")
st.plotly_chart(fig4, use_container_width=True)

# ---- PROFITABILITY TREND ----
st.subheader("💰 Profitability Trend")
profit_trend = df.groupby("Month", as_index=False)["Profit"].sum()
fig5 = px.line(profit_trend, x="Month", y="Profit", title="Monthly Profit Over Time", markers=True, template="plotly_dark")
fig5.update_xaxes(title="Month")
fig5.update_yaxes(title="Total Profit")
st.plotly_chart(fig5, use_container_width=True)

# ---- DISCOUNT IMPACT ----
st.subheader("🔖 Discount Impact on Sales")
discount_impact = df.groupby("Discount")["Sales"].mean().reset_index()
fig6 = px.scatter(discount_impact, x="Discount", y="Sales", size="Sales", title="Discount vs Sales", template="plotly_dark")
fig6.update_xaxes(title="Discount (%)")
fig6.update_yaxes(title="Average Sales")
st.plotly_chart(fig6, use_container_width=True)

# ---- SALES vs PROFIT CORRELATION ----
st.subheader("📈 Sales vs Profit Correlation")
fig7 = px.scatter(
    filtered_df, 
    x="Sales", 
    y="Profit", 
    color="Category", 
    size=filtered_df["Profit"].abs(),  # Convert negative values to positive
    title="Sales vs Profit", 
    template="plotly_dark"
)
fig7.update_xaxes(title="Sales")
fig7.update_yaxes(title="Profit")
st.plotly_chart(fig7, use_container_width=True)

st.write("🔍 **Tip:** Use the sidebar to filter data and explore trends.")

# ℹ Developer Info
st.sidebar.markdown("---")
st.sidebar.subheader("👨‍💻 Developer Info")
st.sidebar.write("**Name:** D ARUN KUMAR")
st.sidebar.write("📧 Email: kumardarun11@gmail.com")
st.sidebar.write("[GitHub](https://github.com/kumardarun11) | [LinkedIn](https://linkedin.com/in/kumardarun11)")
