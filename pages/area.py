import streamlit as st
from helpers import get_menu_plot, get_menu_doc
from helpers import remove_space_from_code_snippet
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title(f"{__file__.split('/')[-1].capitalize().split('.')[0]}")
get_menu_plot(show_all=False)

# Area
if 1:
    st.header("Area plot using px.area")
    get_menu_doc(link1="https://plotly.com/python-api-reference/generated/plotly.express.area.html",
                 link2="https://plotly.com/python/filled-area-plots/")

    df = px.data.gapminder()
    st.write("Sample df: ", df.head(5))

    fig1 = px.area(df, x="year", y="pop", color="continent", line_group="country")
    st.plotly_chart(fig1, use_container_width=True)

    with st.expander("Show code"):
        code = '''
        fig1 = px.area(df, x="year", y="pop", color="continent", line_group="country")
        fig1.show()
        '''
        st.code(code, language="python")

    with st.expander("Show snippet"):
        code = '''
             plotly.express.area(data_frame=None, x=None, y=None, line_group=None, color=None, pattern_shape=None, symbol=None, hover_name=None, hover_data=None, custom_data=None, text=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, pattern_shape_sequence=None, pattern_shape_map=None, symbol_sequence=None, symbol_map=None, markers=False, orientation=None, groupnorm=None, log_x=False, log_y=False, range_x=None, range_y=None, line_shape=None, title=None, template=None, width=None, height=None) → plotly.graph_objects._figure.Figure
        '''
        st.code(remove_space_from_code_snippet(code), language="python")