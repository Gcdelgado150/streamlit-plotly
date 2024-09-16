import streamlit as st
from datetime import datetime
import pickle
import os
from streamlit_extras.switch_page_button import switch_page

def create_sidebar():
    st.sidebar.title("Plotly Plots")
    st.sidebar.page_link("home.py", label="Visão Geral") 
    st.sidebar.divider()

    pages_list = sorted([page.split(".")[0].capitalize() for page in os.listdir("./pages/") if page.endswith(".py")])

    cols = st.sidebar.columns([1, 3, 1])   

    with cols[0]:
        st.write("Plots: ")
    with cols[1]:
        pagename = st.selectbox(label="Plots", 
                                options=pages_list,
                                label_visibility="collapsed")

    with cols[2]:
        button_go = st.button("Go")

    if button_go:
        switch_page(pagename.lower())

    st.sidebar.divider()

    st.sidebar.header("Plots:", divider="gray")
    st.sidebar.page_link("pages/area.py", label="Area")
    st.sidebar.page_link("pages/bar.py",  label="Bar")
    st.sidebar.page_link("pages/box.py",  label="Box")
    st.sidebar.page_link("pages/choropleth.py", label="Choropleth")

    st.sidebar.page_link("pages/density_contour.py", label="Density Contour")
    st.sidebar.page_link("pages/density_heatmap.py", label="Density Heatmap")
    st.sidebar.page_link("pages/density_map.py", label="Density Map")
    st.sidebar.page_link("pages/density_mapbox.py", label="Density Mapbox")

    st.sidebar.page_link("pages/ecdf.py",       label="Ecdf")
    st.sidebar.page_link("pages/funnel.py",     label="Funnel")
    st.sidebar.page_link("pages/histogram.py",  label="Histogram")
    st.sidebar.page_link("pages/icicle.py",     label="Icicle")
    st.sidebar.page_link("pages/imshow.py",     label="Imshow")
    st.sidebar.page_link("pages/line.py",       label="Line")
    st.sidebar.page_link("pages/others.py",     label="Others")
    st.sidebar.page_link("pages/parallel.py",   label="Parallel")
    st.sidebar.page_link("pages/pie.py",        label="Pie")
    st.sidebar.page_link("pages/scatter.py",    label="Scatter")
    st.sidebar.page_link("pages/strip.py",      label="Strip")
    st.sidebar.page_link("pages/sunburst.py",   label="Sunburst")
    st.sidebar.page_link("pages/timeline.py",   label="Timeline")
    st.sidebar.page_link("pages/treemap.py",    label="Treemap")
    st.sidebar.page_link("pages/violin.py",     label="Violin")

    st.sidebar.divider()