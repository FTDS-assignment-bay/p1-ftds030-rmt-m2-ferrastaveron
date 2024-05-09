import streamlit as st
import prediction
import eda

page = st.sidebar.selectbox('Pilih Halaman:', ('EDA', 'Prediction'))

if page == 'EDA':
    eda.run()
else:
    prediction.run()