import streamlit as st
from helpers import get_menu_plot
from helpers import create_sidebar


st.set_page_config(page_title=f"{__file__.split('/')[-1].capitalize().split('.')[0]}", 
                   layout="wide")
create_sidebar()