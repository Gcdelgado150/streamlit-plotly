import streamlit as st
from helpers import get_menu_plot, get_menu_doc
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title(f"{__file__.split('/')[-1].capitalize().split('.')[0]}")
get_menu_plot(show_all=False)
get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.box.html",
             link2="https://plotly.com/python/box-plots/")

df = px.data.iris()
fig = px.box(df, x='species', y='sepal_width')
st.plotly_chart(fig, use_container_width=True)
