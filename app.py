import streamlit as st
import pandas as pd

st.title("Weekly Scorecard Automation")

uploaded_file = st.file_uploader(
    "Upload Excel",
    type=["xlsx"]
)

if uploaded_file:

    raw = pd.read_excel(
        uploaded_file,
        sheet_name="Cella",
        header=None
    )

    st.write("Raw Sheet Cella")

    st.dataframe(raw.head(15))
