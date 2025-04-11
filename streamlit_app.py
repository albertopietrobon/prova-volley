import streamlit as st
import pandas as pd
import numpy as np
import pathlib

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path = pathlib.Path("court.css")
load_css(css_path)

col1,col2,col3=st.columns(3,gap="small")

with col1:
    for i in range (1,4):
      st.button(f"{i}", key=f"butt{i}", use_container_width=True)
    st.button("block", key=f"butt4", use_container_width=True)
    for i in range (5,7):
      st.button(f"{i}", key=f"butt{i}", use_container_width=True)
    st.button("serve", key=f"butt7", use_container_width=True)

with col2:
    for i in range (8,11):
      st.button(f"{i}", key=f"butt{i}", use_container_width=True)
    st.button("block", key=f"butt11", use_container_width=True)
    for i in range (12,14):
      st.button(f"{i}", key=f"butt{i}", use_container_width=True)
    st.button("serve", key=f"butt14", use_container_width=True)

with col3:
    for i in range (15,18):
      st.button(f"{i}", key=f"butt{i}", use_container_width=True)
    st.button("block", key=f"butt18", use_container_width=True)
    for i in range (19,21):
      st.button(f"{i}", key=f"butt{i}", use_container_width=True)
    st.button("serve", key=f"butt21", use_container_width=True)
