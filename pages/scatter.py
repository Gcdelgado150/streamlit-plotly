import streamlit as st
from helpers import get_menu_plot, get_menu_doc
from helpers import remove_space_from_code_snippet
import plotly.express as px
import plotly.graph_objects as go
from helpers import create_sidebar


st.set_page_config(page_title=f"{__file__.split('/')[-1].capitalize().split('.')[0]}", 
                   layout="wide")
create_sidebar()

# Scatter
with st.container(border=True):
    st.header("Scatter plot using px.scatter")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.scatter.html",
                 link2="https://plotly.com/python/line-and-scatter/")

    df = px.data.iris()
    st.write("Sample df: ", df.head(5))

    fig1 = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
    st.plotly_chart(fig1, use_container_width=True)

    with st.expander("Show code"):
        code = '''
        fig1 = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
        fig1.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
             plotly.express.scatter(data_frame=None, 
             x=None, y=None, color=None, symbol=None, size=None, 
             hover_name=None, hover_data=None, 
             custom_data=None, text=None, 
             facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, 
             error_x=None, error_x_minus=None, error_y=None, error_y_minus=None, 
             animation_frame=None, animation_group=None, 
             category_orders=None, labels=None, orientation=None, 
             color_discrete_sequence=None, color_discrete_map=None, color_continuous_scale=None, 
             range_color=None, color_continuous_midpoint=None, 
             symbol_sequence=None, symbol_map=None, opacity=None, size_max=None, 
             marginal_x=None, marginal_y=None, trendline=None, 
             trendline_options=None, trendline_color_override=None, 
             trendline_scope='trace', log_x=False, log_y=False, range_x=None, range_y=None, render_mode='auto', 
             title=None, template=None, width=None, height=None)
            → plotly.graph_objects._figure.Figure
        '''
        st.code(remove_space_from_code_snippet(code), language="python")



# Scatter 3D
with st.container(border=True):
    st.header("Scatter 3d using px.scatter_3d")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.scatter_3d.html",
                 link2="https://plotly.com/python/3d-scatter-plots/")

    st.write("Sample df: ", df.head(5))

    fig2 = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
    st.plotly_chart(fig2, use_container_width=True)

    with st.expander("Show code"):
        code = '''
        fig2 = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
        fig2.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
             plotly.express.scatter_3d(data_frame=None, x=None, y=None, z=None, color=None, symbol=None, size=None, text=None, hover_name=None, 
             hover_data=None, custom_data=None, error_x=None, error_x_minus=None, error_y=None, error_y_minus=None, error_z=None, error_z_minus=None, 
             animation_frame=None, animation_group=None, category_orders=None, labels=None, size_max=None, color_discrete_sequence=None, 
             color_discrete_map=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, symbol_sequence=None, 
             symbol_map=None, opacity=None, log_x=False, log_y=False, log_z=False, range_x=None, range_y=None, range_z=None, title=None, 
             template=None, width=None, height=None) → plotly.graph_objects._figure.Figure
        '''
        st.code(remove_space_from_code_snippet(code), language="python")

# Scatter Polar
with st.container(border=True):
    st.header("Scatter Polar using px.scatter_polar")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.scatter_polar.html",
                 link2="https://plotly.com/python/polar-chart/")

    df = px.data.wind()
    st.write("Sample df: ", df.head(5))

    fig3 = px.scatter_polar(df, r="frequency", theta="direction")
    st.plotly_chart(fig3, use_container_width=True)

    with st.expander("Show code"):
        code = '''
        fig3 = px.scatter_polar(df, r="frequency", theta="direction")
        fig3.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
        plotly.express.scatter_polar(data_frame=None, r=None, theta=None, color=None, symbol=None, size=None, hover_name=None, hover_data=None, 
        custom_data=None, text=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, 
        color_discrete_map=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, symbol_sequence=None, symbol_map=None, 
        opacity=None, direction='clockwise', start_angle=90, size_max=None, range_r=None, range_theta=None, log_r=False, render_mode='auto', title=None, 
        template=None, width=None, height=None) → plotly.graph_objects._figure.Figure
        '''
        st.code(remove_space_from_code_snippet(code), language="python")


# Scatter Ternary
with st.container(border=True):
    st.header("Scatter Ternary using px.scatter_polar")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.scatter_ternary.html",
                 link2="https://plotly.com/python/ternary-plots/")

    df = px.data.election()
    st.write("Sample df: ", df.head(5))

    fig4 = px.scatter_ternary(df, a="Joly", b="Coderre", c="Bergeron")
    st.plotly_chart(fig4, use_container_width=True)

    with st.expander("Show code"):
        code = '''
        fig4 = px.scatter_ternary(df, a="Joly", b="Coderre", c="Bergeron")
        fig4.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
        plotly.express.scatter_ternary(data_frame=None, a=None, b=None, c=None, color=None, symbol=None, size=None, text=None, hover_name=None, 
        hover_data=None, custom_data=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, 
        color_discrete_map=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, symbol_sequence=None, symbol_map=None, 
        opacity=None, size_max=None, title=None, template=None, width=None, height=None) → plotly.graph_objects._figure.Figure     
        '''
        st.code(remove_space_from_code_snippet(code), language="python")


# Scatter Mapbox
st.header("TODO: Scatter Mapbox using px.scatter_mapbox")
if 0:
    st.header("Scatter Mapbox using px.scatter_mapbox")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.scatter_mapbox.html",
                 link2="https://plotly.com/python/scattermapbox/")

    px.set_mapbox_access_token(open(".mapbox_token").read())
    df = px.data.carshare()
    st.write("Sample df: ", df.head(5))

    fig5 = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon",     color="peak_hour", size="car_hours",
                    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
    st.plotly_chart(fig5, use_container_width=True)

    with st.expander("Show code"):
        code = '''
        fig5 = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon",     color="peak_hour", size="car_hours",
                    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
        fig5.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
        plotly.express.scatter_mapbox(data_frame=None, lat=None, lon=None, color=None, text=None, hover_name=None, hover_data=None, custom_data=None, 
        size=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, 
        color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, opacity=None, size_max=None, zoom=8, center=None, mapbox_style=None, 
        title=None, template=None, width=None, height=None) → plotly.graph_objects._figure.Figure    
        '''
        st.code(remove_space_from_code_snippet(code), language="python")


# Scatter Geo
with st.container(border=True):
    st.header("Scatter Geo using px.scatter_geo")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.scatter_geo.html",
                 link2="https://plotly.com/python/scatter-plots-on-maps/")

    df = px.data.gapminder().query("year == 2007")
    st.write("Sample df: ", df.head(5))

    fig6 = px.scatter_geo(df, locations="iso_alpha",size="pop")
    st.plotly_chart(fig6, use_container_width=True)


    with st.expander("Show code"):
        code = '''
        fig6 = px.scatter_geo(df, locations="iso_alpha",size="pop")
        fig6.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
        plotly.express.scatter_geo(data_frame=None, lat=None, lon=None, locations=None, locationmode=None, geojson=None, featureidkey=None, color=None, 
        text=None, symbol=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, hover_name=None, 
        hover_data=None, custom_data=None, size=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, 
        color_discrete_sequence=None, color_discrete_map=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, 
        symbol_sequence=None, symbol_map=None, opacity=None, size_max=None, projection=None, scope=None, center=None, fitbounds=None, basemap_visible=None,
        title=None, template=None, width=None, height=None) → plotly.graph_objects._figure.Figure    
        '''
        st.code(remove_space_from_code_snippet(code), language="python")

# Scatter Matrix
with st.container(border=True):
    st.header("Scatter Matrix using px.scatter_matrix")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.scatter_matrix.html",
                 link2="https://plotly.com/python/splom/")

    df = px.data.iris()
    st.write("Sample df: ", df.head(5))

    fig7 = px.scatter_matrix(df)
    st.plotly_chart(fig7, use_container_width=True)


    with st.expander("Show code"):
        code = '''
        fig7 = px.scatter_matrix(df)
        fig7.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
        plotly.express.scatter_matrix(data_frame=None, dimensions=None, color=None, symbol=None, size=None, hover_name=None, hover_data=None, 
        custom_data=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, color_continuous_scale=None, 
        range_color=None, color_continuous_midpoint=None, symbol_sequence=None, symbol_map=None, opacity=None, size_max=None, title=None, template=None, 
        width=None, height=None) → plotly.graph_objects._figure.Figure   
        '''
        st.code(remove_space_from_code_snippet(code), language="python")


# # Example 3: Custom Plotly Figure using Graph Objects
# st.header("Custom Plot")
# fig3 = go.Figure()

# # Add traces
# fig3.add_trace(go.Scatter(
#     x=df['sepal_width'],
#     y=df['sepal_length'],
#     mode='markers',
#     marker=dict(color='rgba(135, 206, 250, 0.6)', size=10),
#     name='Scatter Plot'
# ))

# fig3.add_trace(go.Box(
#     y=df['sepal_width'],
#     name='Box Plot',
#     marker=dict(color='rgba(255, 165, 0, 0.6)')
# ))

# # Update layout
# fig3.update_layout(
#     title="Custom Plotly Figure",
#     xaxis_title="Sepal Width",
#     yaxis_title="Sepal Length",
#     legend_title="Legend"
# )

# # Display the figure in Streamlit
# st.plotly_chart(fig3, use_container_width=True)