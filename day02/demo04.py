import pandas as pd
import streamlit as st

st.title("CSV Explorer")

# upload a CSV file
data_file = st.file_uploader("Upload a CSV file", type=["csv"])
# load it as dataframe
if data_file:
    df = pd.read_csv(data_file)
    # display the dataframe
    st.dataframe(df)
