import time
import pandas as pd
import streamlit as st
from st_paywall import add_auth

st.set_page_config(page_title="PropHunter by BettingIsCool", page_icon="🍀", layout="wide", initial_sidebar_state="expanded")

import db_oddsapi as db
from datetime import datetime

from config import TEXT_LANDING_PAGE, TEXT_BEST_PRACTICE

placeholder1 = st.empty()
placeholder1.markdown(TEXT_LANDING_PAGE)

add_auth(required=True)

placeholder1.empty()


def refresh_table():

  st.cache_data.clear()


def color_cells(val):

  color = 'white'
  if val is not None:
    
    if val > 0.05:
        color = 'green'
    elif val > 0.025:
      color = 'yellow'

  return f'color: {color}'


def highlight_outdated_odds(val):

 if (datetime.now() - val).total_seconds() > 600:
  color = 'red' 
 else:
  color = 'green'
 return f'color: {color}'

st.button('Refresh Table', on_click=refresh_table)

odds_display = st.sidebar.radio("Display Odds", ['Decimal', 'American'], index=0)

bankroll = st.sidebar.number_input("Bankroll", min_value=0.01, value=2500.00, step=1.00, format="%0.2f")

min_val = st.sidebar.slider(label='Min Value Percentage', min_value=0.00, max_value=25.0, value=2.5, step=0.5)

unique_leagues = ['NFL', 'NBA', 'NHL', 'MLB']
selected_leagues = st.sidebar.multiselect(label='Leagues', options=sorted(unique_leagues), default=unique_leagues)
selected_leagues = [f"'{s}'" for s in selected_leagues]
selected_leagues = f"({','.join(selected_leagues)})"

unique_regions = ['au', 'eu', 'us', 'u2', 'uk']
selected_regions = st.sidebar.multiselect(label='Regions', options=sorted(unique_regions), default=unique_regions)
selected_regions = [f"'{s}'" for s in selected_regions]
selected_regions = f"({','.join(selected_regions)})"

if selected_regions != '()':
  
  unique_books = db.get_books(regions=selected_regions)
  selected_books = st.sidebar.multiselect(label='Bookmakers', options=sorted(unique_books), default=unique_books)
  selected_books = [f"'{s}'" for s in selected_books]
  selected_books = f"({','.join(selected_books)})"

  if selected_books != '()':
  
    bets = db.get_bets(leagues=selected_leagues, books=selected_books, regions=selected_regions, min_val=float(min_val) / 100)
    
    if bets:
    
      bets_df = pd.DataFrame(bets)

      # Add kelly stakes
      stakes = list()
      for index, row in bets_df.iterrows():
        stakes.append(bankroll * row['value'] / (row['odds'] - 1))
      bets_df.insert(11, 'K-STAKE', stakes, True)
      
      #bets_df = bets_df.rename(columns={'starts': 'STARTS', 'league': 'LEAGUE', 'runner_home': 'HOME_TEAM', 'runner_away': 'AWAY_TEAM', 'market': 'MARKET', 'selection': 'SELECTION', 'side': 'SIDE', 'line': 'LINE', 'odds_american': 'ODDS', 'ref_odds_american': 'REF_ODDS', 'fair_odds_american': 'FAIR_ODDS', 'book': 'BOOKMAKER', 'region': 'REGION', 'value': 'VALUE', 'timestamp': 'LAST_UPDATE'})

      if odds_display == 'American':
        bets_df = bets_df.rename(columns={'starts': 'STARTS', 'league': 'LEAGUE', 'runner_home': 'HOME_TEAM', 'runner_away': 'AWAY_TEAM', 'market': 'MARKET', 'selection': 'SELECTION', 'side': 'SIDE', 'line': 'LINE', 'odds_american': 'ODDS', 'ref_odds_american': 'REF_ODDS', 'fair_odds_american': 'FAIR_ODDS', 'book': 'BOOKMAKER', 'link': 'LINK', 'region': 'REGION', 'value': 'VALUE', 'timestamp': 'LAST_UPDATE'})
        bets_df = bets_df[['STARTS', 'LEAGUE', 'HOME_TEAM', 'AWAY_TEAM', 'MARKET', 'SELECTION', 'SIDE', 'LINE', 'ODDS', 'REF_ODDS', 'FAIR_ODDS', 'VALUE', 'K-STAKE', 'BOOKMAKER', 'LINK', 'REGION', 'LAST_UPDATE']]
        styled_df = bets_df.style.applymap(color_cells, subset=['VALUE']).applymap(highlight_outdated_odds, subset=['LAST_UPDATE']).format({'LINE': '{:g}'.format, 'ODDS': '{0:g}'.format, 'REF_ODDS': '{0:g}'.format, 'FAIR_ODDS': '{0:g}'.format, 'VALUE': '{:,.2%}'.format, 'K-STAKE': '{:,.0f}'.format})
      elif odds_display == 'Decimal':
        bets_df = bets_df.rename(columns={'starts': 'STARTS', 'league': 'LEAGUE', 'runner_home': 'HOME_TEAM', 'runner_away': 'AWAY_TEAM', 'market': 'MARKET', 'selection': 'SELECTION', 'side': 'SIDE', 'line': 'LINE', 'odds': 'ODDS', 'ref_odds': 'REF_ODDS', 'fair_odds': 'FAIR_ODDS', 'book': 'BOOKMAKER', 'link': 'LINK', 'region': 'REGION', 'value': 'VALUE', 'timestamp': 'LAST_UPDATE'})
        bets_df = bets_df[['STARTS', 'LEAGUE', 'HOME_TEAM', 'AWAY_TEAM', 'MARKET', 'SELECTION', 'SIDE', 'LINE', 'ODDS', 'REF_ODDS', 'FAIR_ODDS', 'VALUE', 'K-STAKE', 'BOOKMAKER', 'LINK', 'REGION', 'LAST_UPDATE']]
        styled_df = bets_df.style.applymap(color_cells, subset=['VALUE']).applymap(highlight_outdated_odds, subset=['LAST_UPDATE']).format({'LINE': '{:g}'.format, 'ODDS': '{:,.3f}'.format, 'REF_ODDS': '{:,.3f}'.format, 'FAIR_ODDS': '{:,.3f}'.format, 'VALUE': '{:,.2%}'.format, 'K-STAKE': '{:,.0f}'.format})
      
      if len(bets_df) > 0:
        st.dataframe(styled_df, column_config={"LINK": st.column_config.LinkColumn("LINK")})
        st.markdown(TEXT_BEST_PRACTICE)
