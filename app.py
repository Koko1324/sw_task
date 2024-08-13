import streamlit as st
from PIL import Image

# 페이지 레이아웃 설정
st.set_page_config(layout="wide")

# 로고 이미지를 열고, 크기를 조절합니다.
logo = Image.open("logo.png")

# 언어 설정 초기화
if 'language' not in st.session_state:
    st.session_state.language = 'EN'  # 기본값으로 영어 선택

# 각 언어에 대한 텍스트 정의
translations = {
    "KO": {
        "home": "홈",
        "select_language": "언어 선택",
        "selected_language": "선택된 언어",
        "dynamic_text": "실시간 텍스트 업데이트 중",
        "apply_button": "적용"  # Apply 버튼에 대한 번역
    },
    "EN": {
        "home": "Home",
        "select_language": "Language",
        "selected_language": "Selected Language",
        "dynamic_text": "Real-time text updating",
        "apply_button": "Apply"  # Apply 버튼에 대한 텍스트
    },
    "CN": {
        "home": "主页",
        "select_language": "语言",
        "selected_language": "选择的语言",
        "dynamic_text": "实时文本更新中",
        "apply_button": "应用"  # Apply 버튼에 대한 번역
    },
    "JP": {
        "home": "ホーム",
        "select_language": "言語",
        "selected_language": "選択した言語",
        "dynamic_text": "リアルタイムテキストの更新中",
        "apply_button": "適用"  # Apply 버튼에 대한 번역
    }
}

# 현재 언어에 따른 텍스트 가져오기
current_language = st.session_state.language

def get_translation(key):
    """주어진 키에 대한 현재 언어의 번역을 반환합니다."""
    return translations[current_language].get(key, key)

# 헤더 섹션을 만들기 위해 열(column)을 나눕니다.
header_col1, header_col2 = st.columns([1, 4])

with header_col1:
    # 첫 번째 열에 로고 이미지를 추가합니다.
    st.image(logo, use_column_width=True)

with header_col2:
    # 열을 다시 나누어 언어 선택 박스를 오른쪽 상단에 작게 배치
    _, selectbox_col = st.columns([4, 1])  # 왼쪽에 빈 공간을 두어 오른쪽에 배치

    with selectbox_col:
        languages = ["KO", "EN", "CN", "JP"]
        selected_index = languages.index(st.session_state.language)
        selected_language = st.selectbox(
            get_translation("select_language"),  # 선택된 언어에 따라 레이블 변경
            languages,
            index=selected_index,
            key='language_selectbox'
        )

        # Apply 버튼 추가 (아무 기능도 없음)
        st.button(get_translation("apply_button"))  # 버튼 클릭 시 아무 작업도 하지 않음

