import streamlit as st
import pandas as pd

st.title("Scorecard Automation")

uploaded_file = st.file_uploader(
    "Upload Excel",
    type=["xlsx"]
)

if uploaded_file:

    master = pd.read_excel(
        uploaded_file,
        sheet_name="MASTER",
        nrows=10
    )

    st.write(master.head(10))
