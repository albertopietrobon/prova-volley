import streamlit as st


set_page = st.Page('pages/set.py', title='Set')
court_page = st.Page('pages/court.py', title='Court')

pg = st.navigation([set_page,court_page], position='sidebar')
st.set_page_config(page_title='DV4S')


pg.run()



