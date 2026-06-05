import streamlit as st
import pandas as pd

st.set_page_config(page_title="Scorecard Cella", layout="wide")

st.title("📊 Weekly Scorecard Automation")

uploaded_file = st.file_uploader(
    "Upload Excel",
    type=["xlsx"]
)

if uploaded_file:

    xls = pd.ExcelFile(uploaded_file)

    st.success("Excel uploaded successfully")

    st.write("Sheets found:")
    st.write(xls.sheet_names)

    if "Cella" in xls.sheet_names:
        df_cella = pd.read_excel(uploaded_file, sheet_name="Cella")

        st.subheader("Preview - Sheet Cella")
        st.dataframe(df_cella.head(20))

    if "MASTER" in xls.sheet_names:
        df_master = pd.read_excel(uploaded_file, sheet_name="MASTER")

        st.subheader("Preview - Sheet MASTER")
        st.dataframe(df_master.head(20))
