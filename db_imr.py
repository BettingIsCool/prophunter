import streamlit as st
from sqlalchemy import text
from config import TABLE_LOG, TABLE_USERS, TABLE_BETS

conn = st.connection('imr', type='sql')


@st.cache_data(ttl=10)
def get_log(sports: str, leagues: str, min_diff: float, min_limit: float):

  return conn.query(f"SELECT event_id, starts, sport_name, league_name, runner_home, runner_away, line, spread_home, spread_away, spread_home_max, diff_home, diff_away, stake_home, stake_away, timestamp, ratings_updated FROM {TABLE_LOG} WHERE starts >= NOW() AND type = 'c' AND sport_name IN {sports} AND league_name IN {leagues} AND (diff_home >= {min_diff} OR diff_away >= {min_diff}) AND spread_home_max >= {min_limit} ORDER BY starts", ttl=600).to_dict('records')


@st.cache_data(ttl=10)
def get_sports():

  return conn.query(f"SELECT DISTINCT(sport_name) FROM {TABLE_LOG} WHERE starts >= NOW()", ttl=600)['sport_name'].tolist()


@st.cache_data(ttl=10)
def get_leagues():

  return conn.query(f"SELECT DISTINCT(league_name) FROM {TABLE_LOG} WHERE starts >= NOW()", ttl=600)['league_name'].tolist()


@st.cache_data(ttl=10)
def get_users():

  return conn.query(f"SELECT name, username, password FROM {TABLE_USERS}", ttl=600).to_dict('records')


#@st.cache_data(ttl=10)
def get_processed_bets(username: str):

  return conn.query(f"SELECT event_id FROM {TABLE_BETS} WHERE username = '{username}'", ttl=600)['event_id'].tolist()


#@st.cache_data(ttl=10)
def delete_processed_bet(username: str, event_id: int):

  query = f"DELETE FROM {TABLE_BETS} WHERE username = '{username}' AND event_id = {event_id}"

  with conn.session as session:
    session.execute(text(query))
    session.commit()


#@st.cache_data(ttl=10)
def append_processed_bet(username: str, event_id: int):

  query = f"INSERT INTO {TABLE_BETS} (username, event_id) VALUES(:username, :event_id)"

  with conn.session as session:
    session.execute(text(query), params = dict(username = username, event_id = event_id))
    session.commit()    
