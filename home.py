import streamlit as st
import os
from helpers import get_menu_plot

st.set_page_config(layout="wide")
st.title("Home")
get_menu_plot()

# st.page_link("pages/bar.py", label="Bar", icon="2️⃣")
# st.page_link("pages/line.py", label="Line")