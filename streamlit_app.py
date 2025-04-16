import streamlit as st
import pandas as pd

start_page = st.Page('pages/start_page.py', title='Start')
game_1 = st.Page('pages/game_1.py', title='Game_1')
set_page = st.Page('pages/set.py', title='Set')
court_page = st.Page('pages/court.py', title='Court')


pg = st.navigation([start_page,game_1,set_page,court_page], position='sidebar')
st.set_page_config(page_title='DV4S')

if "team name" not in st.session_state:
    st.session_state.team_name = 'Numia Vero Volley Milano'

if "opp_teams" not in st.session_state:
    st.session_state.opp_teams = [
        'Prosecco Doc Imoco Conegliano',
        'Savino Del Bene Scandicci',
        'Igor Gorgonzola Novara',
        'Reale Mutua Fenera Chieri 76',
        'Eurotek Uyba Busto Arsizio',
        'Megabox Ond. Savio Vallefoglia',
        'Bergamo',
        'Wash4green Pinerolo',
        'Bartoccini-Mc Restauri Perugia',
        'Honda Olivero Cuneo',
        'Il Bisonte Firenze',
        'Smi Roma Volley',
        'Cda Volley Talmassons Fvg'
    ]

team = {
     "Name": ['Helena Cazaute', 'Juliette Gelin','Ludovica Guidi', 'Laura Heyrman', 'Elena Pietrini', 'Alessia Orro', 'Anna Danesi', 'Lamprini Konstantinidou', 'Satomi Fukudome', 'Hena Kurtagic', 'Anna Smrek', 'Myriam Sylla', 'Paola Egonu', 'Nika Daalderop'],
     "Number":[1,2,3,5,7,8,11,12,13,14,15,17,18,19],
     "Role":['ATT','LIB','CEN','CEN','ATT','SET','CEN','SET','LIB','CEN','OPP','ATT','OPP','ATT'],
     "Age":[1997,2001,1992,1993,2000,1998,1996,1996,1997,2004,2003,1995,1998,1998],
     "Height":[184,162,186,188,186,180,196,184,162,195,207,181,193,190],
     "Nationality":['FRA','FRA','ITA','BEL','ITA','ITA','ITA','GRE','JPN','SRB','CAN','ITA','ITA','NED']
    }


if "roster" not in st.session_state:
    st.session_state.roster = team




pg.run()



