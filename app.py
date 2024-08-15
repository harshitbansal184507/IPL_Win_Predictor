import streamlit as st
import pickle 
import pandas as pd 
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt

pipe = pickle.load(open("pipe5.pkl","rb"))
st.markdown(
    """
    <style>
    .title-container {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .title-container img {
        height: 60px; /* Adjust the size of the logo */
        margin-right: 15px;
    }
    .title-container h1 {
        color: white;
    }
    </style>
    <div class="title-container">
        <img src="https://thefederal.com/file/2023/01/ipl-logo.webp" alt="IPL Logo">
        <h1>IPL Win Predictor</h1>
    </div>
    """, unsafe_allow_html=True)
teams = ['Mumbai Indians',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Sunrisers Hyderabad',
 'Delhi Capitals',
 'Punjab Kings',
 'Lucknow Super Giants',
 'Gujarat Titans',
 'Royal Challengers Bengaluru']

cities = ['Bangalore', 'Delhi', 'Mumbai', 'Kolkata', 'Hyderabad', 'Chennai',
       'Jaipur', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
       'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
       'Ahmedabad', 'Cuttack', 'Nagpur', 'Visakhapatnam', 'Pune',
       'Raipur', 'Ranchi', 'Abu Dhabi', 'Bengaluru', 'Dubai',
       'Sharjah', 'Navi Mumbai', 'Chandigarh', 'Lucknow', 'Guwahati',
       'Dharamsala', 'Mohali']

col1 , col2 = st.columns(2)

with col1 :
    batting_team =st.selectbox("Select the batting team",sorted(teams))
with col2 :
    bowling_team = st.selectbox("Select the bowling team",sorted(teams))    


city = st.selectbox("Select the city",sorted(cities))

target=st.number_input("Target",step=1)

col3 , col4 , col5 = st.columns(3)
with col3 :
    score = st.number_input("Score",step=1)
with col4 :
    overs = st.number_input("Overs",min_value=0,max_value=20)
with col5 :
    wickets = st.number_input("Wickets",min_value=0,max_value=10)
if st.button("Predict"):
    
    runs_left= target - score
    balls_left = 120- (overs*6)
    wickets = 10-wickets
    crr= score/overs 
    rr = (runs_left*6)/balls_left
    data = {
    "batting_team": [batting_team],
    "bowling_team": [bowling_team],
    "city": [city],
    "runs_left": [runs_left],
    "balls_left": [balls_left],
    "wickets_left": [wickets],
    "total_runs_x": [target],
    "crr": [crr],
    "rr": [rr]
        }

    input_df = pd.DataFrame(data)

    result = pipe.predict_proba(input_df)
    loss= result[0][0]
    win = result[0][1]
    st.header("Batting Team : "+ str(round(win*100)) + "%")
    st.header("Bowling Team : "+ str(round(loss*100)) + "%")
    fig, ax = plt.subplots(figsize=(8, 0.75),)
    bars = ['Batting Team', 'Bowling Team']
    values = [round(win*100), round(loss*100)]
    teams_probs = {
        "Batting Team":win,  
        "Bowling Team": loss  
    }
    fig.patch.set_facecolor('grey')
    ax.set_facecolor('grey')
    ax.barh('Winning Probability', values[0], color='red', label=batting_team)
    ax.barh('Winning Probability', values[1],left=values[0], color='blue', label=bowling_team)
    
    ax.tick_params(axis='both', colors='white', labelsize=10, pad=10) 
    ax.set_xlim(0, 100,)  # Set x-axis to 0-1 for a percentage scale
    ax.set_xlabel('')
    ax.set_title('')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small', frameon=False)

    st.pyplot(fig)