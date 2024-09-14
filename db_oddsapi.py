import streamlit as st
from sqlalchemy import text
from config import TABLE_BETS

conn = st.connection('oddsapi', type='sql')


@st.cache_data(ttl=10)
def get_bets(leagues: str, books: str, regions: str, min_val: float):

  return conn.query(f"SELECT starts, league, runner_home, runner_away, market, selection, side, line, odds, ref_odds, fair_odds, book, region, value, timestamp, odds_american, ref_odds_american, fair_odds_american FROM {TABLE_BETS} WHERE league IN {leagues} AND book IN {books} AND region IN {regions} AND value >= {min_val} AND starts >= NOW() ORDER BY starts", ttl=600).to_dict('records')


@st.cache_data(ttl=10)
def get_leagues():

  return conn.query(f"SELECT DISTINCT(league) FROM {TABLE_BETS} WHERE starts >= NOW()", ttl=600)['league'].tolist()


@st.cache_data(ttl=10)
def get_books(regions: str):

  return conn.query(f"SELECT DISTINCT(book) FROM {TABLE_BETS} WHERE starts >= NOW() AND region in {regions}", ttl=600)['book'].tolist()


@st.cache_data(ttl=10)
def get_regions():

  return conn.query(f"SELECT DISTINCT(region) FROM {TABLE_BETS} WHERE starts >= NOW()", ttl=600)['region'].tolist()
