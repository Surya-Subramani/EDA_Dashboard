import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("📊 Exploratory Data Analysis Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("🔍 Data Preview")
    st.write(df.head())

    st.subheader("📦 Data Summary")
    st.write(df.describe())

    st.subheader("🧱 Column Info")
    st.write(df.dtypes)

    column = st.selectbox("Choose a column to visualize", df.columns)

    if df[column].dtype == 'object':
        st.write("🔢 Value Counts")
        st.write(df[column].value_counts())
        fig = px.histogram(df, x=column, color=column)
        st.plotly_chart(fig)
    else:
        fig = px.histogram(df, x=column)
        st.plotly_chart(fig)

    st.subheader("📈 Correlation Heatmap")
    if st.checkbox("Show correlation matrix"):
        corr = df.select_dtypes(include=['float64', 'int64']).corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
