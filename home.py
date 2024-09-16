import streamlit as st
import os
from helpers import get_menu_plot
from helpers import create_sidebar

st.set_page_config(page_title="Visão Geral", 
                   layout="wide",
                   page_icon="🏠",
                   menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })
create_sidebar()

st.title("Opções de plots:")
get_menu_plot()