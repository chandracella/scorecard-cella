import streamlit as st
import pandas as pd

st.set_page_config(page_title="Scorecard Automation", layout="wide")

st.title("📊 Weekly Scorecard Automation")

uploaded_file = st.file_uploader(
    "Upload Excel",
    type=["xlsx"]
)

if uploaded_file:

    df = pd.read_excel(
        uploaded_file,
        sheet_name="Cella",
        header=0
    )

    # Ambil semua kolom week
    week_cols = []

    for col in df.columns:
        if "-" in str(col):
            week_cols.append(col)

    st.success("Excel loaded successfully")

    selected_week = st.selectbox(
        "Select Week",
        week_cols
    )

    st.write("Selected Week:", selected_week)

    st.subheader("Preview Data")

    preview_cols = [
        "AGENT LIST",
        "CODE",
        "STATION",
        selected_week
    ]

    preview_cols = [
        c for c in preview_cols
        if c in df.columns
    ]

    st.dataframe(
        df[preview_cols].head(30)
    )
