import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Starbucks Menu Profitability & Optimization",
    page_icon="?",
    layout="wide"
)

st.title("? Starbucks Menu Profitability & Optimization Dashboard")
st.markdown("Financial analysis of menu items, COGS, labor costs, margins, and net profit.")

# Load dataset from pkl file
pkl_file = 'starbucks_profitability_dataset.pkl'
if os.path.exists(pkl_file):
    df = pd.read_pickle(pkl_file)
    st.subheader("?? Dataset Overview")
    st.dataframe(df.head(10))
    
    st.subheader("Quick Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Menu Items", len(df))
    with col2:
        if 'Price' in df.columns:
            st.metric("Average Price", f"${df['Price'].mean():.2f}")
    with col3:
        if 'Net Profit' in df.columns:
            st.metric("Average Net Profit", f"${df['Net Profit'].mean():.2f}")
else:
    st.warning(f"Could not find `{pkl_file}`. Please make sure it is uploaded to your GitHub repository.")

# Load original HTML component if available
html_file = 'starbucks_product_profitability_menu_optimization.html'
if os.path.exists(html_file):
    st.subheader("?? Interactive Decision Tree & Visualizations")
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=800, scrolling=True)
else:
    st.info("HTML visualization file not detected.")