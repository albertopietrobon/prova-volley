import streamlit as st

st.title("SET page")

if "att_point" not in st.session_state:
    st.session_state.att_point=0

if "dif_point" not in st.session_state:
    st.session_state.dif_point=0

if "mur_point" not in st.session_state:
    st.session_state.mur_point=0

def attack():
    st.session_state.att_point=1
    st.session_state.mur_point=0

def defense():
    st.session_state.dif_point=1
    st.session_state.mur_point=0

def block():
    st.session_state.mur_point=1
    st.session_state.att_point=0
    st.session_state.dif_point=0


st.button("attacco", key="att", on_click=attack)
st.button("difesa", key="dif", on_click=defense)
st.button("muro", key="mur", on_click=block)
save_butt= st.button("SAVE")

if save_butt:
    if st.session_state.mur_point != 0:
        st.info("Block")
        st.session_state.mur_point = 0
        st.session_state.att_point = 0
        st.session_state.dif_point = 0
    elif st.session_state.att_point != 0 and st.session_state.dif_point !=0:
        st.info("Point on attack")
        st.session_state.mur_point = 0
        st.session_state.att_point = 0
        st.session_state.dif_point = 0
    elif (st.session_state.att_point == 0 and st.session_state.dif_point !=0) or (st.session_state.att_point != 0 and st.session_state.dif_point ==0) or (st.session_state.att_point == 0 and st.session_state.dif_point ==0 and st.session_state.mur_point == 0):
        st.warning("Go back! missing selection")
        st.session_state.mur_point = 0
        st.session_state.att_point = 0
        st.session_state.dif_point = 0

