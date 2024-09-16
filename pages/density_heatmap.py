import streamlit as st
from helpers import get_menu_plot, get_menu_doc, remove_space_from_code_snippet
from helpers import create_sidebar
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Density Heatmap",
                   layout="wide")
create_sidebar()

with st.container(border=True):
    st.header("Density contour using px.density_heatmap")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.density_heatmap.html",
                 link2="https://plotly.com/python/2D-Histogram/")
    
    df = px.data.tips()
    st.write("Sample df: ", df.head(5))

    fig = px.density_heatmap(df, x="total_bill", y="tip")
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("Show code"):
        code = '''
        fig = px.density_heatmap(df, x="total_bill", y="tip")
        fig1.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
        plotly.express.density_heatmap(data_frame=None, x=None, y=None, z=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, hover_name=None, hover_data=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, orientation=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, marginal_x=None, marginal_y=None, opacity=None, log_x=False, log_y=False, range_x=None, range_y=None, histfunc=None, histnorm=None, nbinsx=None, nbinsy=None, text_auto=False, title=None, template=None, width=None, height=None) → plotly.graph_objects._figure.Figure
        '''
        st.code(remove_space_from_code_snippet(code), language="python")

with st.container(border=True):
    st.header("Density contour using go.Histogram2d")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.graph_objects.Histogram2d.html",
                 link2="https://plotly.com/python/2D-Histogram/")


    fig = go.Figure(go.Histogram2d(
            x=np.random.randn(500),
            y=np.random.randn(500)+1
        ))
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("Show code"):
        code = '''
        fig = go.Figure(go.Histogram2d(
            x=np.random.randn(500),
            y=np.random.randn(500)+1
        ))
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
        plotly.graph_objects.Histogram2d(arg=None, autobinx=None, autobiny=None, autocolorscale=None, bingroup=None, coloraxis=None, colorbar=None, colorscale=None, customdata=None, customdatasrc=None, histfunc=None, histnorm=None, hoverinfo=None, hoverinfosrc=None, hoverlabel=None, hovertemplate=None, hovertemplatesrc=None, ids=None, idssrc=None, legend=None, legendgroup=None, legendgrouptitle=None, legendrank=None, legendwidth=None, marker=None, meta=None, metasrc=None, name=None, nbinsx=None, nbinsy=None, opacity=None, reversescale=None, showlegend=None, showscale=None, stream=None, textfont=None, texttemplate=None, uid=None, uirevision=None, visible=None, x=None, xaxis=None, xbingroup=None, xbins=None, xcalendar=None, xgap=None, xhoverformat=None, xsrc=None, y=None, yaxis=None, ybingroup=None, ybins=None, ycalendar=None, ygap=None, yhoverformat=None, ysrc=None, z=None, zauto=None, zhoverformat=None, zmax=None, zmid=None, zmin=None, zsmooth=None, zsrc=None, **kwargs)
       '''
        st.code(remove_space_from_code_snippet(code), language="python")