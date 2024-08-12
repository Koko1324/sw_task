import streamlit as st
from streamlit_option_menu import option_menu
#st.set_page_config(layout="wide")
#col1,col2,col3 = st.columns([1,1,1])
#with col2:
#    st.title("일정에 맞는 여행 코스를 짜드립니다")
opt = option_menu("MENU", ["세부 조회", "키워드 조회"],
            icons=['bi bi-search', 'bi bi-zoom-in'],
            menu_icon="bi bi-three-dots", default_index=0,
             styles={
        "container": {"padding": "5!important", "background-color": "#575757"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "grey"},
        "nav-link-selected": {"background-color": "#00ddff"},
        }
        )
if opt == "세부 조회":
            st.write('hello')
if opt == "키워드 조회":
            st.write("hi")
