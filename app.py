import streamlit as st
import pandas as pd

st.title("Nassau Candy Dashboard")

# 1. Data load
df = pd.read_excel("Tamanna_Nassau_Candy_Distributor.xlsx", header=None)
df.columns = ['Row Labels', 'Sum of Sales', 'Sum of Gross Profit', 'Average of Gross Margin%']
df = df.drop([0, 1, 2])
df = df[df['Row Labels'] != 'Grand Total']
df['Sum of Sales'] = pd.to_numeric(df['Sum of Sales'], errors='coerce')
df['Sum of Gross Profit'] = pd.to_numeric(df['Sum of Gross Profit'], errors='coerce')

# 2. Filter logic
selected_categories = st.sidebar.multiselect("Categories chunein:", df['Row Labels'].unique())
if not selected_categories:
    df_filtered = df
else:
    df_filtered = df[df['Row Labels'].isin(selected_categories)]

# 3. Metric
total_sales = df_filtered['Sum of Sales'].fillna(0).sum()
st.metric(label="Total Sales", value=f"{total_sales:,.2f}")

# 4. Graph
st.bar_chart(df_filtered.set_index('Row Labels')['Sum of Sales'])

# 5. Phase 3: Correlation (Sales vs Profit)
st.subheader("Analysis: Sales vs Profit Correlation")
corr = df_filtered['Sum of Sales'].corr(df_filtered['Sum of Gross Profit'])
st.write(f"Correlation value: **{corr:.2f}**")