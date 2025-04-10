import streamlit as st
import streamlit.components.v1 as components

col1,col2,col3 = st.columns(3,gap="small",vertical_alignment="center")

with col1:
    st.button("1",key="1_9m",use_container_width=True)
    st.markdown("""
    <style>
    div.stButton > button {
        background-color: #44c544;
        color: white;
        border-top: 3px solid white;
        border-left: 3px solid white;
        border-bottom: 0;
        border-right: 0;
        border-radius: 0px;
        font-size: 16px;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.2s ease, box-shadow 0.2s ease;

    }
    div.stButton > button:hover {
        background-color: red;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    <style>                                            
""",unsafe_allow_html=True)
    st.button("1",key="1_6m",use_container_width=True)
    st.markdown("""
    <style>
    div.stButton > button {
        background-color: red;
        color: white;
        border-top: 3px solid white;
        border-left: 3px solid white;
        border-bottom: 0;
        border-right: 0;
        border-radius: 0px;
        font-size: 16px;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.2s ease, box-shadow 0.2s ease;

    }
    div.stButton > button:hover {
        background-color: red;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    <style>                                            
""",unsafe_allow_html=True)
    st.button("2",key="2_3m",use_container_width=True)
    st.button("block",key="block2_3m",use_container_width=True)
with col2:
    st.button("6",key="6_9m",use_container_width=True)
    st.button("6",key="6_6m",use_container_width=True)
    st.button("3",key="3_3m",use_container_width=True)
    st.button("block",key="block3_3m",use_container_width=True)
with col3:
    st.button("5",key="5_9m",use_container_width=True)
    st.button("5",key="5_6m",use_container_width=True)
    st.button("4",key="4_3m",use_container_width=True)
    st.button("block",key="block4_3m",use_container_width=True)




