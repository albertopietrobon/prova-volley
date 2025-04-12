import streamlit as st
import pandas as pd
import numpy as np
import pathlib

#recall the court.css file to create the court
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = pathlib.Path("court.css")
load_css(css_path)

if 'step' not in st.session_state:
    st.session_state.step = 0

if 'point_start' not in st.session_state:
    st.session_state.point_start = 0

if 'point_end' not in st.session_state:
    st.session_state.point_end = 0

if 'point_block' not in st.session_state:
    st.session_state.point_block = 0

def click_step(i):
    st.session_state.step = i

def click_start(i):
    st.session_state.point_start = i

def click_end(i):
    st.session_state.point_end = i

def click_block(i):
    st.session_state.point_block = i

def return_set_page():
    st.session_state.step = 0
    st.switch_page("pages/set.py")
    


if st.session_state.step == 0:

    #creation of the court
    col1,col2,col3=st.columns(3,gap="small")

    with col1:
        b1 = st.button("1", key="butt1", on_click=click_end,args=[1], use_container_width=True)
        b2 = st.button("2", key="butt2", on_click=click_end,args=[2], use_container_width=True)
        b3 = st.button("3", key="butt3", on_click=click_end,args=[3], use_container_width=True)
        b4 = st.button("block", key="butt4", on_click=click_block,args=[4], use_container_width=True)
        b5 = st.button("5", key="butt5", on_click=click_start,args=[5], use_container_width=True)
        b6 = st.button("6", key="butt6", on_click=click_start,args=[6], use_container_width=True)
        b7 = st.button("serve", key="butt7", on_click=click_start,args=[7], use_container_width=True)

    with col2:
        b8 = st.button("8", key="butt8", on_click=click_end,args=[8], use_container_width=True)
        b9 = st.button("9", key="butt9", on_click=click_end,args=[9], use_container_width=True)
        b10 = st.button("10", key="butt10", on_click=click_end,args=[10], use_container_width=True)
        b11 = st.button("block", key="butt11", on_click=click_block,args=[11], use_container_width=True)
        b12 = st.button("12", key="butt12", on_click=click_start,args=[12], use_container_width=True)
        b13 = st.button("13", key="butt13", on_click=click_start,args=[13], use_container_width=True)
        b14 = st.button("serve", key="butt14", on_click=click_start,args=[14], use_container_width=True)

    with col3:
        b15 = st.button("15", key="butt15", on_click=click_end,args=[15], use_container_width=True)
        b16 = st.button("16", key="butt16", on_click=click_end,args=[16], use_container_width=True)
        b17 = st.button("17", key="butt17", on_click=click_end,args=[17], use_container_width=True)
        b18 = st.button("block", key=f"butt18", on_click=click_block,args=[18], use_container_width=True)
        b19 = st.button("19", key="butt19", on_click=click_start,args=[19], use_container_width=True)
        b20 = st.button("20", key="butt20", on_click=click_start,args=[20], use_container_width=True)
        b21 = st.button("serve", key=f"butt21", on_click=click_start,args=[21], use_container_width=True)


    save = st.button("Save point", key="save", on_click=click_step, args=[1])

if st.session_state.step == 1:
    st.info(f"Do you want to save the point?")
    back = st.button("Back", key="back", on_click=click_step, args=[0])
    confirm = st.button("Confirm", key="confirm", on_click=click_step, args = [2])

if st.session_state.step == 2:
    return_set_page()



