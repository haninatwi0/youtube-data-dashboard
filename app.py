import streamlit as st
import pandas as pd
import os
from visualizer import (
    create_views_likes_scatter,
    create_category_bar,
    create_engagement_box,
    create_time_series
)

st.set_page_config(page_title="YouTube Data Dashboard", layout="wide")

st.title("📊 YouTube Data Visualization Dashboard")
st.markdown("Interactive dashboard analyzing real Kaggle YouTube trends using **Python**, **Plotly Express**, and **Streamlit**.")

# Check if dataset exists
if not os.path.exists("youtube_data.csv"):
    st.error("⚠️ 'youtube_data.csv' not found! Please place your downloaded Kaggle CSV file in the project folder and rename it to 'youtube_data.csv'.")
    st.stop()

@st.cache_data
def load_data():
    df = pd.read_csv("youtube_data.csv")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Options")
categories = df['category_id'].unique()
selected_categories = st.sidebar.multiselect(
    "Select Category IDs",
    options=categories,
    default=categories
)

if selected_categories:
    filtered_df = df[df['category_id'].isin(selected_categories)]
else:
    filtered_df = df

# Metric KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Videos Analyzed", f"{len(filtered_df):,}")
col2.metric("Total Views", f"{filtered_df['views'].sum():,}")
col3.metric("Total Likes", f"{filtered_df['likes'].sum():,}")

st.markdown("---")

# Row 1 of Charts
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.plotly_chart(create_views_likes_scatter(filtered_df), use_container_width=True)

with row1_col2:
    st.plotly_chart(create_category_bar(filtered_df), use_container_width=True)

# Row 2 of Charts
row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.plotly_chart(create_engagement_box(filtered_df), use_container_width=True)

with row2_col2:
    st.plotly_chart(create_time_series(filtered_df), use_container_width=True)