import streamlit as st
import pandas as pd

if 'step' not in st.session_state:
    st.session_state.step = 0

if "game_date" not in st.session_state:
    st.session_state.game_date = None

if "game_opp" not in st.session_state:
    st.session_state.game_opp = None

if "game_roster" not in st.session_state:
    st.session_state.game_roster = None

def click_step(i):
    st.session_state.step = i

def return_home():
    st.session_state.step = 0
    st.switch_page("pages/start_page.py")

def start_game():
    st.session_state.step = 0
    st.switch_page("pages/set.py")



if st.session_state.step == 0:
    tab1,tab2,tab3 = st.tabs(['Game Date', 'Opponent Team', 'Game Roster'])

    with tab1:
        st.session_state.game_date = st.date_input("Select the game's date from the calendar:")
    with tab2:
        st.session_state.game_opp = st.radio("Select the opponent team:", st.session_state.opp_teams)
    with tab3:
        st.write("Details of available players:") 
        st.dataframe(st.session_state.roster)
        st.session_state.game_roster = st.multiselect("Select all the players for the match:", st.session_state.roster['Name'], placeholder="Choose a player...")

    col1,col2 = st.columns(2)

    with col1:
        home = st.button(":house:", on_click=click_step, args=[2])
    with col2:
        report = st.button("Report", on_click=click_step, args=[1])

if st.session_state.step == 1:
    if len(st.session_state.game_roster) != 14 :
        st.warning("You are missing required information. Please finish to fill all the fields.")
        back = st.button("Back", on_click=click_step, args=[0])
    else:
        st.write(f">Game date: {st.session_state.game_date}")
        st.write(f">Opponent team: {st.session_state.game_opp}")
        st.write(f">Game roster: {st.session_state.game_roster}")
        col1,col2 = st.columns(2)

        with col1:
            back = st.button("Back", on_click=click_step, args=[0])
        with col2:
            save = st.button("Save", on_click=click_step, args=[3])

    
    

if st.session_state.step == 2:
    return_home()

if st.session_state.step == 3:
    #save the data related to date, opp and roster
    start_game()