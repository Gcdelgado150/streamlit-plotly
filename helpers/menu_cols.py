import os
import streamlit as st

def get_menu_plot(show_all=True, default_division=4):
    def show_pages():
        pages = sorted([page for page in os.listdir("./pages/") if page.endswith(".py")])
        how_many, remain = int(len(pages)/default_division), len(pages)%default_division

        gi = 0

        for j in range(how_many):
            cols = st.columns(int(len(pages)/how_many))

            for i, c in enumerate(cols):
                with c:
                    with st.container(border=True):
                        st.page_link(f"pages/{pages[gi]}", label=f"{pages[gi].capitalize().split('.')[0]}")
                    gi += 1

        if remain != 0:
            cols = st.columns(remain)

            for i, c in enumerate(cols):
                with c:
                    with st.container(border=True):
                        st.page_link(f"pages/{pages[gi]}", label=f"{pages[gi].capitalize().split('.')[0]}")
                    gi += 1 
    
    if show_all:
        show_pages()
    else:
        # st.page_link("home.py", label="Home", icon="🏠")
        with st.expander("Show all plot options"):
            show_pages()

def get_menu_doc(link1: str, link2: str):
    # Define the custom CSS for the buttons
    button_style = """
    <style>
    .button-89 {
    --b: 3px;   /* border thickness */
    --s: .45em; /* size of the corner */
    --color: #373B44;
    
    padding: calc(.5em + var(--s)) calc(.9em + var(--s));
    color: var(--color);
    --_p: var(--s);
    background:
        conic-gradient(from 90deg at var(--b) var(--b),#0000 90deg,var(--color) 0)
        var(--_p) var(--_p)/calc(100% - var(--b) - 2*var(--_p)) calc(100% - var(--b) - 2*var(--_p));
    transition: .3s linear, color 0s, background-color 0s;
    outline: var(--b) solid #0000;
    outline-offset: .6em;
    font-size: 16px;

    border: 0;

    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    }

    .button-89:hover,
    .button-89:focus-visible{
    --_p: 0px;
    outline-color: var(--color);
    outline-offset: .05em;
    }

    .button-89:active {
    background: var(--color);
    color: #fff;
    }
    </style>
    """

    
    st.markdown(button_style, unsafe_allow_html=True)

    # Create columns and add the custom links
    cols = st.columns(6)
    with cols[0]:
        st.markdown(f'<a class="button-89" href="{link1}" target="_blank">Plotly Documentation</a>', unsafe_allow_html=True)
    with cols[1]:
        st.markdown(f'<a class="button-89" href="{link2}" target="_blank">Plotly Example</a>', unsafe_allow_html=True)

