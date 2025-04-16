import streamlit as st


if 'number_set' not in st.session_state:
    st.session_state.number_set = 1

if 'team_point' not in st.session_state:
    st.session_state.team_point = 0

if 'opp_point' not in st.session_state:
    st.session_state.opp_point = 0

if 'prev_point' not in st.session_state:
    st.session_state.prev_point = 0

st.title(f"SET {st.session_state.number_set}")

col1,col2,col3 = st.columns(3,gap="small", border=True)

with col1:
    st.write(st.session_state.team_point)
with col2:
    st.write("-")
with col3:
    st.write(st.session_state.opp_point, )

point,error = st.columns(2, gap="medium")

with point:
    point_button = st.button("V", key="point")
with error:
    error_button = st.button("X", key="error")








