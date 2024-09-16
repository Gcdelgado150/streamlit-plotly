import streamlit as st
from helpers import get_menu_plot, get_menu_doc
from helpers import remove_space_from_code_snippet
import plotly.express as px
import plotly.graph_objects as go
from helpers import create_sidebar


st.set_page_config(page_title=f"{__file__.split('/')[-1].capitalize().split('.')[0]}", 
                   layout="wide")
create_sidebar()

# Bar
with st.container(border=True):
    st.header("Bar plot using px.bar")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.bar.html",
                 link2="https://plotly.com/python/bar-charts/")

    df = px.data.gapminder().query("country == 'Canada'")
    st.write("Sample df: ", df.head(5))

    fig1 = px.bar(df, x='year', y='pop')
    st.plotly_chart(fig1, use_container_width=True)

    with st.expander("Show code"):
        code = '''
        fig1 = px.bar(df, x='year', y='pop')
        fig1.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
             plotly.express.bar(data_frame=None, x=None, y=None, color=None, pattern_shape=None, facet_row=None, facet_col=None, facet_col_wrap=0, 
             facet_row_spacing=None, facet_col_spacing=None, hover_name=None, hover_data=None, custom_data=None, text=None, base=None, error_x=None, 
             error_x_minus=None, error_y=None, error_y_minus=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, 
             color_discrete_sequence=None, color_discrete_map=None, color_continuous_scale=None, pattern_shape_sequence=None, pattern_shape_map=None, 
             range_color=None, color_continuous_midpoint=None, opacity=None, orientation=None, barmode='relative', log_x=False, log_y=False, range_x=None, 
             range_y=None, text_auto=False, title=None, template=None, width=None, height=None) → plotly.graph_objects._figure.Figure
        '''
        st.code(remove_space_from_code_snippet(code), language="python")