import streamlit as st
st.set_page_config(layout="wide")
col1,col2,col3 = st.columns([1,1,1])
with col2:
    st.title("일정에 맞는 여행 코스를 짜드립니다")
    st.link_button('label', 'app1.py', help=None, type="secondary", disabled=False, use_container_width=False)