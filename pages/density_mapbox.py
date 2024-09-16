import streamlit as st
from helpers import get_menu_plot, get_menu_doc, remove_space_from_code_snippet
from helpers import create_sidebar
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Density Mapbox",
                   layout="wide")
create_sidebar()

with st.container(border=True):
    st.header("Density contour using px.density_heatmap")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.density_mapbox.html",
                 link2="https://plotly.com/python/density-heatmaps/")