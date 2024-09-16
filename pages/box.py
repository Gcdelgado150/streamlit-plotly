import streamlit as st
from helpers import get_menu_plot, get_menu_doc
from helpers import remove_space_from_code_snippet
import plotly.express as px
import plotly.graph_objects as go
from helpers import create_sidebar


st.set_page_config(page_title=f"{__file__.split('/')[-1].capitalize().split('.')[0]}", 
                   layout="wide")
create_sidebar()

# Box
with st.container(border=True):
    st.header("Box plot using px.box")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.box.html",
                 link2="https://plotly.com/python/box-plots/")

    df = px.data.iris()
    st.write("Sample df: ", df.head(5))

    fig1 = px.box(df, x='species', y='sepal_width')
    st.plotly_chart(fig1, use_container_width=True)

    with st.expander("Show code"):
        code = '''
        fig1 = px.box(df, x='species', y='sepal_width')
        fig1.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
        plotly.express.box(data_frame=None, x=None, y=None, color=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, hover_name=None, hover_data=None, custom_data=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, orientation=None, boxmode=None, log_x=False, log_y=False, range_x=None, range_y=None, points=None, notched=False, title=None, template=None, width=None, height=None) → plotly.graph_objects._figure.Figure
        '''
        st.code(remove_space_from_code_snippet(code), language="python")