import streamlit as st
from helpers import get_menu_plot, get_menu_doc, remove_space_from_code_snippet
from helpers import create_sidebar
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


st.set_page_config(page_title=f"{__file__.split('/')[-1].capitalize().split('.')[0]}", 
                   layout="wide")
create_sidebar()

st.write("A Choropleth Map is a map composed of colored polygons. It is used to represent spatial variations of a quantity.")
with st.container(border=True):
    st.header("Choropleth using px.choropleth")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.choropleth.html",
                 link2="https://plotly.com/python/choropleth-maps/")

    df = px.data.election()
    st.write("Sample df: ", df.head(5))

    geojson = px.data.election_geojson()
    st.write("Sample geojson: ", df.head(5))

    fig1 = px.choropleth(df, 
                         geojson=geojson, 
                         color="Bergeron",
                         locations="district", 
                         featureidkey="properties.district",
                         projection="mercator"
                    )
    fig1.update_geos(fitbounds="locations", visible=False)
    fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig1, use_container_width=True)

    with st.expander("Show code"):
        code = '''
        fig1 = px.choropleth(df, 
                         geojson=geojson, 
                         color="Bergeron",
                         locations="district", 
                         featureidkey="properties.district",
                         projection="mercator"
                    )
        fig1.update_geos(fitbounds="locations", visible=False)
        fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig1.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
        plotly.express.choropleth(data_frame=None, lat=None, lon=None, locations=None, locationmode=None, geojson=None, featureidkey=None, color=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, hover_name=None, hover_data=None, custom_data=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, projection=None, scope=None, center=None, fitbounds=None, basemap_visible=None, title=None, template=None, width=None, height=None) → plotly.graph_objects._figure.Figure
        '''
        st.code(remove_space_from_code_snippet(code), language="python")


with st.container(border=True):
    st.header("Choropleth using go.Choropleth")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.graph_objects.Choropleth.html",
                 link2="https://plotly.com/python/choropleth-maps/")

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
    st.write("Sample df: ", df.head(5))
    
    fig1 = go.Figure(data=go.Choropleth(
        locations=df['code'], # Spatial coordinates
        z = df['total exports'].astype(float), # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = 'Reds',
        colorbar_title = "Millions USD",
    ))

    fig1.update_layout(
        title_text = '2011 US Agriculture Exports by State',
        geo_scope='usa', # limite map scope to USA
    )

    st.plotly_chart(fig1, use_container_width=True)

    with st.expander("Show code"):
        code = '''
        fig1 = go.Figure(data=go.Choropleth(
            locations=df['code'], # Spatial coordinates
            z = df['total exports'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Millions USD",
        ))

        fig1.update_layout(
            title_text = '2011 US Agriculture Exports by State',
            geo_scope='usa', # limite map scope to USA
        )
        fig1.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
        plotly.graph_objects.Choropleth(arg=None, autocolorscale=None, coloraxis=None, colorbar=None, colorscale=None, customdata=None, customdatasrc=None, featureidkey=None, geo=None, geojson=None, hoverinfo=None, hoverinfosrc=None, hoverlabel=None, hovertemplate=None, hovertemplatesrc=None, hovertext=None, hovertextsrc=None, ids=None, idssrc=None, legend=None, legendgroup=None, legendgrouptitle=None, legendrank=None, legendwidth=None, locationmode=None, locations=None, locationssrc=None, marker=None, meta=None, metasrc=None, name=None, reversescale=None, selected=None, selectedpoints=None, showlegend=None, showscale=None, stream=None, text=None, textsrc=None, uid=None, uirevision=None, unselected=None, visible=None, z=None, zauto=None, zmax=None, zmid=None, zmin=None, zsrc=None, **kwargs)
        '''
        st.code(remove_space_from_code_snippet(code), language="python")
