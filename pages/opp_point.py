import streamlit as st
import pandas as pd
import numpy as np
import pathlib

#recall the court.css file to create the court
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = pathlib.Path("assets/opp_point.css")
load_css(css_path)

if 'step' not in st.session_state:
    st.session_state.step = 0

if 'point_att' not in st.session_state:
    st.session_state.point_att = 0

if 'point_def' not in st.session_state:
    st.session_state.point_def = 0

if 'point_block' not in st.session_state:
    st.session_state.point_block = 0

def click_step(i):
    st.session_state.step = i

def click_att(i):
    st.session_state.point_att = i

def click_def(i):
    st.session_state.point_def = i
    st.session_state.point_block = 0

def click_block(i):
    st.session_state.point_block = i
    st.session_state.point_def = 0

def return_set_page():
    st.session_state.step = 0
    st.switch_page("pages/set.py")
    


if st.session_state.step == 0:

    #creation of the court
    col1,col2,col3=st.columns(3,gap="small")

    with col1:
        ob1 = st.button("serve", key="obutt1", on_click=click_att,args=['serve-1'], use_container_width=True)
        ob2 = st.button("1", key="obutt2", on_click=click_att,args=['att-1'], use_container_width=True)
        ob3 = st.button("2", key="obutt3", on_click=click_att,args=['att-2'], use_container_width=True)
        ob4 = st.button("block", key="obutt4", on_click=click_block,args=['block-4'], use_container_width=True)
        ob5 = st.button("4", key="obutt5", on_click=click_def,args=['def-4'], use_container_width=True)
        ob6 = st.button("10", key="obutt6", on_click=click_def,args=['def-10'], use_container_width=True)
        ob7 = st.button("5", key="obutt7", on_click=click_def,args=['def-5'], use_container_width=True)

    with col2:
        ob8 = st.button("serve", key="obutt8", on_click=click_att,args=['serve-6'], use_container_width=True)
        ob9 = st.button("6", key="obutt9", on_click=click_att,args=['att-6'], use_container_width=True)
        ob10 = st.button("3", key="obutt10", on_click=click_att,args=['att-3'], use_container_width=True)
        ob11 = st.button("block", key="obutt11", on_click=click_block,args=['block-3'], use_container_width=True)
        ob12 = st.button("3", key="obutt12", on_click=click_def,args=['def-3'], use_container_width=True)
        ob13 = st.button("9", key="obutt13", on_click=click_def,args=['def-9'], use_container_width=True)
        ob14 = st.button("6", key="obutt14", on_click=click_def,args=['def-6'], use_container_width=True)

    with col3:
        ob15 = st.button("serve", key=f"obutt15", on_click=click_att,args=['serve-5'], use_container_width=True)
        ob16 = st.button("5", key="obutt16", on_click=click_att,args=['att-5'], use_container_width=True)
        ob17 = st.button("4", key="obutt17", on_click=click_att,args=['att-4'], use_container_width=True)
        ob18 = st.button("block", key="obutt18", on_click=click_block,args=['block-2'], use_container_width=True)
        ob19 = st.button("2", key=f"obutt19", on_click=click_def,args=['def-2'], use_container_width=True)
        ob20 = st.button("8", key="obutt20", on_click=click_def,args=['def-8'], use_container_width=True)
        ob21 = st.button("1", key="obutt21", on_click=click_def,args=['def-1'], use_container_width=True)


    confirm = st.button("Confirm point", key="oconfirm", on_click=click_step, args=[1])

if st.session_state.step == 1:

    if st.session_state.point_att != 0 and st.session_state.point_block !=0:
        st.info(f"You selected: error in {st.session_state.point_block} from {st.session_state.point_att} .\n\nDo you want to save the action?")
        back = st.button("Back", key="oback", on_click=click_step, args=[0])
        save = st.button("Save", key="osave", on_click=click_step, args = [2])

        
    elif st.session_state.point_att != 0 and st.session_state.point_def !=0:
        st.info(f"You selected: error in {st.session_state.point_def} from {st.session_state.point_att}.\n\nDo you want to save the action?")
        back = st.button("Back", key="oback", on_click=click_step, args=[0])
        save = st.button("Save", key="osave", on_click=click_step, args = [2])

    
    elif (st.session_state.point_att==0) or (st.session_state.point_def==0 and st.session_state.point_block==0):
        st.warning("Please go back. You are missing the point selection!")
        back = st.button("Back", key="oback", on_click=click_step, args=[0])
        
        
if st.session_state.step == 2:
    #method to save the points
    #reset all the variables:
    st.session_state.point_att = 0
    st.session_state.point_def = 0
    st.session_state.point_block = 0

    return_set_page()


