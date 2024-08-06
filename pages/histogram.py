import streamlit as st
from helpers import get_menu_plot

st.set_page_config(layout="wide")
st.title(f"{__file__.split('/')[-1].capitalize().split('.')[0]}")
get_menu_plot(show_all=False)