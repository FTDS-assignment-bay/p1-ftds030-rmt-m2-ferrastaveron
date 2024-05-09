import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
import xgboost as xgb


with open('list_num_cols.txt', 'rb') as file_1:
  num_col = json.load(file_1)

with open('list_cat_cols.txt', 'rb') as file_2:
  cat_col = json.load(file_2)
  
with open('num_pipeline.pkl', 'rb') as file_3:
  num_pipeline = pickle.load(file_3)

with open('cat_pipeline.pkl', 'rb') as file_4:
  cat_pipeline = pickle.load(file_4)

with open('preprocessing.pkl', 'rb') as file_5:
  preprocessing = pickle.load(file_5)

with open('xgboost.pkl', 'rb') as file_6:
  xg = pickle.load(file_6)

with open('pipe_xg_1.pkl', 'rb') as file_7:
  pipe_xg_1 = pickle.load(file_7)


def run():
  st.write('## Board Game Rating Prediction')
  with st.form('Board Game Rating Prediction'):
        min_players = st.number_input('Minimum number of players: ', min_value=1, value=1)
        max_players = st.number_input('Maxmium number of players: ', min_value=1, value=1) 
        playtime = st.number_input('Input average playing time: ', min_value=1, value=1, help='time in minutes')
        age = st.number_input('Input minimum age to play: ', min_value=1, value=5)
        complexity = st.number_input('Rate the complexity for newcomers: ', min_value=1, max_value=10, value=5)
        owned = st.number_input('How many people bought this game: ', min_value=1, value=1)
        mechanics = st.text_input('Type the top mechanic of the game: ', placeholder='Not Specified', help='refer to this [website](https://boardgamegeek.com/browse/boardgamemechanic)')
        domains = st.text_input('Type the top domain of the game: ', placeholder='Not Specified', help="e.g. Strategy Games, Family Games, Wargames, Thematic Games, Children's Games, Party Games, Customizable Games")

        submitted = st.form_submit_button('Predict Your Game Rating!')

  x_inf = {
      'min_players':min_players,
      'max_players':max_players,
      'playtime':playtime,
      'min_age':age,
      'complexity':complexity,
      'owned_users':owned,
      'top_mechanics':mechanics,
      'top_domains':domains
      }
  x_inf_df = pd.DataFrame([x_inf])
  st.dataframe(x_inf_df)


  if submitted:
     pred_inf = pipe_xg_1.predict(x_inf_df)
     st.write('Your Board Game Rating Prediction: ')
     st.write(pred_inf)
     
if __name__ == '__main__':
   run()