import streamlit as st
from PIL import Image
import time

# 페이지 레이아웃 설정
st.set_page_config(layout="wide")

# 슬라이드 쇼에 사용할 이미지 파일 경로를 리스트로 만듭니다.
image_files = ["image1.jpeg", "image2.jpeg", "image3.jpeg"]  # 파일명을 실제 이미지 파일명으로 바꾸세요.

# 세션 상태를 초기화합니다.
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = '홈'

# 헤더 섹션을 만들기 위해 열(column)을 나눕니다.
header_col1, header_col2 = st.columns([1, 5])

with header_col1:
    # 첫 번째 열에 로고 이미지를 추가합니다.
    logo = Image.open("logo.png")
    st.image(logo, use_column_width=True)

with header_col2:
    # 두 번째 열에 선택 박스를 추가합니다.
    st.session_state.selected_option = st.selectbox(
        "Select Option", 
        ["홈", "챗봇"],
        index=["홈", "챗봇"].index(st.session_state.selected_option)
    )

# 버튼 클릭 후 새로고침을 위한 처리
def go_to_chatbot():
    st.session_state.selected_option = "챗봇"

# 현재 선택된 옵션에 따라 화면을 업데이트합니다.
if st.session_state.selected_option == "홈":
    st.write("일정에 맞는 여행 코스를 짜드릴게요")

    # 슬라이드 쇼 구현
    for image_file in image_files:
        image = Image.open(image_file)
        st.image(image, use_column_width=True)
        time.sleep(3)  # 3초 간격으로 이미지 전환
        st.experimental_rerun()  # 페이지 리프레시

    button_clicked = st.button("챗봇으로 여행 코스 짜기(더블 클릭)")
    if button_clicked:
        go_to_chatbot()
elif st.session_state.selected_option == "챗봇":
    st.write("챗봇 코드 넣는곳")
