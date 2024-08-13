import streamlit as st
from PIL import Image

# 페이지 레이아웃 설정
st.set_page_config(layout="wide")

# 로고 이미지를 열고, 크기를 조절합니다.
logo = Image.open("logo.png")

# 세션 상태를 초기화합니다.
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = '홈'

# 헤더 섹션을 만들기 위해 열(column)을 나눕니다.
header_col1, header_col2 = st.columns([1, 5])

#레이아웃 나누기
col3, col4, col5, col6 = st.columns([1,1,1,1])

with header_col1:
    # 첫 번째 열에 로고 이미지를 추가합니다.
    st.image(logo, use_column_width=True)

with header_col2:
    # 두 번째 열에 선택 박스를 추가합니다.
    st.session_state.language = st.selectbox(
        "Language",
        ["KO", "EN", "CN", "JP"],
        index=["KO", "EN", "CN", "JP"].index(st.session_state.language)
    )

# 현재 선택된 옵션에 따라 화면을 업데이트합니다.(여기 챗봇 코드 넣어)
