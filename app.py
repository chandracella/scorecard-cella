import streamlit as st

st.set_page_config(page_title="Scorecard Cella")

st.title("📊 Weekly Scorecard Automation")

uploaded_file = st.file_uploader(
    "Upload Excel",
    type=["xlsx"]
)

if uploaded_file:
    st.success("Excel uploaded successfully")
