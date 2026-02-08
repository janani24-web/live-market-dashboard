import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="MSME Revenue Live")
st.title("📊 MSME Revenue – Real-Time Dashboard")


if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["date", "revenue"])

# REAL-TIME INPUT FORM 
st.sidebar.header("Add Revenue (Live)")

with st.sidebar.form("revenue_form", clear_on_submit=True):
    new_date = st.date_input("Date", date.today())
    new_revenue = st.number_input("Revenue", min_value=0, step=1000)
    submit = st.form_submit_button("Add Record")

if submit:

    new_row = pd.DataFrame([[pd.to_datetime(new_date), new_revenue]], columns=["date", "revenue"])
    st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
    st.sidebar.success("Data added instantly")
    st.rerun() 



display_df = st.session_state.df.sort_values("date")

if not display_df.empty:
    st.subheader("Revenue Trend")
    st.line_chart(display_df.set_index("date")["revenue"])
else:
    st.info("The dashboard is currently empty. Please add data via the sidebar.")

