import streamlit as st

new_game = st.button("NEW GAME")
game_history = st.button("GAME HISTORY")
player_stats = st.button("PLAYER STATS")


if new_game:
    st.switch_page("pages/game_1.py")